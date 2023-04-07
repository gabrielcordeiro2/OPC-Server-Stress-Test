import asyncio
from asyncua import Client
import os
from dotenv import load_dotenv
import datetime
import random

load_dotenv()

async def writer_opc():
    URL = os.getenv('OPC_SERVER_URL')
    async with Client(url=URL) as client:
        print('Iniciado o Client Writer...')
        while True:
            try:
                # Obter os nodes e seus valores atuais
                temp_node = client.get_node("ns=2;i=2")
                press_node = client.get_node("ns=2;i=3")
                tempo_node = client.get_node("ns=2;i=4")

                temp = round(random.uniform(15.0, 50.0), 2)
                press = round(random.uniform(850.0, 1050.0), 2)
                tempo = datetime.datetime.now()

                await temp_node.write_value(temp)
                await press_node.write_value(press)
                await tempo_node.write_value(tempo)

                print(f'Escritos {temp}, {press}, {tempo}')
                await asyncio.sleep(1)
            except:
                print('Encerrando o Client Writer...')
                break

if __name__ == "__main__":
    asyncio.run(writer_opc())
