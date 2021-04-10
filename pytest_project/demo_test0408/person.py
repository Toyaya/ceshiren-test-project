class Father:
    def make_computer(self):
        print("make")


class Person(Father):

    def get_name(self):
        return "hogwarts"

    @classmethod
    def get_age(cls):
        return 100


print(Person().get_name())
Person.get_age()
Person().make_computer()
