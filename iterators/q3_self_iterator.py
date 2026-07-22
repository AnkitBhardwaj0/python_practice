class my_iterator:
    def __init__(self,my_iteration):
        self.my_iteration=my_iteration
    def __iter__(self):
        return self
    def __next__(self):
        if self.my_iteration.start>=self.my_iteration.end:
            raise StopIteration
        current=self.my_iteration.start
        self.my_iteration.start+=1
        return current

class my_it:
    def __init__(self,start,end):
        self.start=start 
        self.end=end
    def __iter__(self):
        return my_iterator(self)
    
a=my_it(1,20)
for i in a:
    print(i)


   
