CREATE OR REPLACE FUNCTION public.format_time(IN time_units integer)
RETURNS text AS $function$
DECLARE
    minutes integer;
    seconds integer;
    duration text;
BEGIN
    minutes := FLOOR((time_units / 1024) / 60);
    seconds := ROUND((time_units / 1024) % 60);
    IF seconds < 10 THEN
        duration := CAST(minutes AS text) || ':0' || CAST(seconds AS text);
    ELSE
        duration := CAST(minutes AS text) || ':' || CAST(seconds AS text);
    END IF;
    RETURN duration;
END;
$function$ LANGUAGE 'plpgsql' IMMUTABLE;
