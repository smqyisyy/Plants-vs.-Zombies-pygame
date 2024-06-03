# 服务端代码
import asyncio
import sys
import os
import json

# 解决使用相对导入的报错
top_path = "\\".join(os.path.abspath(__file__).split("\\")[:-2])
sys.path.append(top_path)
from share.const import *


async def handle_client(reader, writer):
    data = await reader.read(MAX_BYTES)
    msg = json.loads(data.decode())
    s2cmsg = {}
    if msg['type'] == C2S_ADD_FLOWER:
        s2cmsg["type"] = S2C_ADD_FLOWER
        s2cmsg["pos"] = msg["pos"]
    writer.write(json.dumps(s2cmsg).encode())
    await writer.drain()


async def main():
    server = await asyncio.start_server(handle_client, "0.0.0.0", SERVER_PORT)
    print(f"server is listening on 0.0.0.0:{SERVER_PORT}")
    async with server:
        await server.serve_forever()


asyncio.run(main())
