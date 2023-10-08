import math  # підключення бібліотеки


def task_if4():
    """Three integers are given. Find the number of positive numbers in 
       the initial set."""
    try:
        count = 0
        int_num1=int(input("Enter first integer number: "))
        int_num2=int(input("Enter second integer number: "))
        int_num3=int(input("Enter third integer number: "))
        if int_num1 > 0:
            count += 1
        if int_num2 > 0:
            count += 1
        if int_num3 > 0:
            count += 1
        print("Number of positive integers: ", count)
    except ValueError:
        print("INTEGER expected!")

def task_geometry21():
    """Calculation of the number of points inside the area according to the variant"""
    # Ввод входных параметров
    try:
        a = int(input("a = "))
        r = int(input("r = "))
        if a <= 0 or r <= 0:
            raise ValueError
    except ValueError:
        print("Wrong values (a, r)")
    else:
        # створюємо список координат
        x_y_list = [] 
        # Вводимо координати точок для перевірки
        try:
            n = int(input("N = "))
            for i in range(n):  # n = 3: range(3) = 0, 1, 2
                x_i = float(input("\nX{} = ".format(i + 1)))
                y_i = float(input("Y{} = ".format(i + 1)))
                x_y_list.append((x_i, y_i))
        except ValueError:
            print("Wrong values (n, x, y)")
        else:
            # лічильник
            in_count = 0
            # Безпосередня перевірка входження кожної з наявних точок
            circle_r = a / 2
            center_x = a / 2
            center_y = a / 2
            for x, y in x_y_list: # [(2,1), (1, 1), (3, -1)]
                length = math.sqrt(math.pow(x - center_x, 2) + \
                math.pow(y - center_y, 2))
                if (0 <= x <= center_x and 0 <= y <= a and length <= \
                 (math.pi * circle_r * circle_r) / 4) or \
                (center_x < x <= a and 0 <= y <= a and length >= ((a * \
                a) / 2) - ((math.pi * circle_r * circle_r) / 8)):
                    in_count += 1
            print("Final count = {}".format(in_count))

def task_12():
       """Calculate mathematical expression"""
       n = 1
       s = 0
       e = 1e-10  
       g = 1e+10
       while True:
         try:
           num = (math.factorial(n)*(math.e**n))
           denum = (n**(n**0.5))
           u = num / denum
         except ValueError:
           print("Something went wrong!")
         except ZeroDivisionError:
           print("Division by zero")
         else:
           s += u
           n += 1
           print(u)
           if abs(u) < e:
            print("Ряд збігається до ", s)
            break
           elif abs(u) > g:
             print("Ряд розбігається")
             break

if __name__ == "__main__":
  task_series1()
