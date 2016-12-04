CREATE OR REPLACE FUNCTION public.delete_account(IN auth_username text)
RETURNS void AS $function$
DECLARE
    i integer;
    user_id_var integer;
    user_playlist_ids integer[];
BEGIN
    SELECT id INTO user_id_var FROM auth_user WHERE username = auth_username;

    /* delete the user's music library */
    DELETE FROM app_profile_recordings WHERE profile_id = user_id_var;

    /* delete the user's playlists */
    user_playlist_ids := ARRAY(SELECT id
                               FROM app_playlist
                               WHERE profile_id = user_id_var);

    FOREACH i IN ARRAY user_playlist_ids
    LOOP
        DELETE FROM app_playlist_recordings WHERE playlist_id = i;
    END LOOP;

    /* delete the user's profile */
    DELETE FROM app_profile WHERE user_id = user_id_var;

    /* delete the user's account */
    DELETE FROM auth_user WHERE id = user_id_var;
END;
$function$ LANGUAGE 'plpgsql' VOLATILE;
