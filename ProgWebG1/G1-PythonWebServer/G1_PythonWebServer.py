from sys import argv, exit
from socket import socket, AF_INET, SOCK_STREAM
import _thread

def requestHandler (connection, client):
    print(f"Servidor conectado com {client}")

    request = connection.recv(4096).decode("utf-8")

    if not request: # Requisição vazia
        connection.close() # Fecha a conexão
        print(f"Conexão terminada com {client}")
        return

    request = request.splitlines()[0]

    requestMethod, filePath, protocol = request.split(" ")
    print(f"Method: {requestMethod}\tRequested File: {filePath}\tHTTPS Protocol: {protocol}")

    if (requestMethod != "GET"): # 501 - Not Implemented (só aceitamos requisições de método GET por enquanto)
        body = ""
        statusCode = "501"
        message = "Not Implemented"

    else:
        try:
            if filePath == "/": # Requisição sem caminho de arquivo
                with open("webPages/index.html", "rb") as f: # Abre index.html como página default
                    body = f.read()

            else: # Requisição com caminho de arquivo pedido
                if filePath.endswith(".html"):
                    with open("webPages/" + filePath[1:], "rb") as f:
                        body = f.read()

                elif filePath.endswith(".js"):
                    with open("javaScripts/" + filePath[1:], "rb") as f:
                        body = f.read()

                elif filePath.endswith(".jpg") or filePath.endswith(".png"):
                    with open("images/" + filePath[1:], "rb") as f:
                        body = f.read()

                elif filePath.endswith(".gif"):
                    with open("gifs/" + filePath[1:], "rb") as f:
                        body = f.read()
                else: 
                    raise FileNotFoundError
            
            # 200 - OK
            statusCode = "200"
            message = "OK"

        except FileNotFoundError: # 404 - Not Found
            with open("webPages/404.html", "rb") as f:
                    body = f.read()
            statusCode = "404"
            message = "Not Found"

        except Exception: # 500 - Internal Server Error (erro não especificado)
            body = ""
            statusCode = "500"
            message = "Internal Server Error"

    header = [f"Content-Length: {len(body)}", f"Connection: close"]

    connection.send((f"HTTP/1.1 {statusCode} {message}").encode("utf-8"))
    connection.send("".join(header).encode("utf-8"))
    connection.send("\n\n".encode("utf-8"))
    connection.send(body)

    print(message)

    connection.close()
    print(f"Conexão terminada com {client}")

    return

def main():
    if len(argv) == 3:
        hostName = argv[1] # Servidor sendo hospedado em endereço IP pedido pelo usuário
        serverPort = int(argv[2]) # Porta na qual o servidor está aberto
    else:
        hostName = "localhost" # Servidor sendo hospedado localmente
        serverPort = 8080 # Porta default 8080

    # Criar um TCP socket
    tcpSocket = socket(AF_INET, SOCK_STREAM)
    tcpSocket.bind((hostName, serverPort))
    tcpSocket.listen(2)

    print(f"Servidor aberto no endereço {hostName}:{serverPort}")

    while True: # Espera por conexão
        conn, client = tcpSocket.accept()
        _thread.start_new_thread(requestHandler, (conn, client)) # Cria nova thread para lidar com o socket

    tcpSocket.close()
    return


if __name__ == "__main__":        
    main()