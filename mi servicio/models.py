from sqlalchemy import Column, Integer, String, DATETIME

class Rol:
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))


class Usuario:
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    apellido = Column(String(100))
    correo = Column(String(100))
    telefono = Column(String(20))


class Perfil:
    id = Column(Integer, primary_key=True)
    direccion = Column(String(200))


class Sesion:
    id = Column(Integer, primary_key=True)
    fecha_inicio = Column(DATETIME)
    fecha_fin = Column(DATETIME)
