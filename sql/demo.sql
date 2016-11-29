SELECT * FROM get_user_library('silverfrog437');
SELECT * FROM get_user_library('orangefish325');

SELECT * FROM search_library_songs_by_title('silverfrog437', 'さわやかな朝');
SELECT * FROM search_library_songs_by_title('goldenpeacock960', 'さわやかな朝');

SELECT * FROM search_library_songs_by_title('silverfrog437', 'la ');
SELECT * FROM search_library_songs_by_title('orangefish325', 'la ');

SELECT * FROM search_songs_by_title('water');
SELECT * FROM search_songs_by_title('amor');
SELECT * FROM search_songs_by_title('water', 'silverfrog437');
SELECT * FROM search_songs_by_title('water', 'goldenpeacock960');
SELECT * FROM search_songs_by_title('water', 'orangefish325');

SELECT * FROM max_song_price();

SELECT * FROM percentage_categories();

SELECT avg_age(dob) FROM app_profile WHERE user_id = 1780 OR user_id = 1781 OR user_id = 1782;

SELECT avg_age(dob) FROM app_profile;

SELECT avg_age(dob) FROM app_profile WHERE user_id = 1;

SELECT avg_age(dob) AS "avgerage user age (United States)"
FROM user_location_currency
WHERE country_code = 'US';

SELECT avg_age(dob) AS "avgerage user age (Denmark)"
FROM user_location_currency
WHERE country_code = 'DK';

SELECT avg_age(dob) AS "avgerage user age (Brazil)"
FROM user_location_currency
WHERE country_code = 'BR';

SELECT avg_age(dob) AS "avgerage user age (Germany)"
FROM user_location_currency
WHERE country_code = 'DE';
