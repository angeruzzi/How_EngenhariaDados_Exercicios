#https://hub.docker.com/
FROM httpd
COPY ./web/ /usr/local/apache2/htdocs/
EXPOSE 80

#Comandos no terminal
#docker build -t web_apache .       : monta o ambiente docker
#docker image ls                    : Ver as imagens baixadas
#docker run -p 80:80 web_apache     : para rodar o servidor web
#docker run -d -p 80:80 web_apache  : Com o atributo -d o servidor fica desacoplado do terminal
#docker ps                          : Ver os Containers ativos
#docker stop CONTAINER_ID           : Para o container