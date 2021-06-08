from flask.json import jsonify
from src.config.db import DB
cursor = DB.cursor()
class StudentsModel():

    def getStudent(self, ide):

        cursor.execute('select * from students where id = ?',(ide,))
        student = cursor.fetchone()
    
        return student

    def getStudents(self):
        
        cursor.execute('select * from students')
        students = cursor.fetchall()
        
        return students

    def insertStudent(self, iden, name, surname):

        cursor.execute('insert into students(iden, name, surname) values(?,?,?)',(iden,name,surname,))
      

  

    def updateStudent(self, id, iden, name, surname):

        cursor.execute('update students set iden = ?, name = ?, surname = ? where id = ?',(iden,name,surname,id,))

    def deleteStudent(self, id):
        cursor.execute('delete from students where id = ?',(id,))
        
    

        

