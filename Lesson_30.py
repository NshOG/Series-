class Person:
    def __init__(self, initials, age, passport, weight):
        if self.isvalid_name(initials) and self.isvalid_age(age) and self.isvalid_passport(passport) and \
                self.isvalid_weight(weight):
            self.__initials = initials
            self.__age = age
            self.__passport = passport
            self.__weight = weight
            print("data filled")
        else:
            raise ValueError("incorrect info")

    @staticmethod
    def isvalid_name(l):
        return type(l) is list and len(l) == 3 and 

    @staticmethod
    def isvalid_age(age):
        return type(age) is int and 14 <= age <= 65

    @staticmethod
    def isvalid_passport(passport):
        return (passport[0:4] + passport[5:]).isdigit() and len(passport) == 11 and passport[4] == " "

    @staticmethod
    def isvalid_weight(weight):
        return weight >= 20 and isinstance(weight, int | float)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, x):
        if not self.isvalid_age(x):
            return ValueError("invalid age")
        else:
            self.__age = x


p = Person(["Nsho", "Gevorgyan", "Tigranovich"], 25, "4567 778899", 70)
print(p.age)


