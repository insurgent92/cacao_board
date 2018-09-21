# -*- coding: utf-8 -*-
 
#---------------------------------
# pangpang2.py
#---------------------------------
 
import os
import csv
from flask import Flask, request, jsonify

app = Flask(__name__)

def getData():
    loss_text = ["epoch:","iteration","train_loss:","train_acc:","validation_loss:", "validation_acc:"]
    try:
        #f = open('/home/ubuntu/cacao_board/data.csv', 'r', encoding='utf-8')
        f = open('/home/ubuntu/cacao_board/data.csv', 'r')
        rdr = csv.reader(f)
        for line in rdr:
            pass
        f.close()
        epoch = loss_text[0] + line[0] + "\n"
        iteration = loss_text[1] + line[1] + "/" + line[2] + "\n"
        train_loss = loss_text[2] + line[3] + "\n"
        train_acc = loss_text[3] + line[4] + "\n"
        validation_loss = loss_text[4] + line[5] + "\n"
        validation_acc = loss_text[5] + line[6]

        loss_text = epoch + iteration + train_loss + train_acc + validation_loss + validation_acc
             
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
                "text": "팡팡이 명령어 목록!\n1. 도움말\n2. 안녕!\n3. 로스확인!\n4. 저기요~"
            }
        }

    elif u"로스보기" in content:
        dataSend = myfunc()

    else:
        dataSend = {
            "message": {
                "text": content
            }
        }

    return jsonify(dataSend)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 6000)