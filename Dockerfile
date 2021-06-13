FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8082
ENTRYPOINT [ "python" ]
CMD [ "server.py" ]
