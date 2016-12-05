CREATE OR REPLACE FUNCTION public.update_password(IN auth_username text,
                                                  IN auth_password text,
                                                  IN new_password text)
RETURNS boolean AS $function$
BEGIN
    PERFORM *
    FROM auth_user
    WHERE username = auth_username AND password = auth_password;

    IF NOT FOUND THEN
        RETURN false;
    ELSE
        UPDATE auth_user SET password = new_password
        WHERE username = auth_username AND password = auth_password;
        RETURN true;
    END IF;
END;
$function$ LANGUAGE 'plpgsql' VOLATILE;
