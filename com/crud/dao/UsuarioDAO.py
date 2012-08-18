'''
Created on 17/08/2012

@author: felipe
'''
from com.crud.dao.banco.ConnectionFactory import ConnectionFactory
import MySQLdb
from com.crud.model.Usuario import Usuario

class UsuarioDAO:

    def __init__(self):
        self.db = 'crud_schema'
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'admin'
       
        
    def conectar(self):
        try:
            self.conn = ConnectionFactory.conexao(self.db, self.host, self.user, self.password)
            self.cur = self.conn.cursor()
            print 'Conectado'
        except (MySQLdb.OperationalError, MySQLdb.ProgrammingError), e:
            raise e


    def desconectar(self):
        try:
            self.cur.close()
            self.conn.close()
            print 'Desconectado'
        except (MySQLdb.OperationalError, MySQLdb.ProgrammingError), e:
            raise e

        
    def create(self, user):
        self.conectar()
        try:
            self.cur.execute("INSERT INTO python(name, cpf, phone, email) VALUES('" \
                             + str(user.nome) + "', '" \
                             + str(user.cpf) + "', '" \
                             + str(user.telefone) + "', '"  \
                             + str(user.email) + "')")
            self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            self.desconectar()

    
    def read(self, userId):
        self.conectar()
        try:
            self.cur.execute("SELECT * FROM python WHERE id = " + str(userId))
            row = self.cur.fetchone()
            return Usuario(int(row[0]), row[1], row[2], row[3], row[4])
        except:
            self.conn.rollback()
        finally:
            self.desconectar()
            
    
    def readAll(self):
        self.conectar()
        users = list()
        try:
            self.cur.execute("SELECT * FROM python")
            rows = self.cur.fetchall()
            for row in rows:
                users.append(Usuario(int(row[0]), row[1], row[2], row[3], row[4]))
            return users     
        except:
            self.conn.rollback()
        finally:
            self.desconectar()
        
        
    def update(self, user):
        self.conectar()
        try:
            self.cur.execute("UPDATE python SET name = '" + str(user.nome) + "', " \
                             + "cpf='" + str(user.cpf) + "', " \
                             + "phone='" + str(user.telefone) + "', "  \
                             + "email='"  + str(user.email) + "' " \
                             + "WHERE id=" + str(user.userId))
            self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            self.desconectar()
    
    
    def delete(self, userId):
        self.conectar()
        try:
            self.cur.execute("DELETE FROM python WHERE id=" + str(userId))
            self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            self.desconectar()
