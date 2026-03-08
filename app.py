from flask import Flask, render_template, request
import socket

app = Flask(__name__)

def scan_ports(host):
    open_ports = []

    for port in range(1,1024):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)

        result = sock.connect_ex((host, port))

        if result == 0:
            open_ports.append(port)

        sock.close()
    if len(open_ports)==0:
        open_ports.append("no open ports found")
         
    return open_ports
      

@app.route("/", methods=["GET","POST"])
def home():

    results = []

    if request.method == "POST":
        target = request.form["target"]
        results = scan_ports(target)

    return render_template("home.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)