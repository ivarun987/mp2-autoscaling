from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route("/", methods=["POST"])
def stress():
    subprocess.Popen(["python3", "stress_cpu.py"])
    return "CPU stress started", 200

@app.route("/", methods=["GET"])
def get_ip():
    ip = socket.gethostbyname(socket.gethostname())
    return f"Private IP: {ip}", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
