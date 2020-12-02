def main():
    temp = 0
    print("Would you like to enter a temperature in Farenheit or Celsius?")
    input1 = input()
    if input1 == "F":
        print("Please Enter a temperature to convert to Celsius:")
        input2 = int(input())
        input2 = round((input2 - 32)/1.8)
        print("The new temperature is " + str(input2) + " degrees Celsius")
        check()
    elif input1 == "C":
        print("Please Enter a temperature to convert to Farenheit:")
        input2 = int(input())
        input2 = round((input2*1.8+32))
        print("The new temperature is " + str(input2) + " degrees Farenheit")
        check()
    else:
        print("Sorry I didnt catch that, Please try again!")
        main()

def check():
    print("Do you have another conversion?(y/n)")
    input1 = input()
    if input1 == "y":
        main()

main()

