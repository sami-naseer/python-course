class University:
    def __init__ (self,name,department):
        self.name=name
        self.department=department
        
class college(University):
    def __init__ (self,name,department,college_name):
        super().__init__(name,department)#super class mein hum parent class ke constructor ko call kr rahy hein
        self.college_name=college_name#yahan . operator ka use kr k hum parent class ke attribute ko access kr rahy hein

college1=college("UOK","Computer_Scirnce","JKIST")#yahan hum child class ka object bna rahy hein
print(college1.name)
print(college1.department)
print(college1.college_name)
