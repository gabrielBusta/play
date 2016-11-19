/* should be 250 */
-- SELECT * FROM app_country;

/* should be 111 */
-- SELECT COUNT(*) AS "languages" FROM app_language;

/* should be 42 */
-- SELECT COUNT(*) AS "timezones" FROM app_timezone;

-- SELECT * FROM app_country;
-- SELECT * FROM app_language;
-- SELECT * FROM app_country_languages;

-- SELECT * FROM app_country_languages WHERE country_id = 5;
-- SELECT * FROM app_country WHERE id = 5;
-- SELECT * FROM app_language WHERE id = 7 or id = 8;

-- SELECT COUNT(*) AS "country_lang" FROM app_country_languages;
-- SELECT * FROM  app_country_languages;

-- SELECT COUNT(*) AS "country_timezone" FROM app_country_timezones;
-- SELECT * FROM app_country_timezones;
