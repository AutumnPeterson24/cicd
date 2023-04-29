"""
Super Simple HTTP Server in Python .. not for production just for learning and fun
Author: Wolf Paulus (https://wolfpaulus.com)
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from time import asctime
from main import is_mult_of_10
import json

hostName = "0.0.0.0"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == "/health":
            status, content, content_type = 200, "OK", "text/html"
        elif self.path == "/" or self.path.startswith("/?number="):
            status = 200
            number = self.path.split("=")[1] if self.path.startswith("/?number=") else ""
            if self.headers.get('Accept') == 'application/json':
                content_type = "application/json"
                if number.isnumeric():
                    data_dict = {
                        "number": int(number),
                        "multiple_of_10": is_mult_of_10(int(number)),
                        "Version": 1,
                        "container_name": "erau01",
                        "message": f"multiple of 10 number checker Web-service"
                    }
                    status, content, content_type = 200, json.dumps(data_dict), "application/json"
                else:
                    status, content = 400, "Request cannot be made."
            else:
                content_type = "text/html"
                result = f"{number} is {'a multiple of 10' if is_mult_of_10(int(number)) else 'is not a multiple of 10'}." if number.isnumeric() else ""
                with open('./src/response.html', 'r') as f:
                    # read the html template and fill in the parameters: path, time and result
                    content = f.read().format(path=self.path, time=asctime(), result=result)
        else:
            status, content = 404, "Not Found"
        self.send_response(status)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")
