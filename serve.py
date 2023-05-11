from flask import Flask, request
import sys
import shlex, subprocess
import socket
app = Flask(__name__)


@app.route('/', methods = ['POST'])
def stress():
   subprocess.Popen([sys.executable, "stress_cpu.py"])
   return '', 204

@app.route('/', methods = ['GET'])
def get_ip():
   host = socket.gethostname()
   return host

if __name__ == '__main__':
   app.run(debug=True, host="0.0.0.0", port=port)
