from Repositorios.RepositorioPersonal import RepositorioPersonal
from Modelos.Personal import Personal

class ControladorPersonal():
    def __init__(self):
        self.repositorioPersonal = RepositorioPersonal()
    def index(self):
        return self.repositorioPersonal.findAll()
    def create(self,infoPersonal):
        nuevoPersonal=Personal(infoPersonal)
        return self.repositorioPersonal.save(nuevoPersonal)
    def show(self,id):
        elPersonal=Personal(self.repositorioPersonal.findById(id))
        return elPersonal.__dict__
    def update(self,id,infoPersonal):
        personalActual=Personal(self.repositorioPersonal.findById(id))
        personalActual.id=infoPersonal["id"]
        personalActual.rol = infoPersonal["rol"]
        return self.repositorioPersonal.save(personalActual)
    def delete(self,id):
        return self.repositorioPersonal.delete(id)

# class ControladorPersonal():
#     def __init__(self):
#         print("Creando ControladorPersonal")
#     def index(self):
#         print("Listar todos los Personales")
#         unPersonal = {
#             "id": "003",
#             "rol": "psicologo",
#         }
#         return [unPersonal]
#     def create(self,infoPersonal):
#         print("Crear un Personal")
#         elPersonal = Personal(infoPersonal)
#         return elPersonal.__dict__
#     def show(self,id):
#         print("Mostrando un Personal con id ",id)
#         elPersonal = {
#             "id": "003",
#             "rol": "psicologo",
#         }
#         return elPersonal
#     def update(self,id,infoPersonal):
#         print("Actualizando Personal con id ",id)
#         elPersonal = Personal(infoPersonal)
#         return elPersonal.__dict__
#     def delete(self,id):
#         print("Elimiando Personal con id ",id)
#         return {"deleted_count": 1}