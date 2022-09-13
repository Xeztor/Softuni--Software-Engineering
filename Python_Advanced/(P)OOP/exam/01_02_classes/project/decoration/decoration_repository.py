from project.mappers import DECORATIONS_CLASSES_NAMES_MAPPER


class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration not in self.decorations:
            return False

        self.decorations.remove(decoration)
        return True

    def find_by_type(self, decoration_type):
        if decoration_type in DECORATIONS_CLASSES_NAMES_MAPPER:
            desired_type = DECORATIONS_CLASSES_NAMES_MAPPER[decoration_type]
        else:
            return "None"

        for decoration in self.decorations:
            if type(decoration) is desired_type:
                return decoration

        return "None"
