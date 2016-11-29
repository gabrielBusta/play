CREATE OR REPLACE FUNCTION public.percentage_categories(OUT group_percent double precision,
                                                        OUT person double precision,
                                                        OUT orchestra double precision,
                                                        OUT choir double precision,
                                                        OUT character_percent double precision,
                                                        OUT other double precision)
RETURNS record
AS $function$
DECLARE
total double precision;
num_group double precision;
num_person double precision;
num_orchestra double precision;
num_choir double precision;
num_character_percent double precision;
num_other double precision;


BEGIN
    SELECT COUNT(*) INTO total FROM app_artist;
    SELECT COUNT(*) INTO num_group FROM app_artist WHERE category = 'Group';
    SELECT COUNT(*) INTO num_person FROM app_artist WHERE category = 'Person';
    SELECT COUNT(*) INTO num_orchestra FROM app_artist WHERE category = 'Orchestra';
    SELECT COUNT(*) INTO num_choir FROM app_artist WHERE category = 'Choir';
    SELECT COUNT(*) INTO num_character_percent FROM app_artist WHERE category = 'Character';
    SELECT COUNT(*) INTO num_other FROM app_artist WHERE category = 'Other';

    group_percent= (num_group/total)* 100;
    person=(num_person/total)*100;
    orchestra=(num_orchestra/total)*100;
    choir=(num_choir/total)*100;
    character_percent=(num_character_percent/total)*100;
    other=(num_other/total)*100;

END;
$function$ LANGUAGE 'plpgsql' STABLE;
