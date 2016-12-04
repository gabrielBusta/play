CREATE OR REPLACE FUNCTION public.create_account(IN auth_password character varying,
                                                 IN auth_username character varying,
                                                 IN auth_first_name character varying,
                                                 IN auth_last_name character varying,
                                                 IN auth_email character varying,
                                                 IN profile_cell character varying,
                                                 IN profile_phone character varying,
                                                 IN profile_street character varying,
                                                 IN profile_city character varying,
                                                 IN profile_state character varying,
                                                 IN profile_post_code character varying,
                                                 IN profile_dob text,
                                                 IN profile_gender character varying,
                                                 IN profile_country_code text)
RETURNS double precision AS $function$
DECLARE
    user_id_var integer;
    country_id_var integer;

BEGIN
    INSERT INTO auth_user (password, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined)
    VALUES (auth_password, false, auth_username, auth_first_name, auth_last_name, auth_email, false, true, now())
    RETURNING id INTO user_id_var;

    SELECT id INTO country_id FROM app_country WHERE alpha2code = profile_country_code;

    INSERT INTO app_profile (user_id, cell, phone, street, city, state, post_code, dob, gender)
END;
$function$ LANGUAGE 'plpgsql' VOLATILE;
