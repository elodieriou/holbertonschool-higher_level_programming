-- list all shows contained in 'hbtn_0d_tvshows' witohut a genre linked
-- RIGHT JOINT without no intersection
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL;
