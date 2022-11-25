from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Documento import Documento
from bson import ObjectId
class RepositorioDocumento(InterfaceRepositorio[Documento]):
    #pass
    #Consulta de documentos asociados a un paciente con id:id
    def getListadoDocumentosPaciente(self, id):
        theQuery = {"paciente.$id": ObjectId(id)}
        return self.query(theQuery)