import asyncio
from asyncua import Client
import os
from dotenv import load_dotenv

load_dotenv()

async def listener_opc():
    URL = os.getenv('OPC_SERVER_URL')
    async with Client(url=URL) as client:
        print('Iniciado o Client Listener...')
        while True:
            try:
                # Obter os nodes e seus valores atuais
                temp_node = client.get_node("ns=2;i=2")
                press_node = client.get_node("ns=2;i=3")
                tempo_node = client.get_node("ns=2;i=4")

                temp = await temp_node.read_value()
                press = await press_node.read_value()
                tempo = await tempo_node.read_value()

                print(f'Lidos {temp}, {press}, {tempo}')
                await asyncio.sleep(1)
            except:
                print('Encerrando o Client Listener...')
                break

if __name__ == "__main__":
    asyncio.run(listener_opc())
