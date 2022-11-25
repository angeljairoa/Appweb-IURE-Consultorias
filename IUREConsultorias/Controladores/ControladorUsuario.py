from Repositorios.RepositorioUsuario import RepositorioUsuario
from Modelos.Usuario import Usuario

class ControladorUsuario():
    def __init__(self):
        self.repositorioUsuario = RepositorioUsuario()
    def index(self):
        return self.repositorioUsuario.findAll()
    def create(self,infoUsuario):
        nuevoUsuario=Usuario(infoUsuario)
        return self.repositorioUsuario.save(nuevoUsuario)
    def show(self,id):
        elUsuario=Usuario(self.repositorioUsuario.findById(id))
        return elUsuario.__dict__
    def update(self,id,infoUsuario):
        usuarioActual=Usuario(self.repositorioUsuario.findById(id))
        usuarioActual.id=infoUsuario["id"]
        usuarioActual.email = infoUsuario["email"]
        usuarioActual.password = infoUsuario["password"]
        usuarioActual.nombre = infoUsuario["nombre"]
        usuarioActual.apellido = infoUsuario["apellido"]
        usuarioActual.tipo_doc = infoUsuario["tipo_doc"]
        usuarioActual.num_doc = infoUsuario["num_doc"]

        return self.repositorioUsuario.save(usuarioActual)
    def delete(self,id):
        return self.repositorioUsuario.delete(id)


# class ControladorUsuario():
#     def __init__(self):
#         print("Creando ControladorUsuario")
#     def index(self):
#         print("Listar todos los Usuarios")
#         unUsuario = {
#             "id": "001",
#             "email": "jperez@gmail.com",
#             "password": "123456",
#             "nombre": "Juan",
#             "apellido": "Perez",
#             "tipo_doc" : "cc",
#             "num_doc":"45968978"
#         }
#         return [unUsuario]
#     def create(self,infoUsuario):
#         print("Crear un Usuario")
#         elUsuario = Usuario(infoUsuario)
#         return elUsuario.__dict__
#     def show(self,id):
#         print("Mostrando un Usuario con id ",id)
#         elUsuario = {
#             "id": "001",
#             "email": "jperez@gmail.com",
#             "password": "123456",
#             "nombre": "Juan",
#             "apellido": "Perez",
#             "tipo_doc": "cc",
#             "num_doc": "45968978"
#         }
#         return elUsuario
#     def update(self,id,infoUsuario):
#         print("Actualizando Usuario con id ",id)
#         elUsuario = Usuario(infoUsuario)
#         return elUsuario.__dict__
#     def delete(self,id):
#         print("Elimiando Usuario con id ",id)
#         return {"deleted_count": 1}