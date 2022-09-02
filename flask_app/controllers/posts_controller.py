from flask import render_template, redirect, session, request, flash

from flask_app import app

from flask_app.models.users import User
from flask_app.models.posts import Post


@app.route('/dashboard/create/post', methods=['POST'])
def create_post():
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')

    if not Post.validate_post(request.form): 
        return redirect('/dashboard')

    Post.save(request.form)
    return redirect('/dashboard')

