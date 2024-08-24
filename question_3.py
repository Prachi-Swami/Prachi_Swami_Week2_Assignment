# implement a program that takes a tuple of
# integers and returns a new tuple with even
# numbers only.

def even_number(tuple_numbers):
   even=tuple(num for num in tuple_numbers if num %2==0)
   return even

def main():
  numbers=input("enter numbers with space: ")
  numbers_list=numbers.split()
  numbers_tuple=tuple(map(int,numbers_list))
  even=even_number(numbers_tuple)
  print("tuple with even numbers: ",even)

if __name__ == "__main__":
    main()  