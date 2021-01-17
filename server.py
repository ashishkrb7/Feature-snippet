from flask import Flask,request,jsonify
from src import search

app = Flask(__name__)

@app.route('/FeatureSnippet', methods = ['POST','GET'])
def main():
    """ Web service for getting Feature snippet from google """
    try:
        content = request.get_json()
        Result=jsonify({"FS":search(content.get("q"))}),200
    except:
        Result=jsonify({"FS" : ""}),404
    return(Result)

if __name__=="__main__":
    app.run(debug=True)