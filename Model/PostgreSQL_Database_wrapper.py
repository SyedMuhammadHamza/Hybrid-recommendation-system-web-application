# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 22:17:49 2021

@author: Syed Muhammmad Hamza

"""
import pandas as pd 
import pyodbc
import sys
class PostgreSQLconnection(object):
        """
            A class used to to estblish connection to PostgreSQL database using odbc (Open Database Connectivity)
        
            ...
        
            Attributes
            ----------
            db_connection: Connection-Object
                    connection-Object
            cursor: Cursor-object
                    cursor object
            
            Methods
            -------
            establish_db_connection(DATABASE,UID,PWD,SERVER)
                    establish connection to postgreSQL database
            close_db_connecion()
                    close connection to database and cursor
            create_table(sqlstatement,Table)
                    create table in PostgreSQL database
            run_command(command)
                    execute commnad using curosr but never commit them in PostgreSQL database
            run_query(query)
                    execute query in PostgreSQL database
                   
            """
        
        def __init__(self, DATABASE,UID,PWD,SERVER):
                self.db_connection=self.establish_db_connection(DATABASE,UID,PWD,SERVER)
                self.cursor = self.db_connection.cursor()
        def close_db_connecion(self):
            """
            close connection to database and cursor
            
            Parameters
            ----------
            db_connection: Connection-Object
                    connection-Object
            
            cursor: Cursor-object
                    cursor object
            Returns
            -------
            None
            """
            self.cursor.close()
            self.db_connection.close()
        
        def establish_db_connection(self,DATABASE,UID,PWD,SERVER):
            """
            establish connection to database.
            
            Parameters
            ----------
            DATABASE: string_like 
                    valid database name
                    
            UID: string_like 
                    valid username
                    
            PWD: String_like 
                    valid password
                    
            Server: Sting_like 
                    valid Server Name/IP
        
            Returns
            -------
            connection: Connection-Object
                    Connection-Object
            
            """
            try:
                conn_str  = (
                    "DRIVER={PostgreSQL Unicode};"
                    "DATABASE="+DATABASE+";"
                    "UID="+UID+";"
                    "PWD="+PWD+";"
                    "SERVER="+SERVER+";"
                    "PORT=5432;"
                )
                connection = pyodbc.connect(conn_str)
                print("Successfully connected to database.")
                return connection
        
            except:
                # Couldn't connect to database. Print error message with more details
                sys.exit('Failed to connect to database:')
        def create_table(self,sqlstatement,Table):
            """
            create table in PostgreSQL database
            
            Parameters
            ----------
            sqlstatement: String_like
                    SQL query 
            db_connection: Connection-Object
                    connection-Object
            
            Table: String_like
                   table name
            Returns
            -------
            None
            """
            self.cursor.execute(sqlstatement)
            print("Table created successfully with name"+Table)
            # commit the changes
            self.db_connection.commit()
        def run_command(self,command):
            """
            execute commnad using curosr but never commit them in PostgreSQL database
            
            Parameters
            ----------
            command: String_like
                    SQL query 
            db_connection: Connection-Object
                    connection-Object
            
            Returns
            -------
            None
            """
            self.cursor.execute(command)
            print("successfull execution of command")
            self.db_connection.commit()
            return
        def run_query(self,query):
            """
            execute query in PostgreSQL database
            
            Parameters
            ----------
            query: String_like
                    SQL query 
            
            Returns
            -------
            dataframe: pandas_Datafram_object_like
            """
            return pd.read_sql_query(query,con=self.db_connection)
                        