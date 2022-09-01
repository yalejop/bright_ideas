from flask import render_template, redirect, session, request, flash

from flask_app import app

#importando el modelo de User
from flask_app.models.users import User
from flask_app.models.appointments import Appointment

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

@app.route('/register', methods=['POST'])
def register():
    if not User.valida_usuario(request.form):
        return redirect('/')

    pwd = bcrypt.generate_password_hash(request.form['password']) #me encripta el password

    formulario = {
        'full_name': request.form['full_name'],
        'alias': request.form['alias'],
        'email': request.form['email'],
        'password': pwd
    }

    id = User.save(formulario) #guardando a mi usuario y recibo del ID del nuevo registro

    session['user_id'] = id #guardando el id de mi usuario

    return redirect('/dashboard')

#creando ruta para /register
@app.route('/login', methods=['POST'])
def login():
    user = User.get_by_email(request.form)
    if not user: #si user=False
        flash('E-mail no Encontrado', 'login')
        return redirect('/')

    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Password incorrecto', 'login')
        return redirect('/')

    session['user_id'] = user.id

    return redirect('/appointments')    

@app.route('/appointments')
def appointments():
    if 'user_id' not in session:
        return redirect('/')
    
    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario)

    appointments = Appointment.get_all()

    return render_template('appointments.html', usuario = user, appointments = appointments)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
