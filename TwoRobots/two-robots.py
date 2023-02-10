class Robot(object):
    def __init__(self, name, color, weight):
        self.name=name;
        self.color=color;
        self.weight=weight;
    def introduceSelf(self):
        print("My name is " + self.name)

Robot("Tom", "Red", "30")
Robot("Jerry", "Blue", "30")