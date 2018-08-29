import math

while True:
 print("Options:")
 print("1. Calculator")
 print("2. Converter")
 user_input = input("")
 if user_input == "quit":
        break
 
 elif user_input == "1":
     print("Enter 'add' to add two numbers")
     print("Enter 'subtract' to subtract two numbers")
     print("Enter 'multiply' to multiply two numbers")
     print("Enter 'divide' to divide two numbers")
     print("Enter 'expo' to find the power of a number")
     print("Enter 'modulo' to find the quotient two numbers")
     print("Enter 'sqrt' to find the sqrt of a number")
     print("Enter 'quit' to quit the program")
     user_input = input("")
     
     if user_input == "quit":
        break
    
     elif user_input == "add":
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter another number:"))
        result = str(num1 + num2)
        print("The answer is " + result)
        
     elif user_input == "subtract":
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter another number:"))
        result = str(num1 - num2)
        print("The answer is " + result)
        
     elif user_input == "multiply":
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter another number:"))
        result = str(num1 * num2)
        print("The answer is " + result)
        
     elif user_input == "divide":
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter another number:"))
        result = str(num1 / num2)
        print("The answer is " + result)
        
     elif user_input == "expo":
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter the expo number:"))
        result = str(num1 ** num2)
        print("The answer is " + result)
        
     elif user_input == "modulo":
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter another number:"))
        result = str(num1 % num2)
        print("The answer is " + result)
        
     elif user_input == "sqrt":
        num1 = float(input("Enter a number:"))
        result = str(math.sqrt(num1))
        print("The answer is " + result)
        
     else:
         print("Unknown Input")
     
 elif user_input == "2":
     print("Enter 'temp' for temperature")
     print("Enter 'dist' for distance")
     print("Enter 'wgt' for weight ")
     print("Enter 'hgt' for height")
     user_input = input("")
     
     if user_input == "quit":
        break
    
     if user_input == "temp":
         print("1. Fahrenheit to Celsius")
         print("2. Celsius to Fahrenheit")
         user_input = input("")
 
         if user_input == "1":
             num1 = float(input("Enter a temperature:"))
             result = str((num1 - 32)/1.8)
             print("Temperature in Celsius is: " + result)
             
         elif user_input =="2":
             num1 = float(input("Enter a temperature:"))
             result = str((num1 * 1.8)+32)
             print("Temperature in Fahrenheit is: " + result)
             
         else:
             print("Unknown Input")
             
     if user_input == "dist":
         print("1. Kilometers to Miles")
         print("2. Miles to Kilometer")
         user_input = input("")
 
         if user_input == "1":
             num1 = float(input("Enter distance in Km :"))
             result = str(num1 * 0.621371)
             print("Distance in Miles is: " + result)
             
         elif user_input =="2":
             num1 = float(input("Enter distance in Mi :"))
             result = str(1.609344*num1)
             print("Distance in Kilometers is: " + result)
                          
         else:
             print("Unknown Input")
                          
     if user_input == "wgt":
         print("1. Kilograms to Pounds")
         print("2. Pounds to Kilograms")
         user_input = input("")
 
         if user_input == "1":
             num1 = float(input("Enter weight in Kg :"))
             result = str(num1 * 2.20462)
             print("Weight in Pounds is: " + result)
                          
         elif user_input =="2":
             num1 = float(input("Enter weight in lbs :"))
             result = str(num1/2.20462)
             print("Weight in Pounds is: " + result)
                          
         else:
             print("Unknown Input")

     if user_input == "hgt":
         print("1. Feet and Inchs to centimeters")
         print("2. Centimeters to Feet and Inchs")
         user_input = input("")
 
         if user_input == "1":
             num1 = float(input("Enter your height in Feet range only :"))
             num2 = float(input("Enter your height in inches range only :"))             
             result = str(((num1 * 12)+num2)*2.54)
             print("Height in Centimeters is: " + result)
                          
         elif user_input =="2":
             num1 = float(input("Enter height in cms :"))
             feet = (num1*0.3937008)/12
          
                          
         else:
             print("Unknown Input")
             
             
        


 


    
     
 
