CREATE OR REPLACE FUNCTION public.avg_song_len(OUT minutes integer, OUT seconds integer)
 RETURNS record
 LANGUAGE plpgsql
AS $function$
BEGIN

        SELECT floor((avg(length) / 1024) / 60) FROM app_recording INTO minutes;

        SELECT round((avg(length) / 1024) % 60) FROM app_recording INTO seconds;

END;
$function$
