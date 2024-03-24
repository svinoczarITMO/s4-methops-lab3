import math

f = lambda x: x**2 - 3*x + x * math.log(x, math.e)
# step 1
a, b = 1, 2
x1 = (a+b)/2
epsilon = 0.0001
delta_x = 0.01
flag = 0

def quadratic_approximation(x1, x2, x3, fl):
    flag = fl
    if not flag:
        # step 2
        x2 = x1 + delta_x
        # step 3
        f1 = f(x1)
        f2 = f(x2)
        # step 4
        if f1 > f2:
            x3 = x1 + 2*delta_x
        else:
            x3 = x1 - delta_x
        # step 5
        f3 = f(x3)
        
    # step 6
    F_min = min(f1, f2, f3)
    x_min = x1 if F_min == f1 else (x2 if F_min == f2 else x3)
    # step 7
    x_numerator = ((x2**2 - x3**2)*f1 + (x3**2 - x1**2)*f2 + (x1**2 - x2**2)*f3)
    x_denominator = ((x2-x3)*f1 + (x3-x1)*f2 + (x1-x2)*f3)
    if x_denominator == 0:
        x1 = x_min
        return quadratic_approximation(x1, x2, x3, flag)

    x = 0.5*(x_numerator/x_denominator)
    fx = f(x)
    # step 8
    condition1 = abs((F_min - fx) / fx) < epsilon
    condition2 = abs((x_min - x) / x) < epsilon

    if condition1 and condition2:
        return x
    elif (not condition1 or not condition2) and (x1 <= x and x <= x3):
        x2 = min(x_min, x)
        flag = 1
        return quadratic_approximation(x1, x2, x3, flag)
    elif (not condition1 or not condition2) and not (x1 <= x and x <= x3):
        x1 = x
        return quadratic_approximation(x1, x2, x3, flag)


def main():
    print(quadratic_approximation(x1, 0, 0, flag))
    
if __name__ == '__main__':
    main()
