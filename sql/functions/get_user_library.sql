CREATE OR REPLACE FUNCTION public.get_user_library(IN username_var text)
RETURNS TABLE(song character varying,
              duration text,
              album character varying,
              artist character varying)
AS $function$
BEGIN
    RETURN QUERY
    SELECT user_library.song,
           format_time(user_library.duration),
           user_library.album,
           user_library.artist
    FROM user_library
    WHERE user_library.username = username_var;
END;
$function$ LANGUAGE 'plpgsql' STABLE;
