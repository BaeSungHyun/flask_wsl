from flask import Flask
from flask import render_template

db = "database"

def create_app():
    app = Flask(__name__)

    if app.config['DEBUG']:
        app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 1  # 바로 갱신. 캐시에 저장 X.

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.errorhandler(404)
    def page_404(error):
        return render_template('404.html'),404
    return app