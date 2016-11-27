/* find the average length of a song */
SELECT minutes, seconds
FROM
    (SELECT floor((avg(length) / 1024) / 60) AS minutes FROM app_recording) AS minutes_table
NATURAL JOIN
    (SELECT round((avg(length) / 1024 ) % 60) AS seconds FROM app_recording) AS seconds_table;

    SELECT
    	username_recordings.username,
    	username_recordings.song_title,
    	username_recordings.length,
    	app_album.title AS album_title,
    	username_recordings.artist_id
    FROM
    (
    	SELECT *
    	FROM username_recordings JOIN app_album
    	ON username_recordings.album_id = app_album.id where username = 'beautifultiger854';
