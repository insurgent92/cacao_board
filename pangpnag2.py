# -*- coding: utf-8 -*-
 
#---------------------------------
# pangpang2.py
#---------------------------------
 
import os
import csv
from flask import Flask, request, jsonify

app = Flask(__name__)


def getData():
    loss_text = 'loss : '
    try:
        #f = open('/home/ubuntu/cacao_board/data.csv', 'r', encoding='utf-8')
        f = open('/home/ubuntu/cacao_board/data.csv', 'r')
        rdr = csv.reader(f)
        for line in rdr:
            pass
        f.close()
        loss = line[1]
        loss_text = loss_text + loss
            
    except:
        loss_text = loss_text + "읽을 수 없당"

    return loss_text


def myfunc():

    text = getData()
    dataSend = {
            "message": {
                "text": text
            }
        }
    return dataSend
 
@app.route('/keyboard')
def  Keyboard():
    dataSend = {
        "type" : "buttons",
        "buttons" : ["팡팡이와 대화하기!(수정)", "도움말"]
    }
    return jsonify(dataSend)
 
@app.route('/message', methods=['POST'])
def Message():
    dataReceive = request.get_json()
    content = dataReceive['content']
    if content == u"팡팡이와 대화하기!":
        dataSend = {
            "message": {
                "text": "팡팡이 명령어 목록!\n1. 도움말\n2. 안녕!\n3. 로스확인!\n4. 저기요~"
            }
        }
    elif content == u"도움말":
        dataSend = {
            "message": {
                "text": "이제 곧 정식 버전이 출시될거야. 조금만 기다려~~~"
            }
        }
    elif u"안녕" in content:
        dataSend = {
            "message": {
                "text": "안녕~~ 반가워 ㅎㅎ"
            }
        }
    elif u"저기" in content:
        dataSend = myfunc()

    elif u"로스확인" in content:
        
        loss = "3"
        
        out_content = "현재 Loss는" + loss + "이야"
        
        dataSend = {
            "message":{
                "test": out_content
            }
        }

    else:
        dataSend = {
            "message": {
                "text": content
            }
        }
    return jsonify(dataSend)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 6000)