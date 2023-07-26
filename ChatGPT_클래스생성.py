class Person:
    def __init__(self, id, name, phoneNumber):
        self.id = id
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Phone Number: {self.phoneNumber}")


class Manager(Person):
    def __init__(self, id, name, phoneNumber, skill):
        super().__init__(id, name, phoneNumber)
        self.skill = skill

    def printInfo(self):
        super().printInfo()
        print(f"Skill: {self.skill}")


class Employee(Person):
    def __init__(self, id, name, phoneNumber, title):
        super().__init__(id, name, phoneNumber)
        self.title = title

    def printInfo(self):
        super().printInfo()
        print(f"Title: {self.title}")


# Testing the classes
if __name__ == "__main__":
    # Test case 1
    person1 = Person(1, "John Doe", "123-456-7890")
    person1.printInfo()

    # Test case 2
    manager1 = Manager(2, "Alice Smith", "987-654-3210", "Leadership")
    manager1.printInfo()

    # Test case 3
    employee1 = Employee(3, "Bob Johnson", "555-555-5555", "Software Engineer")
    employee1.printInfo()

    # Test case 4
    person2 = Person(4, "Jane Doe", "111-222-3333")
    person2.printInfo()

    # Test case 5
    manager2 = Manager(5, "Eve Brown", "444-555-6666", "Problem-solving")
    manager2.printInfo()

    # Test case 6
    employee2 = Employee(6, "Chris White", "777-888-9999", "Data Analyst")
    employee2.printInfo()

    # Test case 7
    person3 = Person(7, "Sam Smith", "222-333-4444")
    person3.printInfo()

    # Test case 8
    manager3 = Manager(8, "Olivia Davis", "555-666-7777", "Communication")
    manager3.printInfo()

    # Test case 9
    employee3 = Employee(9, "Alex Johnson", "888-999-0000", "Web Developer")
    employee3.printInfo()

    # Test case 10
    person4 = Person(10, "Emily Green", "666-777-8888")
    person4.printInfo()
