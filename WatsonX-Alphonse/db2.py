from keys import *
import ibm_db
import requests
import json

'''
MODULE Containing the db2 class that will be used to be run DB2 SQL Commands
'''

class db2(object):

    def __init__(self):
        '''
        Construct Connection String that will connect to DB2 Instance
        '''

        #CONNECTION STRING TO THE DB2 INSTANCE
        self.conn_string = f"DATABASE={db2_name};HOSTNAME={db2_hostname};PORT={db2_port};PROTOCOL={db2_protocol};UID={db2_uid};PWD={db2_pwd};"

    '''
    PRIVATE FUNCTIONS
    '''

    def __connect(self):
        '''
        ATTEMPT TO ESTABLISH A CONNECTION TO THE DB2 INSTANCE ON THE IBM CLOUD
        '''

        try:
            self.conn = ibm_db.connect(self.conn_string, "", "")

        except:
            pass

    '''
    PUBLIC FUNCTIONS
    '''

    def create(self, table_name):
        '''
        Will Create a Table as need for DB2
        '''
        try:
            self.__connect()
            ibm_db.close(self.conn)
        except:
            pass

    def read(self):
        '''
        Will read data from a Table within DB2
        '''
        try:
            self.__connect()
            ibm_db.close(self.conn)
        except:
            pass

    def update(self):
        '''
        Will update data for a Table within DB2
        '''
        try:
            self.__connect()
            ibm_db.close(self.conn)
        except:
            pass

    def delete(self):
        '''
        Will delete data from a Table within DB2
        '''
        try:
            self.__connect()
            ibm_db.close(self.conn)
        except:
            pass