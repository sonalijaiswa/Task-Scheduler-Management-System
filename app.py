from flask import Flask,request,render_template,redirect,url_for
from flask_pymongo import pyMongo
from bson.objectid  import ObjectId 
from scheduler import run_scheduled_tasks
import threading

app = Flask(__name__)

app.config = ['MONGO_URI']=('mongodb://localhost:27017/')
mongo = pyMongo(app)
tasks_collection = mongo.db.task

@app.route('/')
def index():
    tasks = tasks_collection.find()
    return render_template('index.html',tasks=tasks)

@app.route('/add',methods=['GET','POST'])
def add_task():
    if request.method == 'POST':
        task_name = request.form['task_name']
        description = request.form['description']
        schedule_time = request.form['schedule_time']
        new_task = {
            "name"
        }





@app.route('/edit/<task_id>',methods=['GET','POST'])
def edit_task(task_id):
    task = tasks_collection.find_one({"_id": ObjectId(task_id)})
    if request.method == 'POST':
        updated_task = {
            "name": request.form['task_name'],
            "description": request.form['description'],
            "schedule_time": request.form['schedule_time'],

        }
        tasks_collection.update_one({"_id":ObjectId(task_id)},)