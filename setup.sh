#!/bin/bash

echo "=== Instalando uv (gestor de paquetes Python) ==="
curl -LsSf https://astral.sh/uv/install.sh | sh

# Recargar el PATH para usar uv
export PATH="$HOME/.cargo/bin:$PATH"

echo ""
echo "=== Instalando dependencias del proyecto ==="
uv venv
source .venv/bin/activate
uv pip install mitmproxy requests flask

source .venv/bin/activate
python3 server.py


# echo ""
# echo "=== Configuración completada ==="
# echo ""
# echo "PASOS SIGUIENTES:"
# echo "1. Activa el entorno virtual: source .venv/bin/activate"
# echo "2. En una terminal, ejecuta el servidor: python server.py"
# echo "3. En client.py, cambia 'TU_API' por http://localhost:5000"
# echo "4. En otra terminal, ejecuta el proxy: mitmdump -s client.py"
# echo "5. Configura tu navegador/aplicación para usar el proxy localhost:8080"
# echo "6. Visita http://localhost:5000 para ver el dashboard"