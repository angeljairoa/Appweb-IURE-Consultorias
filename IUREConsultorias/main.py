from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import pymongo  #conecta python con mongo base de datos
import certifi  #gestiona certificados digitales para la conexion remota

ca=certifi.where()
client = pymongo.MongoClient("mongodb+srv://adminangel:abcde12345@cluster0.pbm9pue.mongodb.net/?retryWrites=true&w=majority")
db=client.test
print(db)

baseDatos=client["iure-consultorias"]
print(baseDatos.list_collection_names())

app=Flask(__name__)
cors = CORS(app)
from Controladores.ControladorPaciente import ControladorPaciente
from Controladores.ControladorUsuario import ControladorUsuario
from Controladores.ControladorPersonal import ControladorPersonal
from Controladores.ControladorDocumento import ControladorDocumento
from Controladores.ControladorConsulta import ControladorConsulta
miControladorPaciente=ControladorPaciente()
miControladorUsuario=ControladorUsuario()
miControladorPersonal=ControladorPersonal()
miControladorDocumento=ControladorDocumento()
miControladorConsulta=ControladorConsulta()

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)

#CRUD Pacientes
@app.route("/pacientes",methods=['GET'])
def getPacientes():
    json=miControladorPaciente.index()
    return jsonify(json)
@app.route("/pacientes",methods=['POST'])
def crearPaciente():
    data = request.get_json()
    json=miControladorPaciente.create(data)
    return jsonify(json)
@app.route("/pacientes/<string:id>",methods=['GET'])
def getPaciente(id):
    json=miControladorPaciente.show(id)
    return jsonify(json)
@app.route("/pacientes/<string:id>",methods=['PUT'])
def modificarPaciente(id):
    data = request.get_json()
    json=miControladorPaciente.update(id,data)
    return jsonify(json)
@app.route("/pacientes/<string:id>",methods=['DELETE'])
def eliminarPaciente(id):
    json=miControladorPaciente.delete(id)
    return jsonify(json)

#CRUD usuarios
@app.route("/usuarios",methods=['GET'])
def getUsuarios():
    json=miControladorUsuario.index()
    return jsonify(json)
@app.route("/usuarios",methods=['POST'])
def crearUsuario():
    data = request.get_json()
    json=miControladorUsuario.create(data)
    return jsonify(json)
@app.route("/usuarios/<string:id>",methods=['GET'])
def getUsuario(id):
    json=miControladorUsuario.show(id)
    return jsonify(json)
@app.route("/usuarios/<string:id>",methods=['PUT'])
def modificarUsuario(id):
    data = request.get_json()
    json=miControladorUsuario.update(id,data)
    return jsonify(json)
@app.route("/usuarios/<string:id>",methods=['DELETE'])
def eliminarUsuario(id):
    json=miControladorUsuario.delete(id)
    return jsonify(json)

#CRUDPersonal
@app.route("/personal",methods=['GET'])
def getPersonales():
    json=miControladorPersonal.index()
    return jsonify(json)
@app.route("/personal",methods=['POST'])
def crearPersonal():
    data = request.get_json()
    json=miControladorPersonal.create(data)
    return jsonify(json)
@app.route("/personal/<string:id>",methods=['GET'])
def getPersonal(id):
    json=miControladorPersonal.show(id)
    return jsonify(json)
@app.route("/personal/<string:id>",methods=['PUT'])
def modificarPersonal(id):
    data = request.get_json()
    json=miControladorPersonal.update(id,data)
    return jsonify(json)
@app.route("/personal/<string:id>",methods=['DELETE'])
def eliminarPersonal(id):
    json=miControladorPersonal.delete(id)
    return jsonify(json)

#CRUD Documento
@app.route("/documentos",methods=['GET'])
def getDocumentos():
    json=miControladorDocumento.index()
    return jsonify(json)
@app.route("/documentos",methods=['POST'])
def crearDocumento():
    data = request.get_json()
    json=miControladorDocumento.create(data)
    return jsonify(json)
@app.route("/documentos/<string:id>",methods=['GET'])
def getDocumento(id):
    json=miControladorDocumento.show(id)
    return jsonify(json)
@app.route("/documentos/<string:id>",methods=['PUT'])
def modificarDocumento(id):
    data = request.get_json()
    json=miControladorDocumento.update(id,data)
    return jsonify(json)
@app.route("/documentos/<string:id>",methods=['DELETE'])
def eliminarDocumento(id):
    json=miControladorDocumento.delete(id)
    return jsonify(json)

#CRUD Consulta
@app.route("/consultas",methods=['GET'])
def getConsultas():
    json=miControladorConsulta.index()
    return jsonify(json)
@app.route("/consultas",methods=['POST'])
def crearConsulta():
    data = request.get_json()
    json=miControladorConsulta.create(data)
    return jsonify(json)
@app.route("/consultas/<string:id>",methods=['GET'])
def getConsulta(id):
    json=miControladorConsulta.show(id)
    return jsonify(json)
@app.route("/consultas/<string:id>",methods=['PUT'])
def modificarConsulta(id):
    data = request.get_json()
    json=miControladorConsulta.update(id,data)
    return jsonify(json)
@app.route("/consultas/<string:id>",methods=['DELETE'])
def eliminarConsulta(id):
    json=miControladorConsulta.delete(id)
    return jsonify(json)

#Asignar paciente a documento
@app.route("/documentos/<string:id_doc>/pacientes/<string:id>",methods=['PUT'])
def asignarPacienteaDocumento(id,id_doc):
    json=miControladorDocumento.asignarPaciente(id,id_doc)
    return jsonify(json)

#Consultar y listar documentos de un paciente
@app.route("/documentos/pacientes/<string:id>",methods=['GET'])
def DocumentosPaciente(id):
    json=miControladorDocumento.listarDocumentosPaciente(id)
    return jsonify(json)


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])