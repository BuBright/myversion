
from flask import Flask

app = Flask()

@app.route('/hello')
def hello():
	return "hello word"
	

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=False, port=80)