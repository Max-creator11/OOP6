class Groups:
    numbers_of_students = 0
    stipend_percent = 1.07

    def __init__(self, first, last, group, stipend):
        self.first = first
        self.last = last
        self.group = group
        self.stipend = stipend
        self.person = first + ' ' + last + ', Group:' + \
            group
        Groups.numbers_of_students += 1

    def student(self):
        print("Info: " + self.person)
        return self.person

    def apply_raise(self):
        self.stipend = int(self.stipend * self.stipend_percent)
        return self.stipend


student1 = Groups("Maksym", "Severyn", "It-12sp", 1040)
student2 = Groups("Bohdan", "Martyniv", "It-12sp", 1040)
student3 = Groups("Vasyl", "Horobec", "M-12", 1040)
student1.apply_raise()
print(student1.stipend)
print(student2.stipend)
print(student3.stipend)
print(Groups.numbers_of_students)
student1.student()
student2.student()
student3.student()
