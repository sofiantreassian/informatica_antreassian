#empezamos con web (lo otro era htts, http, res)

#vamos a diseñar una aplicacion web 

#api ---> rutas (endpoints) ---> url en las cuales se accede a los recursos

from flask import Flask 

app = Flask(__name__)

@app.get("/")
def home ():
    return "<p>Te damos la bienvenida a MacoWins </p>"

