class Port:
    name = ""
    type = ""
    size = 0
    direction = ""

    def __init__(self, name, direction, size, type):
        self.name = name
        self.type = type
        self.direction = direction
        self.size = size