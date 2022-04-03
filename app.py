from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
from pymongo import MongoClient
import certifi
ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.tcpuz.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca )
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    nickname_receive = request.form['nickname_give']
    comment_receive = request.form['comment_give']

    doc = {
        'nickname' : nickname_receive,
        'comment' : comment_receive
    }

    db.cheering.insert_one(doc)
    return jsonify({'msg':'여러분의 따뜻한 응원이 등록되었어요!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    cheering_list = list(db.cheering.find({},{'_id':False}))
    return jsonify({'cheering': cheering_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)