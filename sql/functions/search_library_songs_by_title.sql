CREATE OR REPLACE FUNCTION public.search_library_songs_by_title(IN username_var text, IN song_title text)
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
    WHERE user_library.username = username_var AND LOWER(user_library.song) ~ LOWER(song_title);
END;
$function$ LANGUAGE 'plpgsql' STABLE;
