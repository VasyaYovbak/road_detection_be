from flask import Flask
from flask_cors import CORS

from media_controller import media_controller_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
CORS(app)
app.register_blueprint(media_controller_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
