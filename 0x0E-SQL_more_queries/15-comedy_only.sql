-- list all Comedy shows
--
SELECT tv_shows.title FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.id=5
ORDER BY tv_shows.title;
