class employee:
    salary=89000
    increment=2

    @property
    def salary_after_increment(self):   
        return self.salary*self.increment
    
    @salary_after_increment.setter
    def salary_after_increment(self,salary):
        self.salary=salary      
    

e=employee()
print(e.salary_after_increment) # this is a property method and it will return the salary after increment

e.salary_after_increment=90000 # this will set the salary to 90000 and then we can calculate the salary after increment using the property method
print(e.salary_after_increment) # this will return the salary after increment which is 180000   