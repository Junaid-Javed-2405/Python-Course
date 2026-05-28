from random import randint

class train:
    def __init__(self,trainNo):
        self.trainNo=trainNo

    def getBook(self,fro,to):
        print(f"Your ticket from {fro} to {to} is booked on train number {self.trainNo} and your seat number is {randint(1,100)}")
    def cancelBook(self):
        print(f"Your ticket on train number {self.trainNo} is cancelled")

    def getStatus(self):
        print(f"Your ticket on train number {self.trainNo} is confirmed and your seat number is {randint(1,100)}")

    def getPrice(self):
        print(f"The price of your ticket on train number {self.trainNo} is {randint(500,1500)}")        



t1=train(12345)
t1.getBook("Karachi","Lahore")      
t1.getPrice()
t1.getStatus()
