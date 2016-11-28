CREATE OR REPLACE FUNCTION public.formatted_length(IN length integer)
    RETURNS text
    LANGUAGE 'plpgsql'
    NOT LEAKPROOF
AS $function$
DECLARE
    minutes integer;
	  seconds integer;
    duration text;
BEGIN
    minutes := FLOOR((length / 1024) / 60);
    seconds := ROUND((length / 1024) % 60);
    IF seconds > 10 THEN
        duration := CAST(minutes AS text) || ':' || CAST(seconds AS text);
    ELSE
        duration := CAST(minutes AS text) || ':0' || CAST(seconds AS text);
    END IF;

    RETURN duration;
END;
$function$;

ALTER FUNCTION public.formatted_length(integer) OWNER TO postgres;
