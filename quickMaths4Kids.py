import sys

# TODO add justification comments
# TODO add ascii art to all outputs

oddOrEvenCorrectList = []
additiontList = []
subtractionList = []
multiplicationlList = []
divisionList = []


# I created a function in order to reduce the number of times the same
# Lines of code need to be repeated, In addition it makes the code more maintainable and allows for better debugging.
def get_string(input):
    sys.stdout.write(input)
    sys.stdout.flush()
    user_string_input = sys.stdin.readline().lower().strip()
    return user_string_input

# I create a function in order to reduce the number of times the same lines of code need to be repeated
# It also allows for me to be able to change the output in one place and it also allows for better debugging


def correct_answer_odd_even(correctAnswer):
    userChoice = str(
        get_string("\nPlease enter your choice: "))
    # I make a while loop expect of a in if statement to reduce the number of lines of code.
    # It also fakes sure that the code is executed only if the user input is the correct answer.
    while (userChoice == correctAnswer):
        oddOrEvenCorrectList.append(userChoice)
        sys.stdout.write("+1 Correct (◠﹏◠)\n\n")
        break

# I create a function in order to reduce the number of times the same lines of code need to be repeated
# It also allows for me to be able to change the output in one place and it also allows for better debugging


def correct_answer_addition(correctAnswer):
    userChoice = int(
        get_string("\nPlease enter your choice: "))
    # I make a while loop expect of a in if statement to reduce the number of lines of code.
    # It also fakes sure that the code is executed only if the user input is the correct answer.
    while (userChoice == correctAnswer):
        additiontList.append(userChoice)
        sys.stdout.write("+1 Correct (◠﹏◠)\n\n")
        break


# I create a function in order to reduce the number of times the same lines of code need to be repeated
# It also allows for me to be able to change the output in one place and it also allows for better debugging
def correct_answer_subtraction(correctAnswer):
    userChoice = int(
        get_string("\nPlease enter your choice: "))
    # I make a while loop expect of a in if statement to reduce the number of lines of code.
    # It also fakes sure that the code is executed only if the user input is the correct answer.
    while (userChoice == correctAnswer):
        subtractionList.append(userChoice)
        sys.stdout.write("+1 Correct (◠﹏◠)\n\n")
        break

# I create a function in order to reduce the number of times the same lines of code need to be repeated
# It also allows for me to be able to change the output in one place and it also allows for better debugging


def correct_answer_multiplication(correctAnswer):
    userChoice = float(
        get_string("\nPlease enter your choice: "))
    # I make a while loop expect of a in if statement to reduce the number of lines of code.
    # It also fakes sure that the code is executed only if the user input is the correct answer.
    while (userChoice == correctAnswer):
        multiplicationlList.append(userChoice)
        sys.stdout.write("+1 Correct (◠﹏◠)\n\n")
        break

# I create a function in order to reduce the number of times the same lines of code need to be repeated
# It also allows for me to be able to change the output in one place and it also allows for better debugging


def correct_answer_divisionList(correctAnswer):
    userChoice = float(
        get_string("\nPlease enter your choice: "))
    # I make a while loop expect of a in if statement to reduce the number of lines of code.
    # It also fakes sure that the code is executed only if the user input is the correct answer.
    while (userChoice == correctAnswer):
        divisionList.append(userChoice)
        sys.stdout.write("+1 Correct (◠﹏◠)\n\n")
        break


def main():
    # I used a while loop to insure that the user is always returned to the main menu after one of the option in the if statement is completed.

    while True:
        sys.stdout.write("""
 ____        _       _      __  __       _   _           _  _     _  ___     _     
/ __ \      (_)     | |    |  \/  |     | | | |         | || |   | |/ (_)   | |    
| |  | |_   _ _  ___| | __ | \  / | __ _| |_| |__  ___  | || |_  | ' / _  __| |___ 
| |  | | | | | |/ __| |/ / | |\/| |/ _` | __| '_ \/ __| |__   _| |  < | |/ _` / __|
| |__| | |_| | | (__|   <  | |  | | (_| | |_| | | \__ \    | |   | . \| | (_| \__  
 \___\_\\__,_|_|\___ |_|\_\ |_|  |_|\__,_|\__|_| |_|___/    |_|   |_|\_\_|\__,_|___/
+----------------------------------------------------------------------------------+
Choose one of the quick games below:
+----------------------------------------------------------------------------------+
[1] ODD or EVEN
[2] + Addition
[3] - Subtraction
[4] X Multiplication
[5] ÷ Division
[6] = Scoreboard
[7] Exit
+----------------------------------------------------------------------------------+
Please enter your choice: """)
        sys.stdout.flush()
        choice = sys.stdin.readline().strip()
        # I picked an if statement for the options so i can make sure the selection of each option is tracked.
        # It also allows me to check for options other then the correct ones and provide a helpful message.
        if choice == "1":
            sys.stdout.write("""\n+----------------------------------------------------------------------------------+
Type 'odd' or 'even' and press 'Enter'.
Answer correctly to get +1 point.
+----------------------------------------------------------------------------------+

Is the following number ODD or EVEN ?
       __
      /_ |
       | |
       | |
       | |
       |_|
""")
            correct_answer_odd_even("odd")
            sys.stderr.write("""        ___  
       |__ \ 
          ) |
         / / 
        / /_ 
       |____|
""")
            correct_answer_odd_even("even")
            sys.stdout.write("""Is the following number ODD or EVEN ?
        ____  
       |___ \ 
         __) |
        |__ < 
        ___) |
       |____/ 
""")
            correct_answer_odd_even("odd")
            sys.stderr.write("""Is the following number ODD or EVEN ?
        _  _     
       | || |   
       | || |_  
       |__   _| 
           | |  
           |_|  
""")
            correct_answer_odd_even("even")
            sys.stdout.write("""Is the following number ODD or EVEN ?
         _____ 
        | ____|
        | |__  
        |___ \ 
         ___) |
        |____/ 
""")
            correct_answer_odd_even("odd")
            sys.stderr.write("""Is the following number ODD or EVEN ?           
          __  
         / /  
        / /_  
       | '_ \ 
       | (_) |
        \___/ 
""")
            correct_answer_odd_even("even")
            sys.stdout.write("""\n**********************************************************************************
\nMake sure to Check your Score at option [6]
\n**********************************************************************************\n\n""")
            # This elif stament was used in order to provide the write output in the instance tha the user provided it with the correct input.
        elif choice == "2":
            sys.stdout.write("""\n+----------------------------------------------------------------------------------+
Type the missing number '?' and press 'Enter'.
Answer correctly to get +1 point.
+----------------------------------------------------------------------------------+

What is the missing number ?
  _  _                 ___                 _____ 
 | || |        _      |__ \     ______    | ____|
 | || |_     _| |_       ) |   |______|   | |__  
 |__   _|   |_   _|     / /     ______    |___ \ 
    | |       |_|      |_|     |______|    ___) |
    |_|                (_)                |____/ 
""")
            correct_answer_addition(1)
            sys.stdout.write("""What is the missing number ?
  __    ___                _____                ___  
 /_ |  / _ \       _      | ____|    ______    |__ \ 
  | | | | | |    _| |_    | |__     |______|      ) |
  | | | | | |   |_   _|   |___ \     ______      / / 
  | | | |_| |     |_|      ___) |   |______|    |_|  
  |_|  \___/              |____/                (_)  
""")

            correct_answer_addition(15)
            sys.stdout.write("""What is the missing number ?
  ___                __    ___                 ____     ___  
 |__ \       _      /_ |  / _ \     ______    |___ \   / _ \ 
    ) |    _| |_     | | | | | |   |______|     __) | | | | |
   / /    |_   _|    | | | | | |    ______     |__ <  | | | |
  |_|       |_|      | | | |_| |   |______|    ___) | | |_| |
  (_)                |_|  \___/               |____/   \___/ 
""")

            correct_answer_addition(20)
            sys.stdout.write("""What is the missing number ?
  ____     ___                ___                 ______    ___  
 |___ \   / _ \       _      |__ \     ______    |____  |  / _ \ 
   __) | | | | |    _| |_       ) |   |______|       / /  | | | |
  |__ <  | | | |   |_   _|     / /     ______       / /   | | | |
  ___) | | |_| |     |_|      |_|     |______|     / /    | |_| |
 |____/   \___/               (_)                 /_/      \___/ 
""")

            correct_answer_addition(40)
            sys.stdout.write("""What is the missing number ?
  __    ___     ___                __    ___                 ___  
 /_ |  / _ \   / _ \       _      /_ |  / _ \     ______    |__ \ 
  | | | | | | | | | |    _| |_     | | | | | |   |______|      ) |
  | | | | | | | | | |   |_   _|    | | | | | |    ______      / / 
  | | | |_| | | |_| |     |_|      | | | |_| |   |______|    |_|  
  |_|  \___/   \___/               |_|  \___/                (_)  
""")

            correct_answer_addition(110)
            sys.stdout.write("""What is the missing number ?
  ___                  __     ___                 ______    ___  
 |__ \       _        / /    / _ \     ______    |____  |  / _ \ 
    ) |    _| |_     / /_   | (_) |   |______|       / /  | | | |
   / /    |_   _|   | '_ \   > _ <     ______       / /   | | | |
  |_|       |_|     | (_) | | (_) |   |______|     / /    | |_| |
  (_)                \___/   \___/                /_/      \___/ 
""")

            correct_answer_addition(2)
            sys.stdout.write("""\n**********************************************************************************
\nMake sure to Check your Score at option [6] 
\n**********************************************************************************\n\n""")
            # This elif stament was used in order to provide the write output in the instance tha the user provided it with the correct input.
        elif choice == "3":
            sys.stdout.write("""\n+----------------------------------------------------------------------------------+\n
Type the missing number '?' and press 'Enter'. 
Answer correctly to get +1 point. 
+----------------------------------------------------------------------------------+\n
What is the missing number ?
  ______                ___                 _____ 
 |____  |              |__ \     ______    | ____|
     / /     ______       ) |   |______|   | |__  
    / /     |______|     / /     ______    |___ \ 
   / /                  |_|     |______|    ___) |
  /_/                   (_)                |____/ 
""")

            correct_answer_subtraction(2)
            sys.stdout.write("""What is the missing number ?
  __    ___                 _____                ___  
 /_ |  / _ \               | ____|    ______    |__ \ 
  | | | | | |    ______    | |__     |______|      ) |
  | | | | | |   |______|   |___ \     ______      / / 
  | | | |_| |               ___) |   |______|    |_|  
  |_|  \___/               |____/                (_)  
""")

            correct_answer_subtraction(5)
            sys.stdout.write("""What is the missing number ?

  ___                 __    ___                 _  _      ___  
 |__ \               /_ |  / _ \     ______    | || |    / _ \ 
    ) |    ______     | | | | | |   |______|   | || |_  | | | |
   / /    |______|    | | | | | |    ______    |__   _| | | | |
  |_|                 | | | |_| |   |______|      | |   | |_| |
  (_)                 |_|  \___/                  |_|    \___/
""")

            correct_answer_subtraction(50)
            sys.stdout.write("""What is the missing number ?
  __   ___    _____                ___                 ___    _____ 
 /_ | |__ \  | ____|              |__ \     ______    |__ \  | ____|
  | |    ) | | |__      ______       ) |   |______|      ) | | |__  
  | |   / /  |___ \    |______|     / /     ______      / /  |___ \ 
  | |  / /_   ___) |               |_|     |______|    / /_   ___) |
  |_| |____| |____/                (_)                |____| |____/ """)

            correct_answer_subtraction(100)
            sys.stdout.write("""What is the missing number ?

  ___    ____                 ______                ___  
 |__ \  |___ \               |____  |    ______    |__ \ 
    ) |   __) |    ______        / /    |______|      ) |
   / /   |__ <    |______|      / /      ______      / / 
  / /_   ___) |                / /      |______|    |_|  
 |____| |____/                /_/                   (_)  
""")

            correct_answer_subtraction(16)
            sys.stdout.write("""What is the missing number ?
  ___                 ___    ___                 ___    ___  
 |__ \               |__ \  |__ \     ______    |__ \  |__ \ 
    ) |    ______       ) |    ) |   |______|      ) |    ) |
   / /    |______|     / /    / /     ______      / /    / / 
  |_|                 / /_   / /_    |______|    / /_   / /_ 
  (_)                |____| |____|              |____| |____|
""")

            correct_answer_subtraction(44)
            sys.stdout.write("""\n**********************************************************************************
\nMake sure to Check your Score at option [6] \n
**********************************************************************************\n\n""")
            #
        elif choice == "4":
            sys.stdout.write("""
+----------------------------------------------------------------------------------+
Type the missing number '?' as an **Float 1.0** and press 'Enter'. 
Answer correctly to get +1 point. 
+----------------------------------------------------------------------------------+
What is the missing number ?

  ___        _____              ____                 ___  
 |__ \      | ____|            |___ \     ______    |__ \ 
    ) |     | |__     __  __     __) |   |______|      ) |
   / /      |___ \    \ \/ /    |__ <     ______      / / 
  / /_   _   ___) |    >  <     ___) |   |______|    |_|  
 |____| (_) |____/    /_/\_\   |____/                (_)  
""")

            correct_answer_multiplication(7.5)
            sys.stdout.write("""What is the missing number ?

  ____               ___                 ___    ___        _____ 
 |___ \             |__ \     ______    |__ \  |__ \      | ____|
   __) |   __  __      ) |   |______|      ) |    ) |     | |__  
  |__ <    \ \/ /     / /     ______      / /    / /      |___ \ 
  ___) |    >  <     |_|     |______|    / /_   / /_   _   ___) |
 |____/    /_/\_\    (_)                |____| |____| (_) |____/ 
""")

            correct_answer_multiplication(5)
            sys.stdout.write("""
What is the missing number ?

  ____        _____              _____                ___  
 |___ \      | ____|            | ____|    ______    |__ \ 
   __) |     | |__     __  __   | |__     |______|      ) |
  |__ <      |___ \    \ \/ /   |___ \     ______      / / 
  ___) |  _   ___) |    >  <     ___) |   |______|    |_|  
 |____/  (_) |____/    /_/\_\   |____/                (_)  
""")

            correct_answer_multiplication(17.5)
            sys.stdout.write("""What is the missing number ?

  ___               ___                 _____ 
 |__ \             |__ \     ______    | ____|
    ) |   __  __      ) |   |______|   | |__  
   / /    \ \/ /     / /     ______    |___ \ 
  / /_     >  <     |_|     |______|    ___) |
 |____|   /_/\_\    (_)                |____/ 
""")

            correct_answer_multiplication(2.5)
            sys.stdout.write("""What is the missing number ?
  _  _         ___               ____                 ___  
 | || |       |__ \             |___ \     ______    |__ \ 
 | || |_         ) |   __  __     __) |   |______|      ) |
 |__   _|       / /    \ \/ /    |__ <     ______      / / 
    | |    _   / /_     >  <     ___) |   |______|    |_|  
    |_|   (_) |____|   /_/\_\   |____/                (_) 
""")

            correct_answer_multiplication(12.6)
            sys.stdout.write("""What is the missing number ?
  ___               _  _                  ___    _  _          ___  
 |__ \             | || |      ______    |__ \  | || |        / _ \ 
    ) |   __  __   | || |_    |______|      ) | | || |_      | (_) |
   / /    \ \/ /   |__   _|    ______      / /  |__   _|      > _ < 
  |_|      >  <       | |     |______|    / /_     | |    _  | (_) |
  (_)     /_/\_\      |_|                |____|    |_|   (_)  \___/ 
""")

            correct_answer_multiplication(6.2)
            sys.stdout.write("""
**********************************************************************************
Make sure to Check your Score at option [6] 
**********************************************************************************
""")
            # This elif stament was used in order to provide the write output in the instance tha the user provided it with the correct input.

        elif choice == "5":
            sys.stdout.write("""
+----------------------------------------------------------------------------------+
Type the missing number '?' as an **Float 1.0** and press 'Enter'.
Answer correctly to get +1 point.
+----------------------------------------------------------------------------------+

What is the missing number ?

  _____        _        ___                 ___  
 | ____|      (_)      |__ \     ______    |__ \ 
 | |__      _______       ) |   |______|      ) |
 |___ \    |_______|     / /     ______      / / 
  ___) |       _        / /_    |______|    |_|  
 |____/       (_)      |____|               (_)  
""")

            correct_answer_divisionList(2.5)
            sys.stdout.write("""
What is the missing number ?
  ___    __        _          __                 ___  
 |__ \  /_ |      (_)        / /      ______    |__ \ 
    ) |  | |    _______     / /_     |______|      ) |
   / /   | |   |_______|   | '_ \     ______      / / 
  / /_   | |       _       | (_) |   |______|    |_|  
 |____|  |_|      (_)       \___/                (_)  
""")

            correct_answer_divisionList(3.5)
            sys.stdout.write("""What is the missing number ?
 ____    ____         _          __                 ___  
|___ \  |___ \       (_)        / /      ______    |__ \ 
  __) |   __) |    _______     / /_     |______|      ) |
 |__ <   |__ <    |_______|   | '_ \     ______      / / 
 ___) |  ___) |       _       | (_) |   |______|    |_|  
|____/  |____/       (_)       \___/                (_)  
""")

            correct_answer_divisionList(5.5)
            sys.stdout.write("""What is the missing number ?

  ___    ____         _        _  _                  ___  
 |__ \  |___ \       (_)      | || |      ______    |__ \ 
    ) |   __) |    _______    | || |_    |______|      ) |
   / /   |__ <    |_______|   |__   _|    ______      / / 
  / /_   ___) |       _          | |     |______|    |_|  
 |____| |____/       (_)         |_|                 (_)  
""")

            correct_answer_divisionList(5.75)
            sys.stdout.write("""What is the missing number ?
  _  _     _  _          _        _____                ___  
 | || |   | || |        (_)      | ____|    ______    |__ \ 
 | || |_  | || |_     _______    | |__     |______|      ) |
 |__   _| |__   _|   |_______|   |___ \     ______      / / 
    | |      | |         _        ___) |   |______|    |_|  
    |_|      |_|        (_)      |____/                (_)  
""")

            correct_answer_divisionList(8.8)
            sys.stdout.write("""
What is the missing number ?
  ___     ___         _        _  _                  ___  
 |__ \   / _ \       (_)      | || |      ______    |__ \ 
    ) | | (_) |    _______    | || |_    |______|      ) |
   / /   \__, |   |_______|   |__   _|    ______      / / 
  / /_     / /        _          | |     |______|    |_|  
 |____|   /_/        (_)         |_|                 (_)  
""")

            correct_answer_divisionList(7.25)
            sys.stdout.write("""
**********************************************************************************
Make sure to Check your Score at option [6] 
**********************************************************************************

""")
            # This elif stament was used in order to provide the write output in the instance tha the user provided it with the correct input.
        elif choice == "6":
            totalScore = int(len(oddOrEvenCorrectList)) + int(len(additiontList)) + \
                int(len(subtractionList)) + \
                int(len(multiplicationlList)) + int(len(divisionList))
            sys.stdout.write("""*************SCORE*************

        '._==_==_=_.'   
        .-\:      /-.   
       | (|:.     |) |  
        '-|:.     |-'   
          \::.    /    
           '::. .'     
             ) (       
           _.' '._     
          `\"\"\"\"\"\"\"`   

[1] ODD or EVEN: """ + str(len(oddOrEvenCorrectList)) + """
[2] + Addition: """ + str(len(additiontList)) + """
[3] - Subtraction: """ + str(len(subtractionList)) + """
[4] X Multiplication: """ + str(len(multiplicationlList)) + """
[4] X Multiplication: """ + str(len(divisionList)) + """
          Total score: """ + str(totalScore) + """

*************SCORE*************\n\n""")
            # This elif stament was used in order to provide the write output in the instance tha the user provided it with the correct input.
            # It is also the elif that breaks the while loop and ends the program.
            # A break was used instead of an exit as it is more intuitive
        elif choice == "7":

            sys.stdout.write("""
  _______ _                 _                          _  _           _             _             
 |__   __| |               | |                        | || |         | |           (_)            
    | |  | |__   __ _ _ __ | | __  _   _  ___  _   _  | || |_   _ __ | | __ _ _   _ _ _ __   __ _ 
    | |  | '_ \ / _` | '_ \| |/ / | | | |/ _ \| | | | |__   _| | '_ \| |/ _` | | | | | '_ \ / _` |
    | |  | | | | (_| | | | |   <  | |_| | (_) | |_| |    | |   | |_) | | (_| | |_| | | | | | (_| |
    |_|  |_| |_|\__,_|_| |_|_|\_\  \__, |\___/ \__,_|    |_|   | .__/|_|\__,_|\__, |_|_| |_|\__, |
                                    __/ |                      | |             __/ |         __/ |
                                   |___/                       |_|            |___/         |___/ 
See you next time...!!!!
""")
            break
        # This else stament was used to accomodate for any other input that the user might provide other then the allowed input.
        else:
            sys.stdout.write("""
**********************************************************************************
Please enter a valid choice: ex. 1, 2, 3, 4, 5, 6, 7 
**********************************************************************************

""")


main()
