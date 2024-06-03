# 异步连接客户端代码
import asyncio
import json
from const import *
from share.const import *


class AsyncClient:
    def __init__(self, game, ip, port):
        self.ip = ip
        self.port = port
        self.game = game

    # 客户端向服务端发信息的函数
    async def c2s(self, message):
        reader, writer = await asyncio.open_connection(self.ip, self.port)
        data = json.dumps(message).encode('utf-8')
        # 数据异步写入缓冲区
        writer.write(data)
        # 等待数据写入完成
        await writer.drain()

        # 读取服务端数据
        message = await reader.read(MAX_BYTES)
        msg = json.loads(message.decode('utf-8'))
        # 如果服务端传入了要种花的消息类型,就实现客户端种花逻辑
        if msg['type'] == S2C_ADD_FLOWER:
            self.game.checkAddPlant(msg['pos'], SUNFlOWER_ID)
