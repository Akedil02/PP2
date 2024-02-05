class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print("String in upper case:", self.input_string.upper())

# Example of using the class
string_manipulator = StringManipulator()
string_manipulator.getString()
string_manipulator.printString()
