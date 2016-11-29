CREATE OR REPLACE VIEW public.user_library AS
SELECT auth_user.id,
       auth_user.username,
       app_recording.title AS song,
       app_recording.length AS duration,
       app_album.title AS album,
       app_artist.name AS artist
FROM auth_user
JOIN app_profile_recordings ON app_profile_recordings.profile_id = auth_user.id
JOIN app_recording ON app_recording.id = app_profile_recordings.recording_id
JOIN app_artist ON app_artist.id = app_recording.artist_id
JOIN app_album ON app_album.id = app_recording.album_id;
