from flask import request
from flask.json import jsonify
from src import app
from src.models.students import StudentsModel

studentsModel = StudentsModel()

@app.route('/students', methods=['GET'])
def students():

   students = studentsModel.getStudents()
   print(students)
   arrayStudents = []

   for student in students:
      arrayStudents.append({'id':student[0],'iden':student[1],'name':student[2],'surname':student[3]}) 

   if len(students) == 0:
      return jsonify({'message':'No hay estudiantes registrados...'})
   #print(arrayStudents)
   return jsonify(arrayStudents)



@app.route('/students', methods=['POST'])
def insertStudent():
   
   iden = request.json['iden']
   name = request.json['name']
   surname = request.json['surname']
   try: 
      studentsModel.insertStudent(iden, name, surname)
   except:
      return jsonify({'message':'Error'})

   #print(iden, name, surname)
   return jsonify({'message':'Estudiante guardado correctamente...', 'student':{'iden': iden, 'name': name, 'surname':surname}})



@app.route('/students/<id>', methods=['PUT'])
def updateStudent(id):

   student = studentsModel.getStudent(id)

   iden = request.json['iden']
   name = request.json['name']
   surname = request.json['surname']

   if iden == '':
      iden = student[1]
   if name == '':
      name = student[2]
   if surname == '':
      surname = student[3]
      
   try:
      studentsModel.updateStudent(id,iden,name,surname)
   except:
      return jsonify({'message':'Error'})

   #print(student)
   #print(iden, name, surname)
   return jsonify({'message':'Estudiante editado correctamente...','student':{'iden': iden, 'name': name,'surname':surname}})

   

@app.route('/students/<id>', methods=['DELETE'])
def deleteStudent(id):

   studentsModel.deleteStudent(id)

   return jsonify({'message':'Estudiante eliminado correctamente...'})

