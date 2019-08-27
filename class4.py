class RECORDS_student():

    def __init__(self,name,lastname,age,contact):
        self.name=name
        self.lastname=lastname
        self.age=age
        self.contact=contact
    def student_data(self):
        print("student data = ",'name:',self.name,'lastname:',self.lastname,'age:',self.age,'contact:',self.contact)


data=RECORDS_student('akhilesh','kushwah',20,9981806164)
data.student_data()