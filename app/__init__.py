from flask import Flask

app = Flask(__name__)
app.config['TRAP_BAD_REQUESTS'] = True

from app.version1 import v1

app.register_blueprint(v1)

if __name__ == '__main__':
    app.run(debug=True)
