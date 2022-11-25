from Repositorios.RepositorioDocumento import RepositorioDocumento
from Repositorios.RepositorioPaciente import RepositorioPaciente
from Modelos.Paciente import Paciente
from Modelos.Documento import Documento

class ControladorDocumento():
    def __init__(self):
        self.repositorioDocumento = RepositorioDocumento()
        self.repositorioPaciente = RepositorioPaciente()
    def index(self):
        return self.repositorioDocumento.findAll()
    def create(self,infoDocumento):
        nuevoDocumento=Paciente(infoDocumento)
        return self.repositorioDocumento.save(nuevoDocumento)
    def show(self,id):
        elDocumento=Documento(self.repositorioDocumento.findById(id))
        return elDocumento.__dict__
    def update(self,id,infoDocumento):
        documentoActual=Documento(self.repositorioDocumento.findById(id))
        documentoActual.id_doc=infoDocumento["id_doc"]
        documentoActual.tipo_doc = infoDocumento["tipo_doc"]
        documentoActual.fecha_doc = infoDocumento["fecha_doc"]
        documentoActual.descripcion = infoDocumento["descripcion"]
        return self.repositorioPaciente.save(documentoActual)
    def delete(self,id):
        return self.repositorioPaciente.delete(id)

        """
        Relación paciente y documento
        """
    def asignarPaciente(self,id,id_doc):
        documentoActual = Documento(self.repositorioDocumento.findById(id_doc))
        pacienteActual =Paciente(self.repositorioPaciente.findById(id))
        documentoActual.paciente = pacienteActual
        return self.repositorioDocumento.save(documentoActual)

    "Obtener todos los documentos de un paciente"
    def listarDocumentosPaciente(self, id):
        return self.repositorioDocumento.getListadoDocumentosPaciente(id)


# class ControladorDocumento():
#     def __init__(self):
#         self.repositorioDocumento = RepositorioDocumento()
#         self.repositorioPaciente=RepositorioPaciente()
#         #print("Creando ControladorDocumento")
#
#
#     def index(self):
#         print("Listar todos los Documentos")
#         unDocumento = {
#             "id_doc": "001",
#             "tipo_doc" : "contrato_laboral",
#             "fecha_doc": "05/01/2021",
#             "descripcion" : "contrato prestacion de servicios No.3652 de la empresa ABC"
#         }
#         return [unDocumento]
#     def create(self,infoDocumento):
#         print("Crear un Documento")
#         elDocumento = Documento(infoDocumento)
#         return elDocumento.__dict__
#     def show(self,id):
#         print("Mostrando un Documento con id ",id)
#         elDocumento = {
#             "id": "001",
#             "tipo_doc": "contrato_laboral",
#             "fecha_doc": "05/01/2021",
#             "descripcion": "contrato prestacion de servicios No.3652 de la empresa ABC"
#         }
#         return elDocumento
#     def update(self,id,infoDocumento):
#         print("Actualizando Documento con id ",id)
#         elDocumento = Documento(infoDocumento)
#         return elDocumento.__dict__
#     def delete(self,id):
#         print("Elimiando Documento con id ",id)
#         return {"deleted_count": 1}