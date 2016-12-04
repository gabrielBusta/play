CREATE OR REPLACE FUNCTION public.create_playlist(IN _username text,
                                                  IN playlist_title text)
RETURNS void AS $function$
DECLARE
    user_id_var integer;
BEGIN
    SELECT id INTO user_id_var FROM auth_user WHERE username = _username;

    INSERT INTO app_playlist (title, profile_id)
    VALUES (playlist_title, user_id_var);
END;
$function$ LANGUAGE 'plpgsql' VOLATILE;
