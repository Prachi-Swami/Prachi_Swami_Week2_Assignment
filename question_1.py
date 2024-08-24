# Create a program that manages a list of student
# names, allowing the user to add, remove, and
# display the list.
def menu():
  print("\n LIST MANAGER")
  print("1.Display Student")
  print("2.Add Student")
  print("3.Remove Student")
  print("4.EXIT")

def display(students):
  if not students:
    print("\nthe students list is empty.")
  else:
    print("\nStudent List: ")
    for student in students:
      print(student )
      
def add(students):
  name=input("enter name of student: ")
  students.append(name)
  print(f"{name} ADDED SUCCESSFULLY\n")
 
def remove(students):
  name=input("Enter name of student to remove : ")
  if name in students:
    students.remove(name)
    print(f"{name}REMOVED SUCCESSFULLY\n")
  else:
    print("Student NOT Found")

def main():
  students=[]
  while True:
    menu()
    choice=input("Enter Your Choice: ")
    if choice=="1":
     display(students)
    elif choice=="2":
      add(students)
    elif choice=="3":
      remove(students)
    elif choice =="4":
      print("Quitting The Program ") 
    else:
      print("Invalid Choice. Please enter valid choice") 
if __name__=="__main__":
  main()