FROM  amancevice/pandas

COPY ./requirements.txt /tmp/

RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt

WORKDIR /scripts
ENTRYPOINT python run.py