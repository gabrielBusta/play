CREATE OR REPLACE FUNCTION public.add_song_to_playlist(IN _username text,
                                                       IN song_title text,
                                                       IN playlist_title text)
RETURNS void AS $function$
DECLARE
    user_id_var integer;
    recording_id_var integer;
    playlist_id_var integer;
BEGIN
    SELECT id INTO user_id_var FROM auth_user WHERE username = _username;

    SELECT id INTO playlist_id_var
    FROM app_playlist WHERE  title = playlist_title AND profile_id = user_id_var;

    SELECT id INTO recording_id_var FROM app_recording WHERE title = song_title;

    INSERT INTO app_playlist_recordings (playlist_id, recording_id)
    VALUES (playlist_id_var, recording_id_var);
END;
$function$ LANGUAGE 'plpgsql' VOLATILE;
