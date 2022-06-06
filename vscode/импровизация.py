try:
    a = int(input("напиши первое число"))
    b = int(input("напиши второе число"))

    if a < b:
        print ("Производится умножение...произведение = ", (a*b))
    elif (a > b):
        print(a/b)
    else: 
        print(a + b)
except ZeroDivisionError:
    print("Ты дурак?")




