def greet_and_multiply(*num,**student):
    number=1
    for a in num:
        number*=a
        print(number)
    print(f"Hello {student}")