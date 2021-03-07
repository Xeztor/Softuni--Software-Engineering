class Zoo:
    animal_types = ['Lion', 'Tiger', 'Cheetah']
    workers_types = ['Keeper', 'Caretaker', 'Vet']

    def __init__(self, name, budget, animlal_capacity, workers_capacity):
        self.name = name
        self.animals = []
        self.workers = []
        self.__budget = budget
        self.__animal_capacity = animlal_capacity
        self.__workers_capacity = workers_capacity

    def add_animal(self, animal, price):
        if self.__budget < price:
            return "Not enough budget"

        if not self.left_space_animals():
            return "Not enough space for animal"

        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {type(animal).__name__} added to the zoo"

    def hire_worker(self, worker):
        if not self.left_space_workers():
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {type(worker).__name__} hired successfully"

    def fire_worker(self, worker_name):
        worker = self.worker_exist(worker_name)
        if not worker:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        all_workers_salaries = sum([worker.salary for worker in self.workers])
        if self.__budget < all_workers_salaries:
            return "You have no budget to pay your workers. They are unhappy"
        
        self.__budget -= all_workers_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"
    
    def tend_animals(self):
        all_animals_cost = sum([animal.tend_cost for animal in self.animals])
        if self.__budget < all_animals_cost:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= all_animals_cost
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        res = f'You have {len(self.animals)} animals\n'
        for animal_class_name in Zoo.animal_types:
            res += self.get_animal_info_by_classname(animal_class_name)

        return res[:-1]

    def workers_status(self):
        res = f"You have {len(self.workers)} workers\n"
        for worker_class in Zoo.workers_types:
            res += self.get_worker_info_by_classname(worker_class)

        return res[:-1]

    def get_animal_info_by_classname(self, classname):
        animals_of_class = []
        for animal in self.animals:
            if type(animal).__name__ == classname:
                animals_of_class.append(animal)

        animals_info = '\n'.join([str(animal) for animal in animals_of_class]) + '\n'
        return f'----- {len(animals_of_class)} {classname}s:\n' + animals_info

    def get_worker_info_by_classname(self, classname):
        workers_of_class = []
        for worker in self.workers:
            if type(worker).__name__ == classname:
                workers_of_class.append(worker)

        animals_info = '\n'.join([str(worker) for worker in workers_of_class]) + '\n'
        return f'----- {len(workers_of_class)} {classname}s:\n' + animals_info

    def left_space_animals(self):
        return len(self.animals) < self.__animal_capacity

    def left_space_workers(self):
        return len(self.workers) < self.__workers_capacity

    def worker_exist(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                return worker
