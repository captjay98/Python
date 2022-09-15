    def tell(self):
        return ("My grade is ", self.marks)

    def __repr__(self):
        return 'Student("{}", "{}", {})'.format(self.fname, self.lname, self.age)
    

    def tell(self):
            print("My current rating is ", self.rating)

    def __repr__(self):
        return 'Teacher("{}", "{}", {})'.format(self.fname, self.lname, self.age)

    
        if emps is None:
            self.emps = []
        else:
            self.emps = emps

    def addemps(self, emp):
        if emp not in self.emps:
            self.emps.append(emp)
            print(f"{emp} has been added")

    def rememp(self, emp):
        if emp in self.emps:
            self.emps.remove(emp)
            print(f"{emp} has been removed")

    def printemps(self):
        for emp in self.emps:
            print("-->", emp.fullname())
        print(self.emps)

    def __repr__(self):
        return 'Inspector("{}", "{}", {})'.format(self.fname, self.lname, self.age)


jam = Student("Jamal", "Ibrahim", 50, 99)

Teacher5 = Teacher("Jay", "Ibro", 60, 77)

Teacher6 = Teacher("Jam", "Ibra", 88, 50)

"""teac = Teacher("kal" "Abs", 88, 50)"""

sule = Inspector("Sule", "Sule", 55, [Teacher6])

"""print(jam.fullname())"""
"""
sule.addemps(Teacher5)
sule.printemps()
sule.rememp(Teacher6)
sule.printemps()"""

print(repr(sule))
