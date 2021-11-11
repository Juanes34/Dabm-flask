from types import MethodType
from flask import Flask, render_template,request
from flask.wrappers import Request
import os
import random

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
        if resultado==True:
            return render_template("menu.html",title="Sistema DABM")
        else:
            return "Datos no válidos"

@app.route('/monitor')
def monitor():
    #consultar archivo parametros
    datos=getdatos()
    #obtener lectura
    lectura=random.randint(0,45)
    #enviar a la interfaz
    color=0
    if lectura>=int(datos[0][1]) and lectura<=int(datos[0][2]):
        color=1
    if lectura>=int(datos[1][1]) and lectura<=int(datos[1][2]):
        color=2
    if lectura>=int(datos[2][1]) and lectura<=int(datos[2][2]):
        color=3
    return render_template('monitor.html',datos=datos,lectura=lectura,color=color)

@app.route('/config')
def config():
    return render_template('config.html')

@app.route('/config1',methods=["POST"])
def config1():
    if request.method=="POST":
        bajo1=request.form['bajo1']
        bajo2=request.form['bajo2']
        normal1=request.form['normal1']
        normal2=request.form['normal2']
        alto1=request.form['alto1']
        alto2=request.form['alto2']
        print(bajo1)
        print(bajo2)
        print(alto1)
        return "Guardado"

def getdatos():
    directorio=os.path.dirname(__file__)
    archivo="bd/parametros.csv"
    ruta=os.path.join(directorio,archivo)
    f=open(ruta,"r")
    lineas=f.readlines()
    f.close()
    datos=[]
    for a in lineas:
        a=a.replace("\n","")
        a=a.split(";")
        datos.append(a)
    return datos
def verificar(usuario, password):
    cuentas=loadfromusers()
    cuent=False
    passw=False
    for a in cuentas:
        if usuario==a[0]:
            cuent=True
        if password==a[1]:
            passw=True
    if cuent==False:
        return False
    elif cuent==True and passw==False:
        return False
    elif cuent==True and passw==True:
        return True
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