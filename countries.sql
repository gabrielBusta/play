/* should be 250 */
-- SELECT COUNT(*) AS "countries" FROM app_country;

/* should be 111 */
-- SELECT COUNT(*) AS "languages" FROM app_language;

/* should be 42 */
-- SELECT COUNT(*) AS "timezones" FROM app_timezone;

-- SELECT COUNT(*) AS "country_lang" FROM app_country_languages;
-- SELECT * FROM  app_country_languages;

-- SELECT COUNT(*) AS "country_timezone" FROM app_country_timezones;
-- SELECT * FROM app_country_timezones;