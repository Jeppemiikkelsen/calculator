operation = input("type in which operation you would like to do, you have the following options: + x / or - ")
if operation == "+":
    firstnum = float(input("the first number in the addition:"))
    secondnum = float(input("the second number in the addition:"))
    print(firstnum+secondnum)
elif operation == "/":
    firstnum = (input("the number in the numerator:"))
    secondnum = (input("the number in the denominator:"))
    print(float(firstnum)/float(secondnum))
elif operation == "x":
    firstnum = float(input("the first number to be multiplied:"))
    secondnum = float(input("the second number to be multiplied:"))
    print(firstnum*secondnum)
elif operation == "-":
    firstnum = float(input("the first number in the subtraction:"))
    secondnum = float(input("the second number in the subtraction:"))
    print(firstnum-secondnum)
else:
    # hvis bruger indtaster forkert. så får man nyt forsøg
    operation = input("Please type in a valid option, you have the following options: + x % or - ")
    if operation == "+":
        firstnum = float(input("the first number in the addition:"))
        secondnum = float(input("the second number in the addition:"))
        print(firstnum + secondnum)
    elif operation == "%":
        firstnum = (input("the number in the numerator:"))
        secondnum = (input("the number in the denominator:"))
        print(float(firstnum) / float(secondnum))
    elif operation == "x":
        firstnum = float(input("the first number to be multiplied:"))
        secondnum = float(input("the second number to be multiplied:"))
        print(firstnum * secondnum)
    elif operation == "-":
        firstnum = float(input("the first number in the subtraction:"))
        secondnum = float(input("the second number in the subtraction:"))
        print(firstnum - secondnum)