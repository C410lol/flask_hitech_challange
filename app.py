from flask import Flask, request

app = Flask(__name__);




#   DATAS
functionaries = [
    {
        "name": "Caio Gomes",
        "age": 18,
        "department": "Projetos",
        "function": "Assessor",
        "startDate": "01/04/2025" 
    },
    {
        "name": "Lucas Orlikoski",
        "age": 23,
        "department": "Presidência",
        "function": "Gerente",
        "startDate": "30/10/2024" 
    },
    {
        "name": "Gustavo Pellanda",
        "age": 19,
        "department": "Projetos",
        "function": "Gerente",
        "startDate": "30/10/2024" 
    },
    {
        "name": "Cecília Moreira",
        "age": 19,
        "department": "Negócios",
        "function": "Gerente",
        "startDate": "30/10/2024" 
    }
]




#   TEST ROUTES
@app.route("/")
def default():
    return "Hello, World!"

@app.route("/info", methods=['GET'])
def getRoute():
    data = {
        "name": "Caio Gomes",
        "age": 18,
        "department": "Projetos",
        "function": "Assessor",
        "startDate": "01/04/2025" 
    }
    return data


#   CRUD ROUTES
@app.route('/functionary', methods=['POST'])
def createFunctionary():
    data = request.json
    functionaries.append(data)
    return "Funcionário adicionado com sucesso!"

@app.route('/functionaries', methods=['GET'])
def getFunctionaries():
    return functionaries

@app.route('/functionary/<name>', methods=['GET'])
def getFunctionary(name):
    for functionary in functionaries:
        if functionary["name"] == name:
            return functionary;
    return "Funcionário não encontrado!"

@app.route('/functionary/<name>', methods=['PUT'])
def updateFunctionary(name):
    newName = request.args.get("newName")
    for functionary in functionaries:
        if functionary["name"] == name:
            functionary["name"] = newName
            return "Funcionário alterado com sucesso!"
    return "Funcionário não encontrado!"

@app.route('/functionary/<name>', methods=['DELETE'])
def deleteFunctionary(name):
    index = 0;
    for functionary in functionaries:
        if functionary["name"] == name:
            functionaries.pop(index)
            return "Funcionário removido com sucesso!"
        index += 1
    return "Funcionário não encontrado!"
    







if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)
