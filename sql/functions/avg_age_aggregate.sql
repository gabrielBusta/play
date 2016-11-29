CREATE OR REPLACE FUNCTION public.avg_age_final(IN dobs date[])
RETURNS double precision AS $function$
DECLARE
    dob date;
    age_as_interval interval;
    age_in_years double precision;
    total_years double precision;
    num_ages double precision;
    avgerage double precision;
BEGIN
    IF dobs IS NULL THEN
        RETURN NULL;
    END IF;

    total_years := 0;

    FOREACH dob IN ARRAY dobs LOOP
        age_as_interval := age(dob::timestamp);
        age_in_years := EXTRACT(YEAR FROM age_as_interval);
        total_years := total_years + age_in_years;
    END LOOP;

    num_ages := array_length(dobs, 1);
    avgerage := total_years / num_ages;

    RETURN avgerage;
END;
$function$ LANGUAGE 'plpgsql' IMMUTABLE;

DROP AGGREGATE IF EXISTS avg_age(date);

CREATE AGGREGATE avg_age(date) (
  SFUNC = array_append,
  STYPE = date[],
  FINALFUNC = avg_age_final
);
