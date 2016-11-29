CREATE OR REPLACE FUNCTION public.avg_age_of_audience(IN artist_name text)
RETURNS double precision AS $function$
DECLARE
    result double precision;
BEGIN
    SELECT avg_age(app_profile.dob) INTO result
    FROM user_library
    JOIN app_profile ON user_library.id = app_profile.user_id
    WHERE user_library.artist = artist_name;
    RETURN result;
END;
$function$ LANGUAGE 'plpgsql' STABLE;
