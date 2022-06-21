from colorama import Cursor
from flask import Flask, flash, render_template, request, redirect
from datetime import datetime
import pymysql


db = pymysql.Connect(host="localhost", port=3306, user="root",
                     passwd="Zxzx0512zxzx0512.", db="blog")

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/pagina2")
def pagina2():
    return render_template("pagina2.html")


@app.route("/depresion")
def depresion():
    return render_template("depresion.html")


@app.route("/ansiedad")
def ansiedad():
    return render_template("ansiedad.html")


@app.route("/autoestima")
def autoestima():
    return render_template("autoestima.html")


@app.route("/bienestar")
def bienestar():
    return render_template("bienestar.html")


@app.route("/fatiga")
def fatiga():
    return render_template("fatiga.html")


@app.route("/soporte")
def soporte():
    return render_template("soporte.html")


@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")


@app.route("/foro")
def foro():
    return render_template("foro.html")


@app.route("/blog", methods=['GET', 'POST'])
def blog():
    cursor = db.cursor(pymysql.cursors.DictCursor)
    if request.method == "POST" and 'txtbusqueda' in request.form:
        sql = "SELECT * FROM blog.posts WHERE titulo like '%" + \
            request.form['txtbusqueda'] + "%'"
    else:
        sql = "SELECT * FROM blog.posts"
    cursor.execute(sql)
    blogs = cursor.fetchall()
    return render_template("blog.html", blogs=blogs)


@app.route("/agregar")
def agregar():
    return render_template("agregar.html")


@app.route("/create", methods=['POST', 'GET'])
def create():
    cursor = db.cursor(pymysql.cursors.DictCursor)
    titulo = request.form['titulo']
    texto = request.form['texto']
    now = datetime.now()
    sql = """INSERT INTO blog.posts (titulo,fecha,texto) values (%s,%s, %s)"""
    cursor.execute(sql, (titulo, now, texto))
    return redirect("blog")


@app.route('/edit/<id>',  methods=['GET', 'POST'])
def edit(id):
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT * FROM blog.posts WHERE id=id"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    return render_template("editar.html", id=id)


@app.route("/editar", methods=['GET', 'POST'])
def editar():
    titulo = request.form['titulo']
    texto = request.form['texto']
    now = datetime.now()
    cursor = db.cursor()
    cursor.execute(
        "UPDATE blog.posts SET titulo=%s,fecha=%s,texto=%s WHERE id =id values(titulo, now, texto)")


if __name__ == "__main__":
    app.run(debug=True)
