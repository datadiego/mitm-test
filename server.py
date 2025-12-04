from flask import Flask, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)

# Lista para almacenar las peticiones capturadas
captured_requests = []

@app.route('/collect', methods=['POST'])
def collect():
    """Endpoint que recibe los datos capturados por el proxy"""
    try:
        data = request.get_json()
        
        # Añadir timestamp
        data['timestamp'] = datetime.now().isoformat()
        
        # Guardar la petición
        captured_requests.append(data)
        
        # Mostrar en consola
        print(f"\n{'='*80}")
        print(f"[{data['timestamp']}] {data['method']} {data['url']}")
        print(f"Headers: {json.dumps(data['headers'], indent=2)}")
        if data.get('body'):
            print(f"Body: {data['body'][:200]}...")  # Primeros 200 caracteres
        print(f"{'='*80}\n")
        
        return jsonify({"status": "success", "message": "Data received"}), 200
    
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/requests', methods=['GET'])
def get_requests():
    """Endpoint para consultar las peticiones capturadas"""
    return jsonify({
        "total": len(captured_requests),
        "requests": captured_requests
    })

@app.route('/clear', methods=['POST'])
def clear_requests():
    """Endpoint para limpiar las peticiones capturadas"""
    captured_requests.clear()
    return jsonify({"status": "success", "message": "Requests cleared"})

@app.route('/', methods=['GET'])
def index():
    """Página de inicio con estadísticas"""
    return f"""
    <html>
    <head><title>MITM Collector</title></head>
    <body>
        <h1>MITM Request Collector</h1>
        <p>Total requests captured: {len(captured_requests)}</p>
        <ul>
            <li><a href="/requests">View all requests (JSON)</a></li>
            <li>POST to /clear to clear all requests</li>
        </ul>
    </body>
    </html>
    """

if __name__ == '__main__':
    print("="*80)
    print("MITM Request Collector Server")
    print("="*80)
    print("Server running on http://0.0.0.0:5000")
    print("Endpoints:")
    print("  - POST /collect    : Receive captured requests")
    print("  - GET  /requests   : View all captured requests")
    print("  - POST /clear      : Clear all captured requests")
    print("  - GET  /           : Dashboard")
    print("="*80)
    print()
    
    app.run(host='0.0.0.0', port=5000, debug=True)
