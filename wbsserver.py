
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

    websockets.broadcast(CONNECTIONS, data)
  
async def main():
  start_server = websockets.serve(handler, "localhost", 8000)
  async with start_server:
    await asyncio.Future()

asyncio.run(main())
# problema verso il secondo client

