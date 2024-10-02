class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_1 = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        person_instance = Person.people[person["name"]]
        if "wife" in person and person["wife"]:
            person_instance.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"]:
            person_instance.husband = Person.people[person["husband"]]
    return list_1
