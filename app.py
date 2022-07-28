from flask import Flask, jsonify, request
from typing import Dict
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

class Student:
    def __init__(self,student_id,student_name) -> 'Student':
        self.id = student_id
        self.name = student_name
    def to_dict(self) -> Dict:
        return{
            "id" :  self.id,
            "name": self.name
        }

student_db = [
    Student("1","Tom"),
    Student("2","Jerry"),
]

@app.route("/students", methods={'GET','POST'})
def list_student():
    if request.method == "GET":
        return jsonify([student.to_dict() for student in student_db])
    if request.method == "POST":
        data = request.json
        for student in student_db:
            if student.id == data['id']:
                return {}, 409
        student = Student(data['id'],data['name'])
        student_db.append(student)
        return student.to_dict(), 201

@app.route("/students/<student_id>")
def get_student(student_id):
    print(student_id)
    for student in student_db:
        if student.id  == student_id:
            return student.to_dict()
    return "", 404

@app.route("/health")
def health():
    return {
        "version":"v1",
        "health" : "green"
    }