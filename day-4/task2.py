##task 1
class student:
    def __init__(self):
        self.name=input("Enter the name")
        self.usn=input("Enter the usn")
        self.marks=[]
        for i in range(5):
            self.marks.append(int(input("enter the marks")))
        self.calculation(self.marks)
            
    def calculation(self,marks):
        self.cl=sum(marks)     
        self.percentage=(self.cl/500)*100
        if self.percentage>=90:
            self.grade="a"
        else:
            self.grade="b"    
            print(self.name,self.usn,self.cl,self.percentage,self.grade)   
s=[0]*5
for i in range(5):
    s[i]=student()
    