## 4. Querying a normalized database ##

conn = sqlite3.connect("academy_awards.db")

q='''
SELECT ceremonies.year, nominations.movie 
FROM nominations 
INNER JOIN ceremonies
ON nominations.ceremony_id == ceremonies.id
WHERE nominations.nominee == 'Natalie Portman';
'''

portman_movies = conn.execute(q).fetchall()

print(portman_movies)


## 7. Join table ##

conn = sqlite3.connect("academy_awards.db")

q_movies_actors='''
SELECT * FROM movies_actors LIMIT 5;
'''

q_actors='''
SELECT * FROM actors LIMIT 5;
'''

q_movies='''
SELECT * FROM movies LIMIT 5;
'''

five_join_table = conn.execute(q_movies_actors).fetchall()
five_actors = conn.execute(q_actors).fetchall()
five_movies = conn.execute(q_movies).fetchall()

print(five_join_table, five_actors, five_movies)

## 9. Querying a many-to-many relation ##

conn = sqlite3.connect("academy_awards.db")

q='''
SELECT actors.actor, movies.movie FROM movies
INNER JOIN movies_actors ON movies.id == movies_actors.movie_id
INNER JOIN actors ON movies_actors.actor_id == actors.id
WHERE movies.movie="The King's Speech"
'''

kings_actors = conn.execute(q).fetchall()
print(kings_actors)

## 10. Practice: querying a many-to-many relation ##

conn = sqlite3.connect("academy_awards.db")

q='''
SELECT movies.movie, actors.actor FROM movies
INNER JOIN movies_actors ON movies.id == movies_actors.movie_id
INNER JOIN actors ON movies_actors.actor_id == actors.id
WHERE actors.actor="Natalie Portman"
'''

portman_joins = conn.execute(q).fetchall()
print(portman_joins)