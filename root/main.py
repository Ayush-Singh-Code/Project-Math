# Rich is a python library which help to style output

from rich.style import Style
from calculator.calculator import calculator
from rich.console import Console 
from rich.markdown import Markdown
from sequence_series.ap import mainSqSeries

console = Console()  # creating a console object




def welcome():
    message = """# WELCOME TO PROJECT-MATH1

       What operation do you want to perform:
      1. Sequence and Series
      2. Complex Number
      3. Basic Calculator
      4. Finding the value of trignometric ratio

    Please select operation from '1' '2' '3' or '4'
    """
    resultMsg = Markdown(message)
    console.print(resultMsg)
    

welcome()



def selection():
    choice = input(">> Enter your choice: ")
    print("")
    console.rule("")
    print("")

    if choice == '1':
        print("")         # these print are written to give space between line
        mainSqSeries()
    elif choice == '2':
        print("")
        print("Working2")
    elif choice == '3':
        print("")
        calculator()
    elif choice == '4':
        print("")
        print("Working4")
    else:
        console.print("Please Enter a valid input", style="Red on black")

selection()









