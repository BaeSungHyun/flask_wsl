from flask import Flask

db = "database"

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "hello world swdwd48"

    '''=== Routing Practices ==='''
    from markupsafe import escape
    from flask import redirect, jsonify, url_for

    @app.route('/test/name/<name>') # <>: parameter need to be used in def under. Default type is "string"
    def name(name):
        return f"My name is {name}, {escape(type(name))}" 

    @app.route('/test/id/<int:id>')
    def id(id):
        return "ID is %d" % id
    
    @app.route('/test/path/<path:subpath>')
    def path(subpath):
        return subpath

    @app.route('/test/json')
    def json():
        return jsonify([{"Hello":"world"}])

    @app.route('/test/redirect/<path:subpath>')
    def redirect_url(subpath):
        return redirect(subpath)
    
    @app.route('/test/urlfor')
    def urlfor():
        return redirect(url_for('name', name="baebae")) # first parameter: 'def' name,
    
    @app.route('/test/urlfor/<path:subpath>')
    def urlfor2(subpath):
        return redirect(url_for('path', subpath=subpath)) # second parameter: parameter for given 'def' 

    return app