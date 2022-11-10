
import function
import csv
if __name__ == "__main__":
    print("Greetings! To Login, you have to register using a valid email id\n")
    print("If you would like\nTo Login press 1 \nTo Register press 2 \nTo recover password press 3 ")
    A = input()
    if A == '1':
        print("Welcome to Login Page ....!")
        function.login()
        exit()

    elif A == '2':
        print("Welcome to Register Page")
        Email = input("Enter your Email id:  ")
        function.check(Email)
        print("Please enter a valid email id to proceed\n")
        print("PASSWORD Instructions:\n"
              "  1)Length should be greater than 8 and less than 16\n"
              " 2)Atleast one capital and one small letter\n "
              " 3)Atleast 1 number\n "
              " 4)Either of the special characters-@#$! \n ")

        print("Please enter your Password: ")
        Password = function.get()
        print("The Password is correct")
        print("Logged in successfully \n")
        with open("Login.csv", 'a') as file:
            info = csv.writer(file,lineterminator='\n')
            info.writerow([Email, Password])
            file.close()
        exit()
    elif A == '3':
        function.getpwd()
    else:
        print("Invalid Password")