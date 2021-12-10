# class Person(object)
class Person:

    # age = 20
    # name = "Beka"
    # surname = "Junushaliev"

    def __init__(self, age, name, surname) -> None:
        self.age = self.set_age(age)
        self.name = name
        self.surname = surname

    def create(self):
        pass

    def delete(self):
        pass



    def info(self):
        print(f" Name {self.age} \n Surname {self.surname} \n Age {self.name}")

    @property
    def info111(self):
        print(f" Name {self.age} \n Surname {self.surname} \n Age {self.name}")

    @staticmethod
    def sum_of_two():
        print(2+2)

    def __str__(self):
        return self.name

    def set_age(self, age):
        print(age)
        if age < 100:
            return age
        else:
            return "invalid input"


obj = Person(20, "Az", "Ws")
print(obj.sum_of_two())
obj.name = "Aktan"
print(obj.info())
print(obj.info111)
