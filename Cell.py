class Cell:
    def __init__(self):
        self.status = "Dead"

    def set_dead(self):
        self.status = "Dead"
        return self.status

    def set_alive(self):
        self.status = "Alive"
        return self.status

    def is_alive(self):
        if self.status == "Alive":
            return True
        else:
            return False
