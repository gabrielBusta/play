SELECT minutes, seconds
FROM
    (SELECT floor((avg(length) / 1024) / 60) AS minutes FROM app_recording) AS minutes_table
NATURAL JOIN
    (SELECT round((avg(length) / 1024 ) % 60) AS seconds FROM app_recording) AS seconds_table;
