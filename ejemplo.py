from types import MethodType
from flask import Flask, render_template,request
from flask.wrappers import Request

app=Flask(__name__)

@app.route('/')
def inicio():
    return render_template("login.html")

@app.route('/datos')
def datos():
    user = {"nombre" : "Juan"}
    return render_template("datos.html",title='Titulo personalizado',user=user)

@app.route('/validar',methods=["POST"])
def validar():
    if request.method=="POST":
        usuario=request.form['usuario']
        password=request.form['password']
        resultado=verificar(usuario,password)
        return resultado

def verificar(usuario, password):
    cuentas=loadfromusers()
    cuent=False
    passw=False
    for a in cuentas:
        if usuario==a[0]:
            cuent=True
        if password==a[1]:
            passw=True
    print(cuent)
    print(passw)
    if cuent==False:
        return "Usuario no existe"
    elif cuent==True and passw==False:
        return "Contraseña incorrecta"
    elif cuent==True and passw==True:
        return "Datos válidos"

def loadfromusers():
    users=[]
    total=[]
    #try:
    fileusers=open("/Users/usuario/OneDrive/Escritorio/Dabm/Flask/bd/users.csv","r")
    datos=fileusers.readlines()
    fileusers.close()
    for d in datos:
        users=[]
        d=d.replace("\n","")
        datos=d.split(";")
        usuario=datos[0]
        contraseña=datos[1]
        users.append(usuario)
        users.append(contraseña)
        total.append(users)
    return total
    #except:
        #pass

if __name__=="__main__":
    app.run(debug=True)