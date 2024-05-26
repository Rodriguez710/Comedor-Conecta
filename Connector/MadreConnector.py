import pymysql

class MadreConnector():
    def __init__(self):
        self.con = pymysql.connect(
            host = "localhost",
            user = "root", 
            password = "root",
            db = "ComedorConecta"
        )
        self.cursor = self.con.cursor()
        
    def insertar(self, id, nombre, nrehijo):
        sql = "insert into madre (id, nombre, nre-hijo) values (%s, %s, %s)".format(id, nombre, nrehijo)
        self.con.cursor().execute(sql, (id, nombre, nrehijo))
        self.con.commit()
       
    def devuelveTodos(self):
        try:
            sql = "SELECT id, nombre, nre-hijo FROM madre"
            self.cursor.execute(sql)
            madres = self.cursor.fetchall()
            return madres
        except Exception as e:
            print(f"Error al obtener madres: {str(e)}")
            return []
    
    def devuelvePorID(self, id):
        try:
            sql = "SELECT nombre, nre-hijo FROM madre where id = %s".format(id)
            self.cursor.execute(sql, (id))
            madre = self.cursor.fetchone()
            return madre
        except Exception as e:
            print(f"Error al obtener la madre: {str(e)}")
    
    def actualizarMadre(self, id, nombre, nrehijo):
        sql = "update madre set nombre = %s, nre-hijo = %s where id = %s".format(nombre, nrehijo)
        self.cursor.execute(sql, (nombre, nrehijo))
        self.con.commit()
    
    def borrarMadre(self, id):
        sql = "delete from madre where id = %s".format(id)
        self.cursor.execute(sql, (id))
        self.con.commit()
    
    def devuelvePorCurso(self, curso):
        try:
            sql = "SELECT id, nombre, nrehijo FROM madre WHERE curso = %s"
            self.cursor.execute(sql, (curso,))
            madres = self.cursor.fetchall()
            return madres
        except Exception as e:
            print(f"Error al obtener las madres del curso: {str(e)}")
            return []