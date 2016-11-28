CREATE OR REPLACE FUNCTION public.get_library_by_username(IN username_query text)
    RETURNS TABLE (
      song_title character varying(300),
      length integer,
      album_title character varying(300),
      artist_name character varying(100),
      artist_type character varying(9)
    )
    LANGUAGE 'plpgsql'
    NOT LEAKPROOF
AS $function$
BEGIN
    RETURN QUERY
    SELECT
        username_library.song_title,
        username_library.length,
        username_library.album_title,
        username_library.artist_name,
        username_library.artist_type
    FROM username_library
    WHERE username_library.username = username_query;
END;
$function$;

ALTER FUNCTION public.get_library_by_username(text)
    OWNER TO postgres;
