from flask import Flask, jsonify
import jwt
app = Flask(__name__)
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/')
def hello():
    return jsonify({'tasks': tasks})

@app.route('/a')
def hellof():
    encoded = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')
    return jsonify(jwt.decode(encoded, 'secret', algorithms=['HS256']))
    
app.run()