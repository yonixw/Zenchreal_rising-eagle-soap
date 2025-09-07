FROM python:2.7

WORKDIR /app/src
CMD [ "python", "server.py", "80" ]
EXPOSE 80

COPY . .

# Build and global install ZSI
RUN cd /app/src/ZSI-master \
    && python setup.py build \
    && python setup.py install


RUN pip install -r requirements.txt && python -m compileall .

RUN useradd -ms /bin/bash soap_server
USER soap_server