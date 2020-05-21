import mysql.connector

class databaseConnector:
  def __init__(self,user,password,host,database):
    self.connection = mysql.connector.connect(user=user, password=password, host=host, database=database)
    
  def executeQuery(self,query):
    cursor = self.connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    self.connection.close()
    return result