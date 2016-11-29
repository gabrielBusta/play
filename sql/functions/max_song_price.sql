CREATE OR REPLACE FUNCTION public.max_song_price()
RETURNS double precision
AS $function$
DECLARE
    result double precision;
BEGIN
    SELECT max(price) FROM app_recording INTO result;
    RETURN result;
END;
$function$ LANGUAGE 'plpgsql' STABLE;
