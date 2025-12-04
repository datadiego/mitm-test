#!/bin/bash

echo "=== Instalando uv (gestor de paquetes Python) ==="
curl -LsSf https://astral.sh/uv/install.sh | sh

# Recargar el PATH para usar uv
export PATH="$HOME/.cargo/bin:$PATH"

echo ""
echo "=== Instalando dependencias del proyecto ==="
uv venv
source .venv/bin/activate
uv pip install mitmproxy requests

echo ""
echo "=== Configuración completada ==="
echo ""
echo "PASOS SIGUIENTES:"
echo "1. Edita client.py y cambia 'TU_API' por la URL de tu API"
echo "2. Activa el entorno virtual: source .venv/bin/activate"
echo "3. Ejecuta mitmproxy con: mitmdump -s client.py"
echo "4. Configura tu navegador para usar el proxy localhost:8080"