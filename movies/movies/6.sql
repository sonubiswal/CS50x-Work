-- 6. Average rating of movies in 2012
SELECT AVG(rating) FROM movies
JOIN ratings ON movies.id = ratings.movie_id
WHERE movies.year = 2012;
