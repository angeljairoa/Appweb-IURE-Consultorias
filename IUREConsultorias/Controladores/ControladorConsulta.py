from Repositorios.RepositorioConsulta import RepositorioConsulta
from Modelos.Consulta import Consulta

class ControladorConsulta():
    def __init__(self):
        self.repositorioConsulta = RepositorioConsulta()
    def index(self):
        return self.repositorioConsulta.findAll()
    def create(self,infoConsulta):
        nuevoConsulta=Consulta(infoConsulta)
        return self.repositorioConsulta.save(nuevoConsulta)
    def show(self,id):
        laConsulta=Consulta(self.repositorioConsulta.findById(id))
        return laConsulta.__dict__
    def update(self,id,infoConsulta):
        consultaActual=Consulta(self.repositorioConsulta.findById(id))
        consultaActual.id_consulta=infoConsulta["id_consulta"]
        consultaActual.tipo_consulta = infoConsulta["tipo_consulta"]
        consultaActual.fecha_consulta = infoConsulta["fecha_consulta"]
        consultaActual.concepto = infoConsulta["concepto"]

        return self.repositorioConsulta.save(consultaActual)
    def delete(self,id):
        return self.repositorioConsulta.delete(id)


# class ControladorConsulta():
#     def __init__(self):
#         print("Creando ControladorConsulta")
#     def index(self):
#         print("Listar todas las Consultas")
#         unaConsulta = {
#             "id_consulta": "001",
#             "tipo_consulta": "juridica",
#             "fecha_consulta": "15/11/2022",
#             "concepto":"denuncia laboral instaurada por Juan Perez"
#         }
#         return [unaConsulta]
#     def create(self,infoConsulta):
#         print("Crear una Consulta")
#         laConsulta = Consulta(infoConsulta)
#         return laConsulta.__dict__
#     def show(self,id):
#         print("Mostrando una Consulta con id ",id)
#         laConsulta = {
#             "id_consulta": "001",
#             "tipo_consulta": "juridica",
#             "fecha_consulta": "15/11/2022",
#             "concepto": "denuncia laboral instaurada por Juan Perez"
#         }
#         return laConsulta
#     def update(self,id,infoConsulta):
#         print("Actualizando Consulta con id ",id)
#         laConsulta = Consulta(infoConsulta)
#         return laConsulta.__dict__
#     def delete(self,id):
#         print("Elimiando Consulta con id ",id)
#         return {"deleted_count": 1}