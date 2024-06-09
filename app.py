from flask import Flask, jsonify, request, render_template
from chatsql import ChatWithSql

app = Flask(__name__)
obj = ChatWithSql("root","6e6b697565","localhost","bigyan_database")

app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['GET','POST'])
def send_message():
    if request.method == 'POST':
        user_query = request.form.get('query')
        
        if not user_query:
            return jsonify({'error': 'No query provided'}), 400
        
        message = obj.message(user_query)
        return jsonify({'message': message})
    
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
