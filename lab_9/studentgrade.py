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

    #nested loop to collect h grade for each studetns
    totalsumgrade = 0
    for i in range(num_studens):
        while True:
            try:
                grade = int(input(f"Enter a grade for student {i}: "))
                if 0<= grade <=100:
                    totalsumgrade += grade
                    break
                else:
                    print("Grade must be between 0 and 100. ")
            except ValueError:
                print("Invalid input. ")

    average = totalsumgrade / num_studens
    print(f"The class average is {average:.2f}")

if __name__ == "__main__":
    main()
