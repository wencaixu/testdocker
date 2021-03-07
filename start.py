from flask import Flask
import datetime

server=Flask(__name__)

@server.route('/time',methods=['post','get'])
def get_time():
    now=str(datetime.datetime.now())#把当前时间转换成字符串
    return "当前的时间是：%s"%now


server.run(port=8888)