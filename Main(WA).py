from flask import Flask, render_template, jsonify, json
import Util(WA)


app = Flask(__name__)

# 127.0.0.1:5000/api/random_number
@app.route('/', methods=['GET'])
def api_random_num():
	

# 127.0.0.1:5000/
@app.route('/')
def index():
   

if __name__ == '__main__':
    app.debug = True
    ip = '127.0.0.1'
    app.run(host=ip)
