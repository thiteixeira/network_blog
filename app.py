# export FLASK_APP=app.py
# debug mode: export FLASK_ENV=development
# flask run

from flask import Flask, render_template, send_from_directory, request


app = Flask(__name__, static_url_path='/static')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dns")
def dns():
    return render_template("dns.html")


@app.route("/linux")
def linux():
    return render_template("linux.html")


@app.route("/routing")
def routing():
    return render_template("routing.html")


@app.route("/connectivity")
def connectivity():
    return render_template("connectivity.html")


@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


if __name__ == '__main__':
    app.run()
