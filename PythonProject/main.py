from flask import Flask, render_template, request

app = Flask(__name__)

app.debug = True

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == "POST":
        precio = 9000
        nombre = request.form["nombre"]
        edad = int(request.form["edad"])
        pintura = int(request.form["pintura"])

        if (edad >= 18 and edad <= 30):
            return render_template("ejercicio1.html", nombre = nombre, total = f"${precio * pintura}", descuento = f"${(precio * pintura) * 0.15}", pago = f"${(precio * pintura) * 0.85}")
        elif (edad > 30):
            return render_template("ejercicio1.html", nombre = nombre, total = f"${precio * pintura}", descuento = f"${(precio * pintura) * 0.25}", pago = f"${(precio * pintura) * 0.75}")
        else:
            return render_template("ejercicio1.html", nombre = nombre, total = f"${precio * pintura}", descuento = f"${0}", pago = f"${precio * pintura}")

    return render_template("ejercicio1.html")

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == "POST":
        usuario1 = ["juan", "admin", "Administrador"]
        usuario2 = ["pepe", "user", "Usuario"]

        nombre = request.form["nombre"]
        contraseña = request.form["contraseña"]

        if (nombre == usuario1[0] and contraseña == usuario1[1]):
            return render_template("ejercicio2.html", mensaje = f"Bienvenido {usuario1[2]} {usuario1[0]}.")
        elif (nombre == usuario2[0] and contraseña == usuario2[1]):
            return render_template("ejercicio2.html", mensaje = f"Bienvenido {usuario2[2]} {usuario2[0]}.")
        else:
            return render_template("ejercicio2.html", mensaje = "Usuario o contraseña incorrectos.")

    return render_template("ejercicio2.html")

if __name__ == '__main__':
    app.run()