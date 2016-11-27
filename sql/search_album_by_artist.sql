CREATE OR REPLACE FUNCTION public.search_albums_by_artist_name(IN artist_name_query text)
    RETURNS TABLE (
      album_title character varying(300),
      artist_name character varying(100),
      release_date date,
      release_status character varying(30),
      artist_category character varying(9),
      artist_description character varying(100),
      album_barcode bigint
    )
    LANGUAGE 'plpgsql'
    NOT LEAKPROOF
AS $function$
BEGIN
	RETURN QUERY
	SELECT
		app_album.title,
		app_artist.name,
		app_album.date,
		app_album.status,
		app_artist.category,
    app_artist.disambiguation,
		app_album.barcode
	FROM app_album JOIN app_artist ON app_album.artist_id = app_artist.id
    WHERE LOWER(app_artist.name) ~ LOWER(artist_name_query);
END;
$function$;

ALTER FUNCTION public.search_albums_by_artist_name(text)
    OWNER TO postgres;
