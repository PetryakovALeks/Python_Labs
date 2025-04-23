from http.server import HTTPServer, CGIHTTPRequestHandler

# Настройка сервера
server_address = ("", 8000)
handler = CGIHTTPRequestHandler
handler.cgi_directories = ["/"]

# Запуск сервера
httpd = HTTPServer(server_address, handler)
print("Сервер запущен на http://localhost:8000")
httpd.serve_forever()