from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Post:
    
    def __init__(self, data):
        self.id = data['id']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']
        self.post_likes = data['post_likes']
        
        self.alias = data['alias']
        
    @staticmethod
    def validate_post(formulario):
        es_valido = True
        
        if formulario['description'] == "":
            flash('Tu Idea debe tener algo de contenido', 'posts')
            es_valido = False
        elif len(formulario['description']) <= 3:
            flash('Tu idea debe tener mas de 3 letras', 'posts')
            es_valido = False

        return es_valido    
        
    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO posts (description, users_id) VALUES ( %(description)s, %(users_id)s )"
        results = connectToMySQL('bright_ideas').query_db(query, formulario)
        return results
    
    @classmethod
    def get_all(cls):
        query = "SELECT posts.*, alias FROM posts LEFT JOIN users ON users.id = posts.users_id ORDER BY post_likes DESC" 
        results = connectToMySQL('bright_ideas').query_db(query) #Lista de diccionarios
        posts = []
        for post in results:
            posts.append(cls(post)) #cls(appointments) -> Instancia de appointment, Agregamos la instancia a mi lista de appointments
        return posts

    @classmethod
    def get_post_by_id(cls, formulario): 
        query = "SELECT posts.*, alias FROM posts LEFT JOIN users ON users.id = posts.users_id WHERE posts.id = %(id)s" 
        result = connectToMySQL('bright_ideas').query_db(query, formulario) #recibimos una lista 
        post = cls(result[0]) #Creamos una instancia de receta
        return post
    
    @classmethod
    def get_posts_and_likes_by_user(cls, formulario):
        query = "SELECT COUNT(users_id) as posts_publicados, post_likes FROM posts WHERE users_id = %(id)s"
        result = connectToMySQL('bright_ideas').query_db( query, formulario)
        print(result)
        return result
    
    @classmethod
    def update(cls, formulario):   
        query = "UPDATE posts SET description = %(description)s WHERE id = %(id)s"
        result = connectToMySQL('bright_ideas').query_db(query, formulario)
        return result
    
    @classmethod
    def delete(cls, formulario):
        query = "DELETE FROM likes WHERE posts_id = %(id)s;"
        result1 = connectToMySQL('bright_ideas').query_db( query, formulario)
        
        query = "DELETE FROM posts WHERE posts.id = %(id)s"
        result = connectToMySQL('bright_ideas').query_db(query, formulario)
        print(result)
        return result
    