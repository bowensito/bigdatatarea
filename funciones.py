from models import *

## ESTUDIANTES
def crear_estudiante(nombre, edad, rut, carrera, año_ingreso):
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "rut": rut,
        "carrera": carrera,
        "año_ingreso": año_ingreso
    }
    estudiantes.insert_one(estudiante)

def ver_estudiantes():
    return list(estudiantes.find())

def actualizar_estudiante(rut, nuevos_datos):
    estudiantes.update_one({"rut": rut}, {"$set": nuevos_datos})

def eliminar_estudiante(rut):
    estudiantes.delete_one({"rut": rut})

def filtrar_estudiantes_por_carrera(carrera):
    return list(estudiantes.find({"carrera": carrera}))

def filtrar_estudiantes_por_año_ingreso(año_ingreso):
    return list(estudiantes.find({"año_ingreso": año_ingreso}))

## CURSOS
def crear_curso(curso, codigo_curso, rut_estudiante, nota_final):
    curso_doc = {
        "curso": curso,
        "codigo_curso": codigo_curso,
        "rut_estudiante": rut_estudiante,
        "nota_final": nota_final
    }
    cursos.insert_one(curso_doc)

def ver_cursos():
    return list(cursos.find())

def actualizar_curso(codigo_curso, nuevos_datos):
    cursos.update_one({"codigo_curso": codigo_curso}, {"$set": nuevos_datos})

def eliminar_curso(codigo_curso):
    cursos.delete_one({"codigo_curso": codigo_curso})

def filtrar_cursos_por_codigo(codigo_curso):
    return list(cursos.find({"codigo_curso": codigo_curso}))

def filtrar_cursos_por_nota_final(nota_min, nota_max):
    return list(cursos.find({"nota_final": {"$gte": nota_min, "$lte": nota_max}}))
