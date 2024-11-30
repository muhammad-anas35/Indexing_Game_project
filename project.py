# access, modify, slice option available for list .
msg1 :str = "Select the option below : "
my_list :list = [10, "hello", 3.14, True, "world"]

def access_function(index):
  try:
    print(my_list[index])
  except IndexError:
    print("Invalid index to acess ")

def modify_function(index):
  try:
    modified = input("Enter a value to update selected index : ")
    my_list[index] = modified
    return my_list
  except IndexError:
    print("Invalid index to modify ")

def slice_function(index):
  try:
    sec_index = int(input("Input second index to Slice the List : "))
    print( my_list[index:sec_index]   )

  except IndexError:
    print("Invalid index to slice ")

def main():


  print(msg1)
  print("1 : For access list item ")
  print("2 : For modify list item ")
  print("3 : For slice list item ")

  try :
    user_choice = int(input("Enter a number \"1 to 3\" to execute the programme : "))
    user_index = int(input("Enter a  index to perform action : "))
  except ValueError:
    print("Invalid input.no 2")

  if user_choice == 1:
    access_function(user_index)
    print(my_list)
  elif user_choice == 2:
    modify_function(user_index)
    print(my_list)
  elif user_choice == 3:
    slice_function(user_index)

  else :
    print("Invalid Input")

if __name__ == '__main__':
  main()