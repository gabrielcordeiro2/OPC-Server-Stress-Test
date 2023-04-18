docker network create mynetwork

docker build -t server_image .
docker run --rm -d --network mynetwork -p 4842:4842 --name server_container server_image

*************************

docker build -t client_writer_image .
docker run --rm -d --network mynetwork -p 4840:4840 --name writer_container client_writer_image


Casos de uso:

- Servidor local  <-> Client local
- Servidor Docker <-> client local

- Servidor Docker <-> client Docker