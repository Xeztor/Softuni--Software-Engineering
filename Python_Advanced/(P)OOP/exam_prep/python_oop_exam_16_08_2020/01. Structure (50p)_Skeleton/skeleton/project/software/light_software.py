from project.software.software import Software


class LightSoftware(Software):
    def __init__(self, name, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, "Light", int(capacity_consumption * 1.5), memory_consumption // 2)
