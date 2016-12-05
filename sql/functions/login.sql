CREATE OR REPLACE FUNCTION public.login(IN auth_username text,
                                        IN auth_password text)
RETURNS boolean AS $function$
DECLARE
    user_id_var integer;
BEGIN
    PERFORM *
    FROM auth_user
    WHERE username = auth_username AND password = auth_password;

    IF NOT FOUND THEN
        RETURN false;
    ELSE
        UPDATE auth_user SET last_login = now()
        WHERE username = auth_username AND password = auth_password;
        RETURN true;
    END IF;
END;
$function$ LANGUAGE 'plpgsql' VOLATILE;
