from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Like:
    
    def __init__(self, data):
        self.id = data['id']
        self.posts_id = data['posts_id']
        self.users_id = data['users_id']
        self.likes = data['likes']
        
        self.full_name = data['full_name']
        self.alias = data['alias']
        

    @classmethod
    def save_likes_in_db(cls, formulario):
        query = "INSERT INTO likes (posts_id, users_id, likes) VALUES ( %(posts_id)s, %(users_id)s, %(likes)s )"
        results2 = connectToMySQL('bright_ideas').query_db(query, formulario)
        
        query = "UPDATE posts SET post_likes = post_likes + 1 WHERE posts.id = %(posts_id)s;"
        
        result = connectToMySQL('bright_ideas').query_db( query, formulario )
        return result
    
    @classmethod
    def get_users_who_liked(cls, formulario):
        query = "SELECT DISTINCT full_name, alias FROM likes LEFT JOIN users ON users.id = likes.users_id WHERE posts_id = %(id)s"
        result = connectToMySQL('bright_ideas').query_db( query, formulario)
        # likes = []
        # for like in result:
        #     likes.append(cls(like))
        # return likes
        return result
    