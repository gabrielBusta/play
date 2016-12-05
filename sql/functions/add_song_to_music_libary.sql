CREATE OR REPLACE FUNCTION public.add_song_to_music_library(IN _username text,
                                                            IN song_title text)
RETURNS void AS $function$
DECLARE
    user_id_var integer;
    recording_id_var integer;
BEGIN
    SELECT id INTO user_id_var FROM auth_user WHERE username = _username;

    SELECT id INTO recording_id_var FROM app_recording WHERE title = song_title;

    INSERT INTO app_profile_recordings (profile_id, recording_id)
    VALUES (user_id_var, recording_id_var);
END;
$function$ LANGUAGE 'plpgsql' VOLATILE;
