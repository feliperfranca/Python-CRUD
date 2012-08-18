'''
Created on 17/08/2012

@author: felipe
'''

import MySQLdb

class ConnectionFactory:

    def __init__(self):
        pass
    
    @staticmethod
    def conexao(DB, Host, User, PassWd):
        return MySQLdb.Connection(db=DB, host=Host, user=User, passwd=PassWd)
        
        