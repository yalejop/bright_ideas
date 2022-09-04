from flask import render_template, redirect, session, request, flash

from flask_app import app

from flask_app.models.users import User
from flask_app.models.posts import Post
from flask_app.models.likes import Like


@app.route('/dashboard/create/like', methods=['POST'])
def create_like():
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    Like.save_likes_in_db(request.form)
    
    return redirect('/dashboard')