class Cheetah:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        self.tend_cost = 60

    @property
    def tend_cost(self):
        return self.__tend_cost

    @tend_cost.setter
    def tend_cost(self, cost):
        self.__tend_cost = cost

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

    def get_needs(self):
        return self.tend_cost
