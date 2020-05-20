import mysql.connector, json

cnx = mysql.connector.connect(user='root', 
                              password='',
                              host='127.0.0.1',
                              database='sys')

cursor = cnx.cursor()

query = ('''SELECT CASE
	WHEN validade IS NULL THEN pmc
  WHEN promocao IS NULL THEN pmc
  WHEN validade >= curdate() THEN promocao
  WHEN validade < curdate() THEN IF(pmc IS NULL, promocao, pmc)
  END AS precoFinal, barra, quantidade FROM sys.estoque WHERE pmc IS NOT NULL AND quantidade>0''')

cursor.execute(query)

data = []

for (precoFinal, barra, quantidade) in cursor:
  data.append(dict([("ean", barra),("preco", precoFinal),("estoque", quantidade)]))

json_object = json.dumps(data, indent = 2) 

with open("sample.json", "w") as outfile: 
    outfile.write(json_object) 

cursor.close()

cnx.close()