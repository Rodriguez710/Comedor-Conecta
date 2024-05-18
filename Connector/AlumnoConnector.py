import pymysql
from PySide6.QtCore import Qt

class AlumnoConnector():
    def __init__(self):
        self.con = pymysql.connect(
            host = "localhost",
            user = "root", 
            password = "root",
            db = "ComedorConecta"
        )
        self.cursor = self.con.cursor()
        
    def insertar(self, nre, nombre, curso, clase, madre):
        sql = "insert into alumno (nre, nombre, curso, clase, madre) values (%s, %s, %s, %s, %s)".format(nre, nombre, curso, clase, madre)
        self.con.cursor().execute(sql, (nre, nombre, curso, clase, madre))
        self.con.commit()
       
    def devuelveTodos(self):
        try:
            sql = "SELECT nre, nombre, curso, clase, madre FROM alumno"
            self.cursor.execute(sql)
            alumnos = self.cursor.fetchall()
            return alumnos
        except Exception as e:
            print(f"Error al obtener alumnos: {str(e)}")
            return []
    
    def devuelvePorNRE(self, nre):
        try:
            sql = "SELECT nombre, curso, clase, madre FROM alumno where nre = %s".format(nre)
            self.cursor.execute(sql, (nre))
            alumno = self.cursor.fetchone()
            return alumno
        except Exception as e:
            print(f"Error al obtener el alumno: {str(e)}")
    
    def actualizarAlumno(self, nre, nombre, curso, clase, madre):
        sql = "update alumno set nombre = %s, curso = %s, clase = %s, madre = %s where nre = %s".format(nombre, curso, clase, madre, nre)
        self.cursor.execute(sql, (nombre, curso, clase, madre, nre))
        self.con.commit()

    def eliminar_alumnos_seleccionados(self, nres):
        if not nres:
            print("No se han seleccionado alumnos para eliminar.")
            return

        try:
            placeholders = ', '.join(['%s'] * len(nres))
            sql = f"DELETE FROM alumno WHERE nre IN ({placeholders})"
            
            connection = pymysql.connect(host='localhost', user='root', password='root', db='ComedorConecta')
            cursor = connection.cursor()
            cursor.execute(sql, nres)
            connection.commit()
            print(f"Se han eliminado {cursor.rowcount} alumnos.")
        except Exception as e:
            print(f"Error al eliminar alumnos: {str(e)}")
        finally:
            cursor.close()
            connection.close()
    
    def devuelvePorCurso(self, curso):
        try:
            sql = "SELECT nre, nombre, curso, clase, madre FROM alumno WHERE curso = %s"
            self.cursor.execute(sql, (curso,))
            alumnos = self.cursor.fetchall()
            return alumnos
        except Exception as e:
            print(f"Error al obtener los alumnos del curso: {str(e)}")
            return []
