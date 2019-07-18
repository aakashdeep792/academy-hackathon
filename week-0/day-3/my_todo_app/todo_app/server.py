#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
#from werkzeug.utils import secure_filename
from flask import jsonify


#app=Flask(__name__)
#app = Flask(__name__, static_url_path="/static")
app = Flask(__name__, instance_relative_config=True)
#app.config["DEBUG"] = True
#DIR_PATH = os.path.dirname(os.path.realpath(__file__))

todos_store={}

todos_store['aakash']= ['study','coding','eating']

todos_store['raj']= ['music','dance','belle']
todos_store['shivang']= ['sing','read']
    
todos_store['ram']= ['code','code']
def init():
    print("flask initialised")

def todo_view(todos):
   # todo_list=[]
    todo_list=('my todos for today are' + '<br>')
    
    for todo in todos:
        todo_list+=(todo+ '<br>')
    todo_list+='LIST END HERE'
    return todo_list
   # return 'aaaa'

def select_todos(name):#model
    global todos_store
    return todos_store[name]

def add_todo_db(name,todo):#model
    todos_list=todos_store[name]
    todos_list.append(todo)
    todos_store[name]=todos_list
    my_todos=todos_store[name]
    return 

def add_todos_by_name(name,todo):#model
    #add data to db
    my_todos=add_todo_db(name,todo)
    return 

def get_todos_by_name(name):
    try:
        return select_todos(name)
    except:
        return None
   # render_template('404.html',name=name)


#def get_todos_by_name(name):
#    if name=='aakash':
#        return ['study','coding','eating']
#    elif name=='raj':
#        return ['music','dance','belle']

#    elif name=='shivang':
#        return ['sing','read']
#    elif name=='ram':
#       return ['code','code']
#    else:
#        return []


#http://127.0.0.1:5000/todos?name=aakash
@app.route('/todos')
def todos():#controller
    name=request.args.get('name')
    print('------------')
    print(name)
    print('------------')

    my_todos=get_todos_by_name(name)    
    
    #todo_view(my_todos)
    if my_todos == None:
        return render_template('404.html',name=name),404  
    else:
        return render_template('todo_view.html',todos=my_todos)
   # return 'aaa'


# wget http://127.0.0.1:5000/add_todos\?name\=raj\&todo\=play_cricket

@app.route('/add_todos')
def add_todos():
    name=request.args.get('name')
    todo=request.args.get('todo')
    add_todos_by_name(name,todo)
    return 'added sucessfully'

@app.route('/aakash')
def index():       
    my_todos=['study','coding','eating']
    return todo_view(my_todos)
   # return 'aaa'my_todos=['study','coding','eating']
    
    
if __name__ == "__main__":
    print(("* Loading  model and Flask starting server..."
        "please wait until server has fully started"))
    init()
    port = int(os.environ.get("PORT", 5000))
    app.run(threaded=True,host='127.0.0.1', port=port)



