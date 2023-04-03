from flask import Flask

db = "database"

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        app.logger.info("RUN HELLO WORLD")
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

    ''' === Request hook, Context control1 === '''
    from flask import g, current_app

    @app.before_first_request  # only at first request
    def before_first_request():
        app.logger.info("BEFORE_FIRST_REQUEST")
    
    @app.before_request # before business logic on request, this occurs
    def before_request():
        g.test = True
        app.logger.info("BEFORE_REQUEST")

    @app.after_request
    def after_request(response): # take response as parameter
        app.logger.info(f"g.test: {g.test}")
        print("mode: ", current_app.config)
        print(app.config["DEBUG"])
        g.test = False
        app.logger.info("AFTER_REQUEST")
        return response
    
    @app.teardown_request # when request is popped
    def teardown_request(exception): # take exception(error) as parameter
        print(g.test)
        app.logger.info("TEARDOWN_REQEUST")

    @app.teardown_appcontext # when appcontext is popped
    def teardown_appcontext(exception):
        app.logger.info("TEARDOWN_APPCONTEXT")

    return app