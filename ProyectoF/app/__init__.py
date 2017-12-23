from flask import Flask, flash, url_for, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clientes.sqlite3'
app.config['SECRET_KEY'] = 'uippc3'

db = SQLAlchemy(app)
class clientes(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    telefono = db.Column(db.String(50))
    email = db.Column(db.String(200),unique=True)
    mesa = db.Column(db.String(10), unique=True)

    def __init__(self, nombre, telefono, email, mesa):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.mesa = mesa

#@app.route('/')
#def mostrar_todo():
 #   return render_template('mostrar_todo.html', clientes=clientes.query.all())

@app.route('/', methods=['GET', 'POST'])
def nuevo():

     if request.method == 'POST':
      try:
        if not request.form['nombre'] or not request.form['telefono'] or not request.form['email'] \
                or not request.form['mesa']:


            flash('Por favor introduzca todos los campos', 'error')

        else:

             cliente = clientes(request.form['nombre'],
                                     request.form['telefono'],
                                     request.form['email'],
                                request.form['mesa'])


             db.session.add(cliente)
             db.session.commit()
             flash('Registro  con exito!')

             return redirect(url_for('nuevo'))

      except Exception as e:
          print(e)
          flash('mesa reservada')

     return render_template('nuevo.html')

if __name__ == '__main__':
    db.create_all()
app.run()
