from flask import request, redirect, url_for, render_template
from app_config import Config  

def setup_routes(app):
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            from hash_utils import sha512  
            encrypted_password = sha512(password)
            cnxn = Config.get_db_connection()
            cursor = cnxn.cursor()
            cursor.execute("INSERT INTO Usuario (Usuario, Contrasenia) VALUES (?, ?)", username, encrypted_password)
            cursor.commit()
            return render_template('login.html')
        else:
            return render_template('register.html')

