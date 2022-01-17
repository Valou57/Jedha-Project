import math

TEST

class maths():

    def squareroot(self, number):
        result = math.sqrt(number)
        print("the square root of is", number, "is", result)

    def avg(self, number):
        result = math.avg(number)
        print("the avg of", number, "is", result)

    def oddornot(self, number):
        if (number % 2) == 0:
            print("{0} is Even".format(number))
        else:
            print("{0} is Odd".format(number))

    def sumlist(self, number):
        result = sum(number)
        print("the sum of", number, "is", result)

    def sumlist2(self, number):
        result = 0
        for i in number:
            result = result + i
        print("the sum of", number, "is", result)






    def fillnone2(self, number):
        result = [x for x in number if x is not None]
        avg_value = sum(result) / len(result)
        result2 = [avg_value if x is None else x for x in number]
        print(result2)


calcul = maths()
calcul.fillnone2([2, None, 4, None, 6])
