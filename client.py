from mitmproxy import http
import requests
import json

API_URL = "http://TU_API/collect"

def request(flow: http.HTTPFlow):
    data = {
        "url": flow.request.pretty_url,
        "method": flow.request.method,
        "headers": dict(flow.request.headers),
        "body": flow.request.text if flow.request.text else None
    }

    try:
        requests.post(API_URL, json=data, timeout=2)
    except Exception as e:
        print("Error sending to API:", e)
