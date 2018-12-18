import sys

def solve(target, expr):
    if not expr:
        return []
    sols = []
    helper(sols,0,0, target, 0, expr, "" )
    if len(sols) > 0:
        for solution in sols:
            print (solution)
        print("\n")
    else:
        print ("Impossible\n")

def helper(solutions, position, curVal, target, previous, expr, path):
    if position == len(expr):
        if curVal == target:
            solutions.append(path)
            return
    for i in range(position, len(expr)):
        temp = expr[position:i+1]
        if len(temp) > 1 and temp[0] == "0":
            break
        if position == 0:
            helper(solutions, i+1, int(temp), target, int(temp), expr, temp)
        else:
            helper(solutions, i+1, curVal + int(temp), target, int(temp), expr, path + "+"  + temp)
            helper(solutions, i+1, curVal - int(temp), target, -int(temp), expr, path + "-"  + temp)
            helper(solutions, i+1, curVal - previous + previous*int(temp), target, int(temp)*previous, expr, path + "*"  + temp)

if __name__ == "__main__":
    try:
        target = int(sys.argv[1])
        nums = []
        count = 2
        for value in sys.argv[2:]:
            try:
                int(value)
                nums.append(value)
            except ValueError as V:
                print("Sorry {} in argument {} is not a number. The digit sequence must be an integer\n".format(value, count))
            count += 1
        for num in nums:
            solve(target, num)

    except ValueError as V:
        print("Sorry {} is not a number. The target number must be an integer.".format(sys.argv[1]))