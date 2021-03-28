class Groups:
    def __init__(self, first, last, group):
        self.first = first
        self.last = last
        self.group = group
        self.person = first + ' ' + last + ', Group:' + group

    def student(self):
        print("Info: " + self.person)
        return self.person


student1 = Groups("Maksym", "Severyn", "It-12sp")
student2 = Groups("Bohdan", "Martyniv", "It-12sp")
student3 = Groups("Vasyl", "Horobec", "M-12")
student1.student()
student2.student()
student3.student()
