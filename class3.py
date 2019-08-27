class computer():
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("configuration is ",self.cpu,self.ram)

c1=computer("i9",16)
c2=computer("ryzen 3",8)

c1.config()
c2.config()