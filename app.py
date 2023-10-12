import socket
import yfinance as yf

def finger_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 79))
    server_socket.listen(1)
    print('Finger server started.')

    while True:
        client_socket, client_address = server_socket.accept()
        print('Connection from:', client_address)

        data = client_socket.recv(1024).decode('utf-8')
        stock_symbol = data.strip()

        response = get_stock_info(stock_symbol.upper())

        client_socket.sendall(response.encode('utf-8'))
        client_socket.close()

def get_stock_info(stock_symbol):
    try:
        stock = yf.Ticker(stock_symbol)
        info = stock.info
        response = f"Symbol: {info['symbol']}\nName: {info['longName']}\nPrice: {info['regularMarketPrice']}\n"
    except:
        response = 'Stock not found'

    return response

finger_server()
