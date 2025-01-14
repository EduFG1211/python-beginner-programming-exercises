import random

def get_color(color_number=4):
    # making sure is a number and not a string
    color_number = int(color_number)

    switcher={
                  0:'red',
                  1:'yellow',
                  2:'blue',
                  3:'green',
                  4:'black'
              }
    return switcher.get(color_number,"Invalid Color Number")


def get_allStudentColors():

    example_color = 1
    students_array = []
    #your loop here
    for i in range(0,10,1):
        colorNum = random.randint(0,4)
        students_array.append(colorNum)
    colorList = list(map(get_color,students_array))
    return colorList


print(get_allStudentColors())