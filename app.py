from flask import Flask, render_template, request
from controller.dao import VueloDAO

app = Flask(__name__)
vuelo_dao = VueloDAO()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        vuelo_dao.quitar_vuelo()
    return render_template('index.html', vuelos=vuelo_dao.todos(), vuelo=vuelo_dao.ver_primero())

@app.route('/agregar', methods=['POST', 'GET'])
def agregar_vuelo():
    if request.method == 'POST':
        codigo = request.form['codigo']
        aerolinea = request.form['aerolinea']
        destino = request.form['destino']
        tipo = request.form['tipo']
        if tipo == "Emergencia":
            vuelo_final= vuelo_dao.agregar_primero(codigo, aerolinea, destino, tipo)
        else:
            vuelo_final= vuelo_dao.agregar_vuelo(codigo, aerolinea, destino, tipo)
        if not vuelo_final:
            return render_template('agregar.html', error="El vuelo ya existe")
        return render_template('index.html', vuelos=vuelo_dao.todos(), vuelo=vuelo_dao.ver_primero())
    return render_template('agregar.html')

@app.route('/ver', methods=['GET', 'POST'])
def ver_vuelo():
    vuelo = vuelo_dao.ver_primero()
    return render_template('ver.html', vuelos=vuelo_dao.todos(), vuelo=vuelo)

if __name__ == '__main__':
    app.run(debug=True)