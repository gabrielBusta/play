CREATE OR REPLACE FUNCTION public.search_songs_by_album(IN album_title text)
RETURNS TABLE(song character varying,
              duration text,
              album character varying,
              artist character varying,
              release_date date)
AS $function$
DECLARE
    album_id_var integer;
BEGIN
    SELECT id INTO album_id_var
    FROM app_album
    WHERE title = album_title;

    RETURN QUERY
    SELECT app_recording.title,
           format_time(app_recording.length),
           app_album.title,
           app_artist.name,
           app_album.date
    FROM app_recording
    JOIN app_artist ON app_recording.artist_id = app_artist.id
    JOIN app_album ON app_recording.album_id= app_album.id
    WHERE album_id = album_id_var;
END;
$function$ LANGUAGE 'plpgsql' STABLE;
