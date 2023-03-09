from pythonosc import udp_client
from pythonosc.osc_message_builder import OscMessageBuilder
import time

IP = '192.168.2.105'
PORT = 5555

client = udp_client.UDPClient(IP, PORT)

color_list = [
              [int('e2', base=16), int('b2', base=16), int('c0', base=16)],
              [int('ff', base=16), int('f3', base=16), int('53', base=16)],
              [int('a5', base=16), int('d1', base=16), int('f4', base=16)],
              [int('e4', base=16), int('ad', base=16), int('6d', base=16)],
              [int('d6', base=16), int('85', base=16), int('b0', base=16)],
              [int('db', base=16), int('e1', base=16), int('59', base=16)],
              [int('7f', base=16), int('c2', base=16), int('ef', base=16)],
              [int('c4', base=16), int('a6', base=16), int('ca', base=16)],
              [int('ea', base=16), int('bf', base=16), int('4c', base=16)],
              [int('f9', base=16), int('e6', base=16), int('97', base=16)],
              [int('b3', base=16), int('d3', base=16), int('ac', base=16)],
              [int('ea', base=16), int('c7', base=16), int('cd', base=16)]
            ]

for color in color_list:
  msg = OscMessageBuilder(address='/color')
  msg.add_arg(color[0]) #R
  msg.add_arg(color[1]) #G
  msg.add_arg(color[2]) #B
  m = msg.build()
  print(f"send_osc (普通)[間隔:1s] address: /color, R: {color[0]}, G: {color[1]}, B: {color[2]}")
  client.send(m)

  time.sleep(1)

for color in color_list:
  msg = OscMessageBuilder(address='/color')
  msg.add_arg(color[0]) #R
  msg.add_arg(color[1]) #G
  msg.add_arg(color[2]) #B
  m = msg.build()
  print(f"send_osc (遅め？)[間隔:3s] address: /color, R: {color[0]}, G: {color[1]}, B: {color[2]}")
  client.send(m)

  time.sleep(3)

for color in color_list:
  msg = OscMessageBuilder(address='/color')
  msg.add_arg(color[0]) #R
  msg.add_arg(color[1]) #G
  msg.add_arg(color[2]) #B
  m = msg.build()
  print(f"send_osc (連続)[間隔:0.1s] address: /color, R: {color[0]}, G: {color[1]}, B: {color[2]}")
  client.send(m)

  time.sleep(0.1)

# for color in color_list:
#   msg = OscMessageBuilder(address='/color')
#   msg.add_arg(color[0]) #R
#   msg.add_arg(color[1]) #G
#   msg.add_arg(color[2]) #B
#   m = msg.build()
#   print(f"send_osc (連続)[間隔:nop] address: /color, R: {color[0]}, G: {color[1]}, B: {color[2]}")
#   client.send(m)

#   time.sleep(0.02)
  
print('end')