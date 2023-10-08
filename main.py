import lab2

num_to_func = {
  "1": lab2.task_if4,
  "2": lab2.task_geometry21,
  "3": lab2.task_12
}

# Стандартний варіант реалізації меню через розгалуження
if __name__ == "__main__":
  choice = "-1"
  while choice != "0":
    choice = input("Please, choose the task again (0-EXIT): ")
    if choice == "1":
      lab2.task_if4()
    elif choice == "2":
      lab2.task_geometry21()
    elif choice=="3":
      lab2.task_12()
    else:
      print("Wrong task number!")
  print("Good by!")
