from flask import Flask

app = Flask(__name__)

@app.route('/')
def main() :
    return "2021104604 김지애"

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=8080)