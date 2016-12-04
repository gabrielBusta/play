CREATE OR REPLACE FUNCTION public.avg_song_price()
RETURNS double precision
AS $function$
DECLARE
    result double precision;
BEGIN
    SELECT avg(price) FROM app_recording INTO result;
    RETURN result;
END;
$function$ LANGUAGE 'plpgsql' STABLE;
