class student_iterator:
    def __init__(self,data):
        self.data = [data.name,data.std,data.roll,data.marks]
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        while True:
            try:
                current=self.data[self.index]
                self.index+=1
                return current
            except IndexError:
                raise StopIteration
            

class student:
    def __init__(self,name,std,roll,marks):
        self.name=name
        self.std=std
        self.roll=roll
        self.marks=marks
      
    def __iter__(self):
        return student_iterator(self)
    
obj=student("ankit",10,1,[90,95,99,98,97])
for i in obj:
    print(i)