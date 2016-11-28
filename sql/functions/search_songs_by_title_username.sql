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
    SELECT app_currency.usd_rate INTO rate
    FROM auth_user
    JOIN app_profile
    ON app_profile.user_id = auth_user.id
    JOIN app_country
    ON app_country.id = app_profile.country_id
    JOIN app_country_currencies
    ON app_country_currencies.country_id = app_country.id
    JOIN app_currency
    ON app_currency.id = app_country_currencies.currency_id
    WHERE auth_user.username = username_var;

    SELECT app_currency.name INTO currency_name
    FROM auth_user
    JOIN app_profile
    ON app_profile.user_id = auth_user.id
    JOIN app_country
    ON app_country.id = app_profile.country_id
    JOIN app_country_currencies
    ON app_country_currencies.country_id = app_country.id
    JOIN app_currency
    ON app_currency.id = app_country_currencies.currency_id
    WHERE auth_user.username = username_var;

    RETURN QUERY
    SELECT app_recording.title,
           format_time(app_recording.length),
           app_album.title,
           app_artist.name,
           CAST(to_char(local_currency(app_recording.price, rate), 'FM999999999.00') AS text) || ' ' || currency_name
    FROM app_recording
    JOIN app_artist ON app_recording.artist_id = app_artist.id
    JOIN app_album ON app_recording.album_id= app_album.id
    JOIN app_country ON app_album.country_id = app_country.id
    WHERE LOWER(app_recording.title) ~ LOWER(song_title)
    ORDER BY app_album.date DESC;
END;
$function$ LANGUAGE 'plpgsql' STABLE;
