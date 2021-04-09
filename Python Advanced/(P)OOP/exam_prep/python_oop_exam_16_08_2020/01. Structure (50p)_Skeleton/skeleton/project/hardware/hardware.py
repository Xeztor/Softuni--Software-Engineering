from project.software.software import Software


class Hardware:
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def __str__(self):
        return f"Hardware Component - {self.name}\n" \
               f"Express Software Components: {len([sw for sw in self.software_components if sw.type == 'Express'])}\n" \
               f"Light Software Components: {len([sw for sw in self.software_components if sw.type == 'Light'])}\n" \
               f"Memory Usage: {self.taken_memory} / {self.memory}\n" \
               f"Capacity Usage: {self.taken_capacity} / {self.capacity}\n" \
               f"Type: {self.type}\n" \
               f"Software Components: {', '.join([sw.name for sw in self.software_components]) if self.software_components else None}"

    @property
    def taken_memory(self):
        return sum([sw.memory_consumption for sw in self.software_components])

    @property
    def taken_capacity(self):
        return sum([sw.capacity_consumption for sw in self.software_components])

    def install(self, software: Software):
        if software.capacity_consumption + self.taken_capacity > self.capacity or \
                software.memory_consumption + self.taken_memory > self.memory:
            raise Exception("Software cannot be installed")

        self.software_components.append(software)

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)
