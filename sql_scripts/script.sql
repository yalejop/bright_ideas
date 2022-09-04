SELECT * FROM posts;

SELECT posts.*, alias FROM posts 
LEFT JOIN users ON users.id = posts.users_id 
WHERE users.id = 1;

SELECT posts.*, alias FROM posts 
LEFT JOIN users ON users.id = posts.users_id 
WHERE users.id