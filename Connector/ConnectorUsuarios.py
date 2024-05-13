import pymysql

class ConnectorUsuarios():
    def __init__(self):
        self.con = pymysql.connect(
            host = "localhost",
            user = "root", 
            password = "root",
            db = "ComedorConecta"
        )
        self.cursor = self.con.cursor()
        
    def insertar(self, username, email, passwd, centro, telefono):
        sql = "insert into users (username, email, passwd, centro, telefono) values (%s, %s, %s, %s, %s)".format(username, email, 
                passwd, centro, telefono)
        self.con.cursor().execute(sql, (username, email, passwd, centro, telefono))
        self.con.commit()
       
    def devuelveTodos(self):
        try:
            sql = "SELECT id, username, email, passwd, centro, telefono FROM users"
            self.cursor.execute(sql)
            usuarios = self.cursor.fetchall()
            return usuarios
        except Exception as e:
            print(f"Error al obtener usuarios: {str(e)}")
            return []
    
    def devuelvePorID(self, id):
        try:
            sql = "SELECT username, email, passwd, centro, telefono FROM users where id = %s".format(id)
            self.cursor.execute(sql, (id))
            usuario = self.cursor.fetchone()
            return usuario
        except Exception as e:
            print(f"Error al obtener usuario: {str(e)}")
    
    def actualizarUsuario(self, id, username, email, passwd, centro, telefono):
        sql = "update users set username = %s, email = %s, passwd = %s, centro = %s, telefono = %s where id = %s".format(username, email, 
                passwd, centro, telefono, id)
        self.cursor.execute(sql, (username, email, passwd, centro, telefono, id))
        self.con.commit()
    
    def borrarUsuario(self, id):
        sql = "delete from users where id = %s".format(id)
        self.cursor.execute(sql, (id))
        self.con.commit()
        
    def devuelvePorUsuario(self, identificador, tipo):
        try:
            if tipo == "username":
                sql = "SELECT * FROM users WHERE username = %s"
            elif tipo == "email":
                sql = "SELECT * FROM users WHERE email = %s"
            else:
                raise ValueError("Tipo de búsqueda no válido. Debe ser 'username' o 'email'.")

            self.cursor.execute(sql, (identificador,))
            usuario = self.cursor.fetchone()
            return usuario
        except Exception as e:
            print(f"Error al obtener usuario por {tipo}: {str(e)}")
            return None