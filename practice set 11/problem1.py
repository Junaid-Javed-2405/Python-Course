class twoDVector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __show__(self):
        print(f"X: {self.x}, Y: {self.y}")    


class threeDVector:
    def __init__(self,x,y,z):
        super().init__(x,y)
        self.z=z        

    def __show__(self):
        super().show()
        print(f"Z: {self.z}")


v1=twoDVector(2,3)
v1.__show__()
v2=threeDVector(2,3,4)
v2.__show__()           