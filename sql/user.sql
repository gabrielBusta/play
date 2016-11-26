SELECT first_name, last_name, region FROM
(SELECT * FROM auth_user JOIN app_profile ON auth_user.id = app_profile.user_id)
AS user_info
JOIN app_country ON user_info.country_id = app_country.id
WHERE first_name = 'abigail';
