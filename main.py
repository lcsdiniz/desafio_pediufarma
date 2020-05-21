import mysql.connector, json

def dbConnection():
  connection = mysql.connector.connect(user='root', 
                                      password='',
                                      host='127.0.0.1',
                                      database='sys')
  cursor = connection.cursor()

  query = ('''SELECT CASE
    WHEN validade IS NULL THEN pmc
    WHEN promocao IS NULL THEN pmc
    WHEN validade >= curdate() THEN promocao
    WHEN validade < curdate() THEN IF(pmc IS NULL, promocao, pmc)
    END AS precoFinal, barra, quantidade FROM sys.estoque WHERE pmc IS NOT NULL AND quantidade>0''')

  cursor.execute(query)
  result = cursor.fetchall()
  cursor.close()
  connection.close()
  return result

def jsonParser(queryResult):
  data = []
  for (precoFinal, barra, quantidade) in queryResult:
    data.append(dict([("ean", barra),("preco", precoFinal),("estoque", quantidade)]))

  json_object = json.dumps(data, indent = 2)

  with open("sample.json", "w") as outfile: 
      outfile.write(json_object) 

queryResult = dbConnection()
jsonParser(queryResult)