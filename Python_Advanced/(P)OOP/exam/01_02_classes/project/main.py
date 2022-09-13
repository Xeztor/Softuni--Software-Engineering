from project.controller import Controller
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish


def test():
    controller = Controller()
    print(controller.add_aquarium('FreshwaterAquarium', 'fresh'))
    print(controller.add_aquarium('SaltwaterAquarium', 'salty'))
    for i in range(0):
        print(controller.add_fish('fresh', 'FreshwaterFish', 'goshko', 'golemizubi', 10))
    print(controller.feed_fish('fresh'))
    print(controller.add_decoration('Plant'))
    print(controller.insert_decoration('fresh', 'Plant'))
    # print(controller.add_decoration('Plant'))
    print(controller.insert_decoration('salty', 'Plant'))
    print(controller.report())


if __name__ == '__main__':
    test()
