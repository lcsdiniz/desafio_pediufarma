import json

class jsonParser:
  def listToJson(queryResult):
    data = []
    for (precoFinal, barra, quantidade) in queryResult:
      data.append(dict([("ean", barra),("preco", precoFinal),("estoque", quantidade)]))

    json_object = json.dumps(data, indent = 2)

    with open("sample4.json", "w") as outfile: 
        outfile.write(json_object) 