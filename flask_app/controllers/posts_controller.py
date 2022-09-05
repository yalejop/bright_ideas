from flask import render_template, redirect, session, request, flash

from flask_app import app
from flask_app.models.likes import Like

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

@app.route('/bright_ideas/<int:id>')
def show_post(id):
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario)
    
    formulario_post = { "id": id }
    formulario_likes = { "id": id }
    
    post = Post.get_post_by_id(formulario_post)
    
    likes = Like.get_users_who_liked(formulario_likes)
    
    return render_template('show_post.html', user=user, post=post, likes=likes)

@app.route('/edit/posts/<int:id>') 
def edit_recipe(id):
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    formulario = {
        "id": session['user_id']
    }

    user = User.get_by_id(formulario) #Usuario que inició sesión

    formulario_post = { "id": id }
    
    posts = Post.get_post_by_id(formulario_post)

    return render_template('edit_post.html', user=user, posts=posts)

@app.route('/update/posts/<int:id>', methods=['POST'])
def update_posts(id):
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    if not Post.validate_post(request.form):
        return redirect('/edit/posts/'+ request.form['id']) 

    Post.update(request.form)

    return redirect('/dashboard')

@app.route('/delete/posts/<int:id>')
def delete_posts(id):
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    formulario = {"id": id}
    
    Post.delete(formulario)

    return redirect('/dashboard')
