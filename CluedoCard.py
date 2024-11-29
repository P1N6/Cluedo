class CluedoCard:
    def __init__(self, name):
        self.guilty = False
        self.name = name


    # Getters and Setters
    def set_guilty(self):
        self.guilty = True


    def is_guilty(self):
        return self.guilty


    def get_name(self):
        return self.name
