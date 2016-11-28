CREATE OR REPLACE VIEW public.username_library AS
 SELECT username_recordings_album.username,
    username_recordings_album.song_title,
    username_recordings_album.length,
    username_recordings_album.album_title,
    app_artist.name AS artist_name,
    app_artist.category AS artist_type
   FROM username_recordings_album
     JOIN app_artist ON username_recordings_album.artist_id = app_artist.id;

ALTER TABLE public.username_library
    OWNER TO postgres;
