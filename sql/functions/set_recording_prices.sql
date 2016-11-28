CREATE OR REPLACE FUNCTION public.set_recording_prices()
RETURNS void AS $function$
DECLARE
    recording_cursor NO SCROLL CURSOR FOR SELECT * FROM app_recording;
BEGIN

    OPEN recording_cursor;

    LOOP
       MOVE recording_cursor;
       EXIT WHEN NOT FOUND;
       UPDATE app_recording
       SET price = random() + 0.5
       WHERE CURRENT OF recording_cursor;
    END LOOP;

    CLOSE recording_cursor;
END;
$function$ LANGUAGE 'plpgsql' VOLATILE;
