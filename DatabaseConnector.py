"""
Author: B. Hedges
Date: 2024-06-11
Version: 1.0
Description: This program sets up data connections to various databases.
Specifically usefull for connecting to the postgres database used in this project
"""

import CredentialManager as CM
from urllib.parse import quote_plus
from sqlalchemy import create_engine, URL

class DBConnections:
    def __init__(self,RDBMS,Server=None,Database=None,UserName=None,Password=None,Encoding="utf8",Port=None,Echo=False,DSN=None,SQLLiteDatabasePath=""):
        """
        RDBMS: Type of database to connect to, available connection types:
          "MSSQL" = Microsoft SQL Server
          "MSSQL_AA" = Microsoft SQL Server active direcotry authentication
          "PostgreSQL" = PostgreSQL server
          "ORACLE" = Oracle Server
          "MySQL" = MySQL server
          "SQLite" = SQLite database
        Server: Server name; e.g., 128.0.0.1
        Database: Name of database to access
        UserName: UserName used to connect to the DB
        Password: password used to connect to the DB
        Encoding: Defaults to utf8, only used for postgreSQL
        Port: the Port number for the server, MSSQL_AA only
        DSN: data source name, Oracle only
        Echo: default to false, use true to see connections logged to the console
        SQLLiteDatabasePath: SQLite use path to create db connections, if not specified and SQLLite is called then a in memory database is used.
        """
        #####################Set Username and Password if empty#####################
        if not UserName and RDBMS != "SQLite":
            print("No user name provided")
            UserName,Password = CM.Remote_Creds()
        if RDBMS == "MSSQL":
            #####################Microsoft SQL Server Data Connection##########################
            dataConnection = quote_plus(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={Server};DATABASE={Database};UID={UserName},PWD={Password}")
            connectionString = "ssql+pyodbc:///?odbc_connect={}&autocommit=true".format(dataConnection)
            self.Engine = create_engine(connectionString,fast_executemany=True,echo=Echo)
            self.Connection = self.Engine.connect()
        if RDBMS == "MSSQL_AA":
            #####################Microsoft SQL Server Active Directory Data Connection#########
            dataConnection = URL.create("mssql+pyodbc",UserName,Password,Server,Port,Database,query={"driver":"ODBC Driver 18 for SQL Server","TrustServerCertificate":"yes","authentication":"ActiveDirectoryIntegrated",},)
            self.Engine = create_engine(connectionString,fast_executemany=True,echo=Echo)
            self.Connection = self.Engine.connect()
        if RDBMS == "PostgreSQL":
            #####################PostgreSQL Data Connection####################################
            dataConnection = f"postgresql+psycopg://{UserName}:{Password}@{Server}/{Database}"
            self.Engine = create_engine(dataConnection,client_encoding=Encoding,echo=Echo)
            self.Connection = self.Engine.connect().execution_options(stream_results=True)
        if RDBMS == "ORACLE":
            #####################Oracle Data Connection########################################
            dataConnection = f"oracle+cx_oracle://{UserName}:{Password}@{DSN}"
            self.Engine = create_engine(dataConnection,echo=Echo)
            self.Connection = self.Engine.connect().execution_options(stream_results=True)
        if RDBMS == "MySQL":
            #####################MySQL data Connection#########################################
            dataConnection = f"mysql+pymysql://{UserName}:{Password}@{Server}/{Database}"
            self.Engine = create_engine(dataConnection,isolation_level="AUTOCOMMIT",echo=Echo)
            self.Connection = self.Engine.connect().execution_options(stream_results=True)
        if RDBMS == "SQLite":
            #####################SQLite Data Connection########################################
            dataConnection = f"sqlite://{SQLLiteDatabasePath}"
            self.Engine = create_engine(connectionString,echo=Echo)
            self.Connection = self.Engine.connect().execution_options(stream_results=True)

def main():
    print("this only exists for testing purpopses numbnuts")

if __name__ == "__main__":
    main()
