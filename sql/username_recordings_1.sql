CREATE OR REPLACE VIEW public.username_recordings AS
 SELECT username_recording_id.username,
    app_recording.title AS song_title,
    app_recording.length,
    app_recording.album_id,
    app_recording.artist_id
   FROM ( SELECT auth_user.username,
            app_profile_recordings.recording_id
           FROM auth_user
             JOIN app_profile_recordings ON auth_user.id = app_profile_recordings.profile_id) username_recording_id
     JOIN app_recording ON username_recording_id.recording_id = app_recording.id;

ALTER TABLE public.username_recordings
    OWNER TO postgres;
