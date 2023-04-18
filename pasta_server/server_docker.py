import asyncio
from asyncua import Server
import os
from dotenv import load_dotenv
import datetime
from urllib.parse import urlparse
import logging

load_dotenv()

async def main():
    server = Server()
    await server.init()
    # URL = os.getenv('OPC_SERVER_URL')
    URL = "opc.tcp://0.0.0.0:4842/freeopcua/server/"
    server.set_endpoint(URL)

    # Configurar o namespace do servidor
    uri = "http://examples.freeopcua.github.io"
    myNameSpace = await server.register_namespace(uri)
    objects = server.get_objects_node()

    # Configurar Objeto/Colecao
    params = await objects.add_object(myNameSpace, "Parameters")

    # Criar Variaveis
    temperatura = await params.add_variable(myNameSpace, "Temperatura", 20.0)
    pressao = await params.add_variable(myNameSpace, "Pressao", 1000.0)
    tempo_medicao = await params.add_variable(myNameSpace, "TempoDaMedicao", datetime.datetime.now())

    await temperatura.set_writable()
    await pressao.set_writable()
    await tempo_medicao.set_writable()

    # Iniciar o servidor
    await server.start()
    logging.warning(f"Servidor Iniciado na porta {urlparse(URL).port}")

    # Manter servidor em execução:
    try:
        while True:
            await asyncio.sleep(1)
    except:
        await server.stop()
        print(f"Servidor Encerrado na porta {urlparse(URL).port}")

if __name__ == "__main__":
    asyncio.run(main())
