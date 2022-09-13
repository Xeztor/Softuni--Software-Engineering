from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        new_power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(new_power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        new_heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(new_heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int,
                                  memory_consumption: int):
        hardware = System.find_component_by_name_from_components_list(hardware_name, System._hardware)
        if not hardware:
            return "Hardware does not exist"

        software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(software)
            System._software.append(software)
        except Exception as exc:
            return str(exc)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int,
                                memory_consumption: int):
        hardware = System.find_component_by_name_from_components_list(hardware_name, System._hardware)
        if not hardware:
            return "Hardware does not exist"

        software = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(software)
            System._software.append(software)
        except Exception as exc:
            return str(exc)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System.find_component_by_name_from_components_list(hardware_name, System._hardware)
        software = System.find_component_by_name_from_components_list(software_name, System._software)
        if not (hardware and software):
            return "Some of the components do not exist"

        hardware.uninstall(software)

    @staticmethod
    def analyze():
        all_memory = sum([hw.memory for hw in System._hardware])
        taken_memory = sum([hw.taken_memory for hw in System._hardware])
        all_capacity = sum([hw.capacity for hw in System._hardware])
        taken_capacity = sum([hw.taken_capacity for hw in System._hardware])
        return f"System Analysis\n" \
               f"Hardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {taken_memory} / {all_memory}\n" \
               f"Total Capacity Taken: {taken_capacity} / {all_capacity}"

    @staticmethod
    def system_split():
        res = ""
        for hw in System._hardware:
            res += str(hw)

        return res

    @staticmethod
    def find_component_by_name_from_components_list(name, components_list):
        for hw in components_list:
            if hw.name == name:
                return hw
