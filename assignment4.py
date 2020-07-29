# task 1.1

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.area = 0

    def fnd_area(self):
        s = (self.a+self.b+self.c)/2
        self.area = s*((s-self.a)*(s-self.b)*(s-self.c))**0.5
        return self.area
   
from Triangle import Triangle
T1 = Triangle(10, 15, 16)
print(T1.fnd_area())


# task 1.2

lsst = ('asda', 'ashgdfasg', 'asjfgjks', 'as', 'asdfg')


def filter_long_words(lst, number):
    final_list = list()
    for elements in lst:
        if len(elements) > number:
            final_list.append(elements)
    print(final_list)


filter_long_words(lsst, 5)

# task 2.1


def len_words(lst):
    final_lst = [int(len(x)) for x in lst]
    print(final_lst)


len_words(lsst)

# task 2.2


def vowel_check(letter):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    if letter in vowels:
        print("True")
    else:
        print("False")