CREATE OR REPLACE VIEW public.user_location_currency AS
SELECT app_profile.user_id,
       auth_user.username,
       app_country.name AS country,
       app_currency.name AS currency,
       app_currency.iso_code AS currency_code,
       app_currency.usd_rate
FROM auth_user
JOIN app_profile
ON app_profile.user_id = auth_user.id
JOIN app_country
ON app_country.id = app_profile.country_id
JOIN app_country_currencies
ON app_country_currencies.country_id = app_country.id
JOIN app_currency
ON app_currency.id = app_country_currencies.currency_id;
