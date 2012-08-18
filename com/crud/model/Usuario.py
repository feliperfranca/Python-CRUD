'''
Created on 17/08/2012

@author: felipe
'''

class Usuario:
    
    def __init__(self, userId=None, nome=None, cpf=None, telefone=None, email=None):
        self.userId = userId
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email

    
    @property
    def userId(self):
        return self.__userId

    @userId.setter
    def userId(self, value):
        self.__userId = value


    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value


    @property
    def cpf(self):
        return self.__cpf


    @cpf.setter
    def cpf(self, value):
        self.__cpf = value


    @property
    def telefone(self):
        return self.__telefone


    @telefone.setter
    def telefone(self, value):
        self.__telefone = value


    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    
    def __str__(self):
        stringUser = 'Usuario [id=' + str(self.userId) + ', nome=' + str(self.nome) + ', cpf=' + str(self.cpf) + ', telefone=' + str(self.telefone) + ', email=' + str(self.email) + ']'
        return stringUser
