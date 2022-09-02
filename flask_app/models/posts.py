from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Post:
    
    def __init__(self, data):
        self.id = data['id']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']
        
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
        query = "SELECT * FROM posts" 
        results = connectToMySQL('bright_ideas').query_db(query) #Lista de diccionarios
        posts = []
        for post in results:
            posts.append(cls(post)) #cls(appointments) -> Instancia de appointment, Agregamos la instancia a mi lista de appointments
        return posts
        
        