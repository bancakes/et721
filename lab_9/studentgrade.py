"""
Delvin Gonzalez
sep 30, unit testing 'input' data
"""
def main ():
    #loop to collect number of students
    while True:
        try:
            num_studens = int(input("Enter the number of students: "))
            if num_studens >0:
                break
            else:
                print("Invalid Input. ")
        except ValueError:
            print("Invalid input. Try again")