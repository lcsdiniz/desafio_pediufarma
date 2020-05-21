from json_parser import jsonParser
from db_connector import databaseConnector

query = ('''SELECT CASE
  WHEN validade IS NULL THEN pmc
  WHEN promocao IS NULL THEN pmc
  WHEN validade >= curdate() THEN promocao
  WHEN validade < curdate() THEN IF(pmc IS NULL, promocao, pmc)
  END AS precoFinal, barra, quantidade FROM sys.estoque WHERE pmc IS NOT NULL AND quantidade>0''')

database = databaseConnector(user='root',password='',host='127.0.0.1',database='sys')
queryResult = databaseConnector.executeQuery(database,query)
jsonParser.listToJson(queryResult)
print("\nDone!")