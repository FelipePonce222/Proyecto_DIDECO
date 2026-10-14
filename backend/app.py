from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite que el frontend consulte a la API

@app.route('/')
def home():
    return jsonify({
        "status": "OK",
        "mensaje": "¡Servidor DIDECO funcionando impecable!",
        "proyecto": "Sistema de Monitoreo La Granja"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)