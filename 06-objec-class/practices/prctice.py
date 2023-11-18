class studentInfo:
    def __init__(self, student_id, student_name, class_name):
        self.Student_Id = student_id
        self.Student_Name = student_name
        self.Class_Name = class_name

    def show(self):
        print(self.Student_Id, self.Student_Name, self.Class_Name)

    def update(self, student_name, class_name):
        self.Student_Name = student_name
        self.Class_Name = class_name


studentObject = studentInfo(87, "Jakir", 11)
studentObject.show()
studentObject.update("Jasim", 12)
studentObject.show()
