CREATE OR REPLACE FUNCTION public.get_user_library(IN username_query text)
RETURNS TABLE (song character varying(300),
               duration text,
               album character varying(300),
               artist character varying(100))
AS $function$
BEGIN
    RETURN QUERY
    SELECT user_library.song,
           format_time(user_library.duration),
           user_library.album,
           user_library.artist
    FROM user_library
    WHERE user_library.username = username_query;
END;
$function$ LANGUAGE 'plpgsql' STABLE NOT LEAKPROOF;
