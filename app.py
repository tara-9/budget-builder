from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
	data = request.get_json()
	print(data["gender"])
	return "hello world"

if __name__ == '__main__':
   app.run()