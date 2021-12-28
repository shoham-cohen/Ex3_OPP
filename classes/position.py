import string


class position:
    x = 0.0
    y = 0.0
    z = 0.0

    def __init__(self, str: string):
        listofposition = str.split(",")
        self.x = listofposition[0]
        self.y = listofposition[1]
        self.z = listofposition[2]
