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
