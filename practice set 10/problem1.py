class programer:
    company="Microsoft"
    name="" 
    salary=0
    department=""

    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department

    def get_details(self):
        print(f"Name: {self.name}\nSalary: {self.salary}\nDepartment: {self.department}")    



p1=programer("JJ",50000,"CS")
p1.get_details()

p2=programer("Ali",60000,"IT")
p2.get_details()