from flask_app import app

#importando controlador
from flask_app.controllers import users_controller
from flask_app.controllers import posts_controller
from flask_app.controllers import likes_controller


if __name__=='__main__':
    app.run(debug=True)