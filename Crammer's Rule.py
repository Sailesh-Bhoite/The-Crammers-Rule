"""
Crammers Rule Program:
    It is an implementation of Crammer's Rule to solve the two and three variable simultaneous equations.

    Problem:
        Solves only those equations which have solutions.
"""
import numpy as np

n = int(input("Number of variables: "))

if n == 2:
    print("Enter the equation in 'x' and 'y' variables.")
    eq1 = input("Enter first equation: ")
    eq2 = input("Enter second equation: ")


    def separate(equation: str):
        l1 = []
        var = []
        constants = []
        for i in equation:
            if i.isalpha():
                l1.append(" ")
                var.append(i)
            else:
                l1.append(i)

        s2 = "".join(l1)
        coefficient = s2.split()
        if coefficient[-1][0] == "=":
            coefficient[-1] = coefficient[-1][1:]

        # Condition if the coefficient of "x" is positive one.
        if equation[0] == "x":
            coefficient.insert(0, "+")

        constants.append(coefficient[-1])
        coefficient = coefficient[:-1]
        for num, c in enumerate(coefficient):
            if len(c) == 1:
                if c == "+":
                    coefficient[num] = "1"
                elif c == "-":
                    coefficient[num] = "-1"

        return coefficient, var, constants


    def balance(coefflist: list[int], varlist: list[str]) -> (list, list):
        if "x" not in varlist or "y" not in varlist:  # For absent numbers
            print("missing elements!")
            c_list = [0, 0]
            if "x" in varlist:
                c_list[0] = coefflist[varlist.index("x")]
            if "y" in varlist:
                c_list[1] = coefflist[varlist.index("y")]

        else:  # For present numbers
            if varlist[0] == "x" and varlist[1] == "y":
                return coefflist, varlist
            else:  # For miss-matched numbers
                c_list = [coefflist[varlist.index("x")], coefflist[varlist.index("y")]]
                return c_list, ["x", "y"]


    def formD(variable: str, constant_matrix: np.ndarray, main_matrix: np.ndarray) -> np.ndarray:
        const = constant_matrix
        main = main_matrix
        if variable == "x":
            one, two = np.split(main, 2, axis=1)
            dx = np.hstack([const, two])
            return dx
        elif variable == "y":
            one, two = np.split(main, 2, axis=1)
            dy = np.hstack([one, const])
            return dy


    coeff1, var1, const1 = separate(eq1)
    coeff1 = [int(x) for x in coeff1]
    coeff1, var1 = balance(coeff1, var1)
    const1 = [int(x) for x in const1]

    coeff2, var2, const2 = separate(eq2)
    coeff2 = [int(x) for x in coeff2]
    coeff2, var2 = balance(coeff2, var2)
    const2 = [int(x) for x in const2]

    matrix = np.array([coeff1, coeff2])
    print("\nThe matrix will be:\n", matrix)
    det = round(np.linalg.det(matrix))
    if det == 0:
        print("But these equations have many outputs.")
        exit(77)
    print("D:", det, sep=" -> ")
    const_matrix = np.array([const1, const2])
    print("\nThe constants are:\n", const_matrix)

    dX = formD("x", const_matrix, matrix)
    dY = formD("y", const_matrix, matrix)

    detx = round(np.linalg.det(dX))
    dety = round(np.linalg.det(dY))

    print("\nMatrix X:\n", dX)
    print("DX:", detx, sep=" -> ")
    print("\nMatrix Y:\n", dY)
    print("DY:", dety, sep=" -> ")

    x = detx / det
    y = dety / det

    print("\n\nx = ", x, "\ny = ", y)

elif n == 3:
    print("Enter the equation in 'x', 'y' and 'z' variables.")
    eq1 = input("Enter first equation: ")
    eq2 = input("Enter second equation: ")
    eq3 = input("Enter third equation: ")

    def separate(equation: str):
        l1 = []
        var = []
        constants = []
        for i in equation:
            if i.isalpha():
                l1.append(" ")
                var.append(i)
            else:
                l1.append(i)

        s2 = "".join(l1)
        coefficient = s2.split()
        if coefficient[-1][0] == "=":
            coefficient[-1] = coefficient[-1][1:]

        # Condition if the coefficient of "x" is positive one.
        if equation[0] == "x":
            coefficient.insert(0, "+")

        constants.append(coefficient[-1])
        coefficient = coefficient[:-1]
        for num, c in enumerate(coefficient):
            if len(c) == 1:
                if c == "+":
                    coefficient[num] = "1"
                elif c == "-":
                    coefficient[num] = "-1"

        return coefficient, var, constants


    def balance(coefflist: list[int], varlist: list[str]) -> (list, list):
        if "x" not in varlist or "y" not in varlist or "z" not in varlist:  # For absent numbers
            print("missing elements!")
            c_list = [0, 0, 0]
            v_list = ["x", "y", "z"]
            if "x" in varlist:
                c_list[0] = coefflist[varlist.index("x")]
            if "y" in varlist:
                c_list[1] = coefflist[varlist.index("y")]
            if "z" in varlist:
                c_list[2] = coefflist[varlist.index("z")]
            return c_list, v_list
        else:  # For present numbers
            if varlist[0] == "x" and varlist[1] == "y" and varlist[2] == "z":
                return coefflist, varlist
            else:  # For miss-matched numbers
                c_list = [coefflist[varlist.index("x")], coefflist[varlist.index("y")], coefflist[varlist.index("z")]]
                v_list = ["x", "y", "z"]
                return c_list, v_list


    def formD(variable: str, constant_matrix: np.ndarray, main_matrix: np.ndarray) -> np.ndarray:
        const = constant_matrix
        main = main_matrix
        if variable == "x":
            one, two, three = np.split(main, 3,  axis=1)
            dx = np.hstack([const, two, three])
            return dx
        elif variable == "y":
            one, two, three = np.split(main, 3, axis=1)
            dy = np.hstack([one, const, three])
            return dy
        elif variable == "z":
            one, two, three = np.split(main, 3, axis=1)
            dz = np.hstack([one, two, const])
            return dz


    coeff1, var1, const1 = separate(eq1)
    coeff1 = [int(x) for x in coeff1]
    coeff1, var1 = balance(coeff1, var1)
    const1 = [int(x) for x in const1]

    coeff2, var2, const2 = separate(eq2)
    coeff2 = [int(x) for x in coeff2]
    coeff2, var2 = balance(coeff2, var2)
    const2 = [int(x) for x in const2]

    coeff3, var3, const3 = separate(eq3)
    coeff3 = [int(x) for x in coeff3]
    coeff3, var3 = balance(coeff3, var3)
    const3 = [int(x) for x in const3]

    matrix = np.array([coeff1, coeff2, coeff3])
    print("\nThe matrix will be:\n", matrix)
    det = round(np.linalg.det(matrix))
    print("D:", det, sep=" -> ")
    const_matrix = np.array([const1, const2, const3])
    print("\nThe constants are:\n", const_matrix)

    dX = formD("x", const_matrix, matrix)
    dY = formD("y", const_matrix, matrix)
    dZ = formD("z", const_matrix, matrix)

    detx = round(np.linalg.det(dX))
    dety = round(np.linalg.det(dY))
    detz = round(np.linalg.det(dZ))

    print("\nMatrix X:\n", dX)
    print("DX:", detx, sep=" -> ")
    print("\nMatrix Y:\n", dY)
    print("DY:", dety, sep=" -> ")
    print("\nMatrix Z:\n", dZ)
    print("DZ:", detz, sep=" -> ")

    x = detx/det
    y = dety/det
    z = detz/det

    print("\n\nx = ", x, "\ny = ", y, "\nz = ", z)

else:
    print("This program is made to solve only 2 and 3 variable simultaneous equations.\nAnd, you have given number of variable other than 2 and 3.")
