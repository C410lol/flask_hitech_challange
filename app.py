from flask import Flask

app = Flask(__name__);




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




if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)
