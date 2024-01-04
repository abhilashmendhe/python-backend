from app import app 

# @app.route("/")
# @app.route("/index")
# def index():
#     return "Hello, World"

@app.route("/")
@app.route("/index")
def index():
    user = {"username":"Abhilash"}
    return '''
    <html>
        <head>
            <title>Home Page - Microblog</title>
        </head>
        <body>
            <h1>Hello, '''+user["username"]+'''!</h1>
        </body>
    </html>
    '''