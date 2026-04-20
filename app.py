from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        mensaje = request.form.get("mensaje")

        return render_template("mensaje.html", nombre=nombre)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)