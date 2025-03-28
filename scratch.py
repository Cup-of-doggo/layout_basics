from http.server import BaseHTTPRequestHandler, HTTPServer



hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open("sidebar_panel.html", "r", encoding="utf-8") as file:
            page = file.read()
        self.wfile.write(bytes(page, "utf-8"))

if __name__ == "__main__":

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:

        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
