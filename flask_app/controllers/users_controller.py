from flask import render_template, redirect, session, request, flash

from flask_app import app
from flask_app.models.likes import Like

#importando el modelo de User
from flask_app.models.users import User
from flask_app.models.posts import Post

#importando BCrypt (encriptar)
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app) #inicializando instancia de bcrypt

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register/')
def register_template():
    return render_template('register.html')

@app.route('/login/')
def login_template():
    return render_template('login.html')

@app.route('/register/register_user/', methods=['POST'])
def register():
    if not User.valida_usuario(request.form):
        return redirect('/register/')

    pwd = bcrypt.generate_password_hash(request.form['password']) #me encripta el password

    formulario = {
        'full_name': request.form['full_name'],
        'alias': request.form['alias'],
        'email': request.form['email'],
        'password': pwd
    }

    id = User.save(formulario) #guardando a mi usuario y recibo del ID del nuevo registro

    session['user_id'] = id #guardando el id de mi usuario

    return redirect('/login')

#creando ruta para /register
@app.route('/login/login_user/', methods=['POST'])
def login():
    user = User.get_by_email(request.form)
    if not user: #si user=False
        flash('E-mail no Encontrado', 'login')
        return redirect('/login/')

    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Password incorrecto', 'login')
        return redirect('/login/')

    session['user_id'] = user.id

    return redirect('/dashboard')  

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/login/')
    
    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario)
    
    posts = Post.get_all()
    
    # likes = Like.count_likes(formulario_post)
    
    # alias = Post.get_name_by_id(formulario)

    return render_template('dashboard.html', usuario = user, posts=posts)  

@app.route('/users/<int:id>')
def show_user(id):
    if 'user_id' not in session:
        return redirect('/')
    
    formulario = { "id": id }
    
    user = User.get_by_id(formulario)
    
    formulario_posts = { "id": id }
    
    posts = Post.get_posts_and_likes_by_user(formulario_posts)


    return render_template('show_user.html', usuario = user, posts= posts)

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')

# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html')
