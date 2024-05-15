import pymysql

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
    
    def borrarAlumno(self, nre):
        sql = "delete from alumno where nre = %s".format(nre)
        self.cursor.execute(sql, (nre))
        self.con.commit()
    
    def devuelvePorCurso(self, curso):
        try:
            sql = "SELECT nre, nombre, curso, clase, madre FROM alumno WHERE curso = %s"
            self.cursor.execute(sql, (curso,))
            alumnos = self.cursor.fetchall()
            return alumnos
        except Exception as e:
            print(f"Error al obtener los alumnos del curso: {str(e)}")
            return []
