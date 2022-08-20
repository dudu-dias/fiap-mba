from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1>Olá FIAP! versão 2</h1>\nMBA! o/"

if __name__ == '__main__':
    # application.run()
    application.run(host='0.0.0.0',debug=True)
