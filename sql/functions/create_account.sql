CREATE OR REPLACE FUNCTION public.create_account(IN auth_password text,
                                                 IN auth_username text,
                                                 IN auth_first_name text,
                                                 IN auth_last_name text,
                                                 IN auth_email text,
                                                 IN profile_cell text,
                                                 IN profile_phone text,
                                                 IN profile_street text,
                                                 IN profile_city text,
                                                 IN profile_state text,
                                                 IN profile_post_code text,
                                                 IN profile_dob text,
                                                 IN profile_gender text,
                                                 IN profile_country_code text)
RETURNS void AS $function$
DECLARE
    user_id_var integer;
    country_id_var integer;
BEGIN
    INSERT INTO auth_user (password, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined)
    VALUES (auth_password, false, auth_username, auth_first_name, auth_last_name, auth_email, false, true, now())
    RETURNING id INTO user_id_var;

    SELECT id INTO country_id_var FROM app_country WHERE alpha2code = profile_country_code;

    INSERT INTO app_profile (user_id, cell, phone, street, city, state, post_code, dob, gender, country_id)
    VALUES (user_id_var, profile_cell, profile_phone, profile_street, profile_city,
            profile_state, profile_post_code, profile_dob::date, profile_gender, country_id_var);
END;
$function$ LANGUAGE 'plpgsql' VOLATILE;
