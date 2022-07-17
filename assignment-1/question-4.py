# (4) Write a program with python which could accept two parameter a and b to calculate and output the result of S, where
# $\ S=3.14*(1+a/b)^3$ (6 points)

def formula_given(a, b):
    s = float(3.14 * float((1 + a / b)**3))
    return s


print(formula_given(1, 2))
