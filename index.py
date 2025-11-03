# multiple jis class k pass gye usse uper wale chahie ho tb use hoga
# multi level jb hmme malum ho ki kitte classes chahie tb use hogaa

# a is inherited by b is inherited by c is inherited by d this is called multi level 
#multiple inheritance:
# class Teacher:
#     def show(self):
#         print("hello")
# class Professor:
#     def lecture(self):
#         print("hey")
# class Student(Teacher,Professor):
#     def visible(self):
#         print("bye")
# #multi level inhertance:
# class Teacher:
#     def show(self):
#         print("hello")
# class Professor:
#     def lecture(self):
#         print("hey")
# class Student(Professor):
#     def visible(self):
#         print("bye")
# class kid(Student):
#     def play(self):
#         print("play")

# obj1=Student()
# obj1.lecture()

# #hierarchial inheritance:
# # class Teacher:
# #     def show(self):
# #         print("hello")
# # class Professor(Teacher):
# #     def lecture(self):
# #         print("bye")
# # class Student(Teacher):
# #     def visible(self):
# #         print("hey")
# # class kid(Teacher):
# #     def play(self):
# #         print("play")

# # obj1 = Kid()

# # #hybrid inheritance:
# # allows to use both multiple and hierarchiL inheritance in same

# # class Employee:
# #     def dob(self,dob):
# #         self.dob=dob
#     def dob_now(self):
#         print("dob",self.dob)

# class newjoin(Employee):
#     def joiningdate(self,joiningdate):
#         self.joiningdate=joiningdate
#     def join_date(self):
#         print("joining date",self.joiningdate)

# class exp(newjoin):
#     def salary(self,salary):
#         self.salary=salary
#     def salary_x(self):
        # print("salary",self.salary)

# a=exp()
# a.salary("5000")
# a.dob("3/6/2007")
# a.joiningdate("4/5/2020")
# a.dob_now()
# a.join_date()
# a.salary_x()
# class CarParent:
#     def __init__(self,model,fuel,color):
#         self.model = model
#         self.fuel = fuel
#         self.color = color
#         print(self.model,self.fuel,self.color)
# class CarChild(CarParent):
#     def __init__(self,model,fuel,color,engine):
#         super().__init__(model,fuel,color)
#         self.model = model
#         self.fuel = fuel
#         self.color = color
#         self.engine = engine
#         print(self.model,self.fuel,self.color,self.engine)

# obj1 = CarChild("top",50,"red",1500)

#super keyword is used to call the method of parent class

# class University:
#     def __init__(self,attendance,marks):
#         self.attendance = attendance
#         self.marks = marks
#     def attendence(self):
#         return self.attendance
#     def marksget(self):
#         return self.marks
# class College(University):
#     def eligible(self):
#         if super().attendence()>=75:
#             return True
#         return False
#     def result(self):
#         if super().marksget()>=30:
#             return True
#         return False
# class School(College):
#     def total(self):
#         print(self.total)
    

# obj1 =School(50,500)



# class Animal:
#     def voice(self):
#         print("the voice of an animal")
# class Cat(Animal):
#     def voice(self):
#         print("meow")
# class Dog(Animal):
#     def voice(self):
#         print("woof")

# dog = Animal()
# dog.voice()
# #the voice function of animal class is getting called not the current one, by overriding the property.

# class employee:
#     def callparameter(self,a,b):
#         self.a=a
#         self.b=b
#         print((self.a+self.b)/2)
# class staff(employee):
#     def callparameter(self,a,b,c):
#         super().callparameter(a,b)
#         self.a=a
#         self.b=b
#         self.c=c
#         print((self.a+self.b+self.c)/3)
# class office(staff):
#     def callparameter(self,a,b,c,d):
#         super().callparameter(a,b,c)
#         self.a=a
#         self.b=b
#         self.c=c
#         self.d=d
#         print((self.a+self.b+self.c+self.d)/4)

# obj1=office()
# obj1.callparameter(10,20,30,40)

#operator overloading:
class car:
    def __init__(self,wheels):
        self.wheels=wheels
    def add(self,otherwheels):
        return self.wheels + otherwheels.wheels
car1=car(4)
car2=car(2)
print(car1.add(car2))