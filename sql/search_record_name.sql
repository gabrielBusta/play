CREATE OR REPLACE FUNCTION public.search_records_by_name(IN record_name_query text)
    RETURNS TABLE (
      record_name character varying As title(300),
      formatted_length(length) AS length,
      artist_name character varying As artist(100),
      album_title character varying(300),
      release_date date
      artist_category character varying(9),
    )
    LANGUAGE 'plpgsql'
    NOT LEAKPROOF
AS $function$
BEGIN
	RETURN QUERY
	SELECT
    app_recording.title,
    app_recording.length,
		app_artist.name,
    app_album.title,
		app_album.date,
		app_artist.category,

    FROM app_recording
    JOIN app_artist ON app_recording.artist_id = app_artist.id
    JOIN app_album ON app_recording.album_id= app_album.id
      WHERE LOWER(app_recording.title) ~ LOWER(record_name_query);
END;
$function$;

ALTER FUNCTION public.search_albums_by_artist_name(text)
    OWNER TO postgres;
