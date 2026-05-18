class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

p1 = person("Adil", 18)
print(p1.name)
print(p1.get_age())