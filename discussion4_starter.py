class Rectangle():

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "A rectangle with width " + str(self.width) + " and height " + str(self.height)

    # def verify_input(self):
    #     if self.width > 0 and self.height > 0:
    #         return True
    #     else:
    #         return False
        
    # def area(self):
    #     if self.verify_input() == True:
    #         return self.width * self.height
    #     else:
    #         return "Invalid input"

    # def perimeter(self):
    #     if self.verify_input() == False:
    #         return "Invalid input"
    #     else:
    #         perimeter = 2 * (self.width + self.height)
    #         return perimeter


def main():
    r = Rectangle(10, 10)
    print(r)
    print("Area:", r.area())
    print("Perimeter:", r.perimeter())
    print()

    r = Rectangle(0, 10)
    print(r)
    print("Area:", r.area())
    print("Perimeter:", r.perimeter())
    print()

if __name__ == "__main__":
    main()