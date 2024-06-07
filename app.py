from flask import Flask, jsonify
from chatsql import ChatWithSql

app = Flask(__name__)
obj = ChatWithSql("root","6e6b697565","localhost","bigyan_database")

@app.route('/send_message', methods = ['GET'])
def send_message():
    message = obj.message('How many columns are there in the table?')
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(debug= True)