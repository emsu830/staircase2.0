'''
Name: Emily Su
Project: Staircase 2.0
'''
'''custom exceptions to handle edge cases'''
class IntegerOutOfRangeException(Exception):
    '''user inputs an integer less than 0 or greater than 500'''
    pass

class NoStairCaseException(Exception):
    '''user inputs a value of 0'''
    pass

class UserTermination(Exception):
    '''user requests to terminate the program'''
    pass

'''prompts user to provide the number of steps or terminate program with keyword DONE'''
def getUserInput():
    userInput = input("Please input your stair case size:")

    if userInput == "DONE":
        raise UserTermination
    
    stepCount = int(userInput)    
    return stepCount


'''
parameter: number of steps
return: string containing steps determined by parameter
raises exceptions for invalid user inputs
'''
def createSteps(stepCount):
    '''invalid integer input'''
    if stepCount < 0 or stepCount >= 500:
        raise IntegerOutOfRangeException
    if stepCount == 0:
        raise NoStairCaseException

    '''valid integer input'''
    stairs = ""
    for i in reversed(range(stepCount)):
        if i == stepCount - 1: #top of highest step
            stairs += "  " * i + "+-+\n"
        else:
            stairs += "  " * i + "+-+-+\n"
                                    
        stairs += "  " * i + "| |\n" #middle of step
                
        if i == 0: #bottom of lowest step
            stairs += "+-+"
        
    return stairs


'''
handles custom exceptions with an error message
returns an exit message if the user decides to terminate the program
'''
def runProgram():
    condition = 1
    while condition:
        try:
            condition = getUserInput()
            print(createSteps(condition))
                
        except ValueError:
            print("There are no steps in the staircase.")
        except IntegerOutOfRangeException:
            print("That staircase size is out of range.")
        except NoStairCaseException:
            print("There are no steps in the staircase.")
            condition = 1
        except UserTermination:
            break
                
    return "Done Executing"


if __name__ == "__main__": 
    print(runProgram())


