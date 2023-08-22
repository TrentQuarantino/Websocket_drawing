#https://www.piesocket.com/blog/python-websocket
import asyncio
import websockets
import json

CONNECTIONS = set()

async def register(websocket):
  CONNECTIONS.add(websocket)
  print(CONNECTIONS.id)
  try:
    await websocket.wait_closed()
  finally:
    CONNECTIONS.remove(websocket)

# create handler for connection
async def handler(websocket):
  CONNECTIONS.add(websocket)
  print('client n: ',list(CONNECTIONS))
  while True:
    data = await websocket.recv()
    print( data)

    #reply = f"Data received as: {data}!"
    #reply = data
    websockets.broadcast(CONNECTIONS, data)
    #initialize = await websocket.recv()
    #initio = f"Riceit: {initialize}"
    #await websocket.send(initio)
  
async def main():
  start_server = websockets.serve(handler, "localhost", 8000)
  async with start_server:
    await asyncio.Future()
#asyncio.get_event_loop().run_until_complete(start_server)
#asyncio.get_event_loop().run_forever()
asyncio.run(main())

#https://github.com/Pithikos/python-websocket-server/blob/
# master/websocket_server/websocket_server.py
#https://www.tutorialspoint.com/html5/html5_websocket.htm
#https://stackoverflow.com/questions/62205620/asyncio-how-can-i-stop-and-
# restart-server-without-stopping-event-loop
#https://blog.teclado.com/changes-to-async-event-loops-in-python-3-10/