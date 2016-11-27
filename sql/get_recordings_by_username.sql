CREATE OR REPLACE FUNCTION public.get_recordings_by_username(IN username_query text)
    RETURNS TABLE (
      song_title character varying(300),
      artist_name character varying(100),
      song_length integer
    )
    LANGUAGE 'plpgsql'
    NOT LEAKPROOF
AS $function$
BEGIN
	RETURN QUERY
  SELECT
    app_user_profile_recordings_recording.title,
    app_artist.name,
    app_user_profile_recordings_recording.length
  FROM
  (
    SELECT *
	  FROM
	  (
		  SELECT *
		  FROM
		(
			SELECT *
			FROM auth_user JOIN app_profile ON auth_user.id = app_profile.user_id
		)
		AS app_user_profile
    JOIN app_profile_recordings
    ON app_user_profile.user_id = app_profile_recordings.profile_id
	)
	AS app_user_profile_recordings
	JOIN app_recording
	ON app_user_profile_recordings.recording_id = app_recording.id
)
AS app_user_profile_recordings_recording
JOIN app_artist
ON app_user_profile_recordings_recording.artist_id = app_artist.id
WHERE username = username_query;
END;
$function$;

ALTER FUNCTION public.search_albums_by_artist_name(text)
    OWNER TO postgres;
