FROM daocloud.io/library/python:latest
MAINTAINER Fisher "7wencaixu"

COPY start.py /
RUN pip install flask -i https://pypi.douban.com/simple
WORKDIR /

CMD python start.py