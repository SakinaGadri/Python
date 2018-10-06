#this function takes 3 parameters and returns a string.
def useless (param1, param2, param3):
    sentence = 'That was a waste of time'
    return sentence

#this function squares the input number and returns the answer
def square_me (param1):
    squaredNumber = param1**2
    return squaredNumber

#this function takes student data and displays it as a string
def student_data (tag, number, student_id, enlisted):
    name = str(tag)
    age = str (number)
    student_number = str(student_id)
    enrolled = str (enlisted)
    order = "<" + student_number + "," + name + "," + age + "," + enrolled + ">"
    return order
    