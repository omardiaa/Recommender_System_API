from flask import Flask, request

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/get_recommendations',methods = ['POST'])
def get_recommendations():
    print(request.get_json())
    req = request.get_json() 
    return req["Test"]

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000)