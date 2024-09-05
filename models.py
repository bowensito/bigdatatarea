from conexion import get_db

db = get_db()
estudiantes = db["Estudiantes"]
cursos = db["Cursos"]

def actualizar_datos_rut(rut, nuevos_datos):
    estudiantes.update_one({"rut": rut}, {"$set": nuevos_datos})
