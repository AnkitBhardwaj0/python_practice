class student:
    def __init__(self,name,std,roll):
        self.name=name
        self.std=std
        self.roll=roll

    def gen(self):
        yield self.name
        yield self.std
        yield self.roll

s=student("amit",12,2)
for i in s.gen():
    print(i)
