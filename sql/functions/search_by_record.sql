-- this searches by record change the name to what you want on the wizard
-- i had to redo it since i copy pasted wrong 
CREATE OR REPLACE FUNCTION public.sample(IN record_name text)
    RETURNS TABLE(
      song character varying(300),
      artist character varying(100),
      album character varying(300),
      release_date date,
      artist_type character varying
    )
    LANGUAGE 'plpgsql'
    VOLATILE
AS $function$
BEGIN
    RETURN QUERY
	SELECT
    app_recording.title,
	app_artist.name,
    app_album.title,
	app_album.date,
	app_artist.category

    FROM app_recording
    JOIN app_artist ON app_recording.artist_id = app_artist.id
    JOIN app_album ON app_recording.album_id= app_album.id
    WHERE LOWER(app_recording.title) ~ LOWER(record_name);
END;
$function$;
