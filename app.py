from flask import Flask, render_template, request, redirect, url_for
from register import setup_routes
from app_config import Config  

app = Flask(__name__)
app.config['cnxn'] = Config.get_db_connection()  

setup_routes(app)  

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    from hash_utils import sha512 
    username = request.form['username']
    password = request.form['password']
    encrypted_password = sha512(password)
    cursor = app.config['cnxn'].cursor()
    cursor.execute("SELECT * FROM Usuario WHERE Usuario=? AND Contrasenia=?", username, encrypted_password)
    usuario = cursor.fetchone()
    if usuario:
        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'), debug=True)
