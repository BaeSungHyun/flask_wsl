from flask import Flask
app = Flask(__name__)

print("__name__", __name__)
print("DEBUG", app.config["DEBUG"])

@app.route("/")
def index():
    return "hello world swdwd48"

# if __name__ == "__main__": # Flask가 할 때는  __name__ app, 여기서 하면 __name__ main
#     print("run")
#     app.run(debug=True, host=5501, host="localhost")