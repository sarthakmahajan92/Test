# # numbers = [1, 2, 3, 4, 5]

# # squares = [x**3 for x in numbers] #[expression for item in iterable if condition]
# # print(squares)



# # tup = (10, 20, 30) 

# # print(tup)
# # print(type(tup))


# # L = ["apple","banana","mango"] #note : In case of list, we use square brackets 

# # print(L)
# # print(type(L))



# # Dict = { 'Dict1': { },
# #         'Dict2': { }}
# # print("Nested dictionary 1 :")
# # print(Dict)

# # #having same keys
# # Dict = { 'Dict1': {'name': 'Sarthak', 'age': '19'},
# #         'Dict2': {'name': 'Rohit', 'age': '25'}}

# # print("\nNested dictionary 2 :")
# # print(Dict)

# # # Nested dictionary of mixed dictionary keys
# # Dict = { 'Dict1': {1: 'T', 2: 'E', 3: 'A'},
# #         'Dict2': {'Name': 'CUP', 1: [1, 2]} }

# # print("\nNested dictionary 3 :")
# # print(Dict)


# # nested_dict = {
# #     "student1": {"name": "S1", "major": "Computer Science"},
# #     "student2": {"name": "S2", "major": "Physics"},
# #     "student3": {"name": "S3", "major": "Mathematics"}
# # }

# # # Indexing
# # print(nested_dict["student3"]["major"])  


# # #slicing
# # slice_dict = {key: value for key, value in nested_dict.items() if key != "student1"} 
# # print(slice_dict)



# # # Defining a class
# # class Employee():
    
# #     def __init__(self, name, position):
# #         self.name = name
# #         self.position = position  # self used to represent the instance of the class
                
                
# #     def show(self):
# #         print("Employee name:", self.name)
# #         print("Employee position:", self.position)

# # obj=Employee(name= "Rahul", position= "Engineer")
# # obj.show()

# # print(dir(obj)) #list all the methods by it's obj



# # class Person():
    
# #     def __init__(mygame,name,age) :
# #         mygame.name= name 
# #         mygame.age= age

# #     def sar(mygsame):
# #         print("Person name:", mygame.name)
# #         print("Person age:", mygame.age)
        
# # p1= Person("Sarth", 20)

# # p1.sar()


# class ch:
#     def __init__(self,value1):
#         self.value1 = value1

#     def __add__(self,value2):
#        return  self.value1 + value2

# check= ch(20)
# r=check.__add__(130)
# print(r)


# def __init__()

  
# try:
#     a=5/int (input("Enter the number:"))
# except ZeroDivisionError:
#     print("Something went wrong")
# finally:
#     print("The 'try except' is finished")


try:
    result = 10/ 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print("The result is:", result)

