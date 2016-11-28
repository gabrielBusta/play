SELECT
song_title AS title,
formatted_length(length) AS length,
album_title AS album,
artist_name AS artist
FROM get_library_by_username('silverfrog437');
