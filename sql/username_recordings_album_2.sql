CREATE OR REPLACE VIEW public.username_recordings_album AS
 SELECT username_recordings.username,
    username_recordings.song_title,
    username_recordings.length,
    app_album.title AS album_title,
    username_recordings.artist_id
   FROM username_recordings
     JOIN app_album ON username_recordings.album_id = app_album.id;

ALTER TABLE public.username_recordings_album
    OWNER TO postgres;
