from pythonosc import osc_server
from pythonosc.dispatcher import Dispatcher

def color_handler(unused_addr, red, green, blue):
    """ 値を受信したときに行う処理 """
    print(f'received color : ({red}, {green}, {blue})')

IP = '127.0.0.1'
PORT = 5555

# URLにコールバック関数を割り当てる
dispatcher = Dispatcher()
dispatcher.map('/color', color_handler)

# サーバを起動する
server = osc_server.ThreadingOSCUDPServer((IP, PORT), dispatcher)
print(f'Serving on {server.server_address}')
server.serve_forever()