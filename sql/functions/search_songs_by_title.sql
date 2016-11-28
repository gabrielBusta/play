CREATE OR REPLACE FUNCTION public.search_songs_by_title(IN song_title text)
RETURNS TABLE(song character varying,
              duration text,
              album character varying,
              artist character varying,
              release_date date,
              release_country character varying)
AS $function$
BEGIN
    RETURN QUERY
	  SELECT app_recording.title,
           format_time(app_recording.length),
	         app_artist.name,
           app_album.title,
	         app_album.date,
	         app_country.name
    FROM app_recording
    JOIN app_artist ON app_recording.artist_id = app_artist.id
    JOIN app_album ON app_recording.album_id= app_album.id
    JOIN app_country ON app_album.country_id = app_country.id
    WHERE LOWER(app_recording.title) ~ LOWER(song_title)
    ORDER BY app_album.date DESC;
END;
$function$ LANGUAGE 'plpgsql' STABLE;
