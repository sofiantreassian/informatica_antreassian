from flask import Flask, render_template

app = Flask(_name_) #Me refiero a la aplicacion por la palabra app. Instanciamos app

@app.get("/") #Le asociamos una ruta a app
def home(): #Es el metodo que me permite mostrar los datos que estan asociados a la pagina( en este caso ninguno)
    return render_template("casa.html")                 
