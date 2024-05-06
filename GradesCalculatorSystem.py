class Grade:
    def __init__(self):
        # Initialize an empty dictionary to store subjects and grades
        self.gradeBook = {}

    def addSubjectAndGrade(self):
        # Continuously prompt the user to input subjects and grades
        while True:
            # Ask the user to enter a subject, or "exit" to stop adding subjects
            addSubject = str(input("\nEnter your Subject to be calculated, press 'exit' to start calculating : "))

            # Check if the user wants to exit
            if addSubject.lower() == "exit":
                break  # Exit the loop if the user enters "exit"

            else:
                # If not exiting, ask for the grade of the subject and store it in the dictionary
                addGrade = int(input("Enter the grade of " + addSubject + " : "))
                self.gradeBook[addSubject] = addGrade

    def displaySubjectAndGrade(self):
        # Display the subjects and corresponding grades stored in the grade book
        for subject, grade in self.gradeBook.items():
            print(f"\nSubject : {subject}\nGrade : {grade}")

    def calculateAverage(self):
        # Calculate the average grade from the grades stored in the grade book
        sumOfGrades = sum(self.gradeBook.values())
        averageGrade = sumOfGrades / len(self.gradeBook)
        
        # Wait for user confirmation before displaying the average grade
        input("\nPress Enter to see your average grade : ")
        print(f"\nAverage Grade : {averageGrade}\n")


# Instantiate the Grade class
gradesCalculatorSystem = Grade()

# Welcome message
print("Welcome to Grades Calculator System!")

# Wait for user confirmation before starting
input("Press Enter to start : ")

# Add subjects and grades
gradesCalculatorSystem.addSubjectAndGrade()

# Display subjects and grades
gradesCalculatorSystem.displaySubjectAndGrade()

# Calculate and display the average grade
gradesCalculatorSystem.calculateAverage()
