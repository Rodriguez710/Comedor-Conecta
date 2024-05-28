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
        
    def insertar(self, nombre, nre_hijo, email, direccion):
        sql = "insert into madre (nombre, nre_hijo, email, direccion) values (%s, %s, %s, %s)".format(nombre, nre_hijo, email, direccion)
        self.con.cursor().execute(sql, (nombre, nre_hijo, email, direccion))
        self.con.commit()
       
    def devuelveTodos(self):
        try:
            sql = "SELECT id, nombre, nre_hijo, email, direccion FROM madre"
            self.cursor.execute(sql)
            madres = self.cursor.fetchall()
            return madres
        except Exception as e:
            print(f"Error al obtener madres: {str(e)}")
            return []
    
    def devuelvePorID(self, id):
        try:
            sql = "SELECT id, nombre, nre_hijo, email, direccion FROM madre where id = %s".format(id)
            self.cursor.execute(sql, (id))
            madre = self.cursor.fetchone()
            return madre
        except Exception as e:
            print(f"Error al obtener la madre: {str(e)}")
    
    def actualizarMadre(self, nombre, nre_hijo, email, direccion, id):
        sql = "update madre set nombre = %s, nre_hijo = %s, email = %s, direccion = %s where id = %s".format(nombre, nre_hijo, email, direccion, id)
        self.cursor.execute(sql, (nombre, nre_hijo, email, direccion, id))
        self.con.commit()
    
    def borrarMadre(self, id):
        sql = "delete from madre where id = %s".format(id)
        self.cursor.execute(sql, (id))
        self.con.commit()
        
    def devuelvePorID(self, id):
        try:
            sql = "SELECT id, nombre, nre_hijo, email, direccion FROM madre WHERE id = %s"
            self.cursor.execute(sql, (id,))
            madre = self.cursor.fetchone()
            return madre
        except Exception as e:
            print(f"Error al obtener las madres del curso: {str(e)}")
            return None
    
    def existeNRE(self, nre_hijo):
        sql = "SELECT COUNT(*) FROM madre WHERE nre_hijo = %s"
        self.cursor.execute(sql, (nre_hijo,))
        count = self.cursor.fetchone()[0]
        return count > 0
        
    def eliminar_padres_seleccionados(self, ids):
        if not ids:
            print("No se han seleccionado alumnos para eliminar.")
            return

        try:
            placeholders = ', '.join(['%s'] * len(ids))
            sql = f"DELETE FROM madre WHERE id IN ({placeholders})"
            
            self.cursor.execute(sql, ids)
            self.con.commit()
        except Exception as e:
            print(f"Error al eliminar alumnos: {str(e)}")
        finally:
            self.cursor.close()
            self.con.close()
            
    def devuelvePorNREHijo(self, nre):
        try:
            sql = "SELECT id, nombre, nre_hijo, email, direccion FROM madre WHERE nre_hijo = %s".format(nre)
            self.cursor.execute(sql, (nre))
            madre = self.cursor.fetchone()
            return madre
        except Exception as e:
            print(f"Error al obtener las madres del curso: {str(e)}")
            return None
