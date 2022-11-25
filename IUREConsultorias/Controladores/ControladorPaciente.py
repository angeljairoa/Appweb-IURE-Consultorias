from Repositorios.RepositorioPaciente import RepositorioPaciente
from Modelos.Paciente import Paciente

class ControladorPaciente():
    def __init__(self):
        self.repositorioPaciente = RepositorioPaciente()
    def index(self):
        return self.repositorioPaciente.findAll()
    def create(self,infoPaciente):
        nuevoPaciente=Paciente(infoPaciente)
        return self.repositorioPaciente.save(nuevoPaciente)
    def show(self,id):
        elPaciente=Paciente(self.repositorioPaciente.findById(id))
        return elPaciente.__dict__
    def update(self,id,infoPaciente):
        pacienteActual=Paciente(self.repositorioPaciente.findById(id))
        pacienteActual.id=infoPaciente["id"]
        pacienteActual.sexo = infoPaciente["sexo"]
        pacienteActual.telefono = infoPaciente["telefono"]
        pacienteActual.direccion = infoPaciente["direccion"]
        pacienteActual.desc_caso = infoPaciente["desc_caso"]
        pacienteActual.mode_contact = infoPaciente["mode_contact"]
        pacienteActual.id_doc = infoPaciente["id_doc"]
        pacienteActual.tipo_consulta = infoPaciente["tipo_consulta"]

        return self.repositorioPaciente.save(pacienteActual)
    def delete(self,id):
        return self.repositorioPaciente.delete(id)


# class ControladorPaciente():
#     def __init__(self):
#         print("Creando ControladorPaciente")
#     def index(self):
#         print("Listar todos los Pacientes")
#         unPaciente = {
#             "id": "001",
#             "sexo": "M",
#             "telefono": "6697852",
#             "direccion": "calle 98 #98-30",
#             "desc_caso": "denuncia laboral",
#             "mode_contact": "telefono",
#             " id_doc":"001",
#             "tipo_consulta":"juridica"
#         }
#         return [unPaciente]
#     def create(self,infoPaciente):
#         print("Crear un Paciente")
#         elPaciente = Paciente(infoPaciente)
#         return elPaciente.__dict__
#     def show(self,id):
#         print("Mostrando un Paciente con id ",id)
#         elPaciente = {
#             "id": "001",
#             "sexo": "M",
#             "telefono": "6697852",
#             "direccion": "calle 98 #98-30",
#             "desc_caso": "denuncia laboral",
#             "mode_contact": "telefono",
#             " id_doc": "001",
#             "tipo_consulta": "juridica"
#         }
#         return elPaciente
#     def update(self,id,infoPaciente):
#         print("Actualizando Paciente con id ",id)
#         elPaciente = Paciente(infoPaciente)
#         return elPaciente.__dict__
#     def delete(self,id):
#         print("Elimiando Paciente con id ",id)
#         return {"deleted_count": 1}