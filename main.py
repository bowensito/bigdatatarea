from funciones import *
from models import *

def menu_estudiantes():
    while True:
        print("\n--- MENÚ ESTUDIANTES ---")
        print("1. Crear Estudiante")
        print("2. Ver Estudiantes")
        print("3. Actualizar Estudiante")
        print("4. Eliminar Estudiante")
        print("5. Filtrar Estudiantes por Carrera")
        print("6. Filtrar Estudiantes por Año de Ingreso")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            rut = input("RUT: ")
            carrera = input("Carrera: ")
            año_ingreso = int(input("Año de ingreso: "))
            crear_estudiante(nombre, edad, rut, carrera, año_ingreso)

        elif opcion == "2":
            for estudiante in ver_estudiantes():
                print(estudiante)

        elif opcion == "3":
            rut = input("RUT del estudiante a actualizar: ")
            nuevos_datos = {
                "nombre": input("Nuevo nombre (dejar en blanco para no cambiar): "),
                "edad": input("Nueva edad (dejar en blanco para no cambiar): "),
                "carrera": input("Nueva carrera (dejar en blanco para no cambiar): "),
                "año_ingreso": input("Nuevo año de ingreso (dejar en blanco para no cambiar): ")
            }
            nuevos_datos = {k: v for k, v in nuevos_datos.items() if v}
            actualizar_estudiante(rut, nuevos_datos)

        elif opcion == "4":
            rut = input("RUT del estudiante a eliminar: ")
            eliminar_estudiante(rut)

        elif opcion == "5":
            carrera = input("Carrera a filtrar: ")
            for estudiante in filtrar_estudiantes_por_carrera(carrera):
                print(estudiante)

        elif opcion == "6":
            año_ingreso = int(input("Año de ingreso a filtrar: "))
            for estudiante in filtrar_estudiantes_por_año_ingreso(año_ingreso):
                print(estudiante)

        elif opcion == "0":
            break

        else:
            print("Opción no válida, por favor intente de nuevo.")


def menu_cursos():
    while True:
        print("\n--- MENÚ CURSOS ---")
        print("1. Crear Curso")
        print("2. Ver Cursos")
        print("3. Actualizar Curso")
        print("4. Eliminar Curso")
        print("5. Filtrar Cursos por Código")
        print("6. Filtrar Cursos por Nota Final")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            curso = input("Nombre del Curso: ")
            codigo_curso = input("Código del Curso: ")
            rut_estudiante = input("RUT del Estudiante: ")
            nota_final = float(input("Nota Final: "))
            crear_curso(curso, codigo_curso, rut_estudiante, nota_final)

        elif opcion == "2":
            for curso in ver_cursos():
                print(curso)

        elif opcion == "3":
            codigo_curso = input("Código del curso a actualizar: ")
            nuevos_datos = {
                "curso": input("Nuevo nombre del curso (dejar en blanco para no cambiar): "),
                "rut_estudiante": input("Nuevo RUT del estudiante (dejar en blanco para no cambiar): "),
                "nota_final": input("Nueva nota final (dejar en blanco para no cambiar): ")
            }
            nuevos_datos = {k: v for k, v in nuevos_datos.items() if v}
            actualizar_curso(codigo_curso, nuevos_datos)

        elif opcion == "4":
            codigo_curso = input("Código del curso a eliminar: ")
            eliminar_curso(codigo_curso)

        elif opcion == "5":
            codigo_curso = input("Código del curso a filtrar: ")
            for curso in filtrar_cursos_por_codigo(codigo_curso):
                print(curso)

        elif opcion == "6":
            nota_final = float(input("Nota final a filtrar: "))
            for curso in filtrar_cursos_por_nota_final(nota_final):
                print(curso)

        elif opcion == "0":
            break

        else:
            print("Opción no válida, por favor intente de nuevo.")


def menu_principal():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Gestionar Estudiantes")
        print("2. Gestionar Cursos")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_estudiantes()
        elif opcion == "2":
            menu_cursos()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")


def menu_inicial():
    while True:
        print("\n--- MENÚ INICIAL ---")
        print("1. Usar la colección de Estudiantes")
        print("2. Usar la colección de Cursos")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_estudiantes()
        elif opcion == "2":
            menu_cursos()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")


if __name__ == "__main__":
    menu_inicial()
