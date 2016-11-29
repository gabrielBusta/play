CREATE OR REPLACE FUNCTION public.search_songs_by_title(IN song_title text, IN username_var text)
RETURNS TABLE(song character varying,
              duration text,
              album character varying,
              artist character varying,
              price text)
AS $function$
DECLARE
    rate double precision;
    currency_name character varying;
BEGIN
    SELECT user_location_currency.usd_rate INTO rate
    FROM user_location_currency
    WHERE user_location_currency.username = username_var;

	  SELECT user_location_currency.currency INTO currency_name
    FROM user_location_currency
    WHERE user_location_currency.username = username_var;

    RETURN QUERY
    SELECT app_recording.title,
           format_time(app_recording.length),
           app_album.title,
           app_artist.name,
           CAST(to_char(local_currency(app_recording.price, rate), 'FM999999999.00') AS text) || ' ' || currency_name
    FROM app_recording
    JOIN app_artist ON app_recording.artist_id = app_artist.id
    JOIN app_album ON app_recording.album_id= app_album.id
    WHERE LOWER(app_recording.title) ~ LOWER(song_title)
    ORDER BY app_album.date DESC;
END;
$function$ LANGUAGE 'plpgsql' STABLE;
