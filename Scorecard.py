class Scorecard:
    unknown = -1

    def __init__(self, players, people, weapons, rooms):
        self.people_matrix = dict()
        self.init_people_matrix(players, people)

        self.weapons_matrix = dict()
        self.init_weapons_matrix(players, weapons)

        self.rooms_matrix = dict()
        self.init_rooms_matrix(players, rooms)


    def init_people_matrix(self, players, people):
        for player in players:
            self.people_matrix[player] = dict()
            for person in people:
                self.people_matrix[player][person] = Scorecard.unknown


    def init_weapons_matrix(self, players, weapons):
        for player in players:
            self.weapons_matrix[player] = dict()
            for weapon in weapons:
                self.weapons_matrix[player][weapon] = Scorecard.unknown


    def init_rooms_matrix(self, players, rooms):
        for player in players:
            self.rooms_matrix[player] = dict()
            for room in rooms:
                self.rooms_matrix[player][room] = Scorecard.unknown


    def update_card(self, player, card, value):
        match card.type:
            case "Person":
                self.people_matrix[player][card] = value
            case "Weapon":
                self.weapons_matrix[player][card] = value
            case "Room":
                self.rooms_matrix[player][card] = value
            case _:
                pass


    # Getters and Setters
    def get_people_matrix(self):
        return self.people_matrix


    def get_weapons_matrix(self):
        return self.weapons_matrix


    def get_rooms_matrix(self):
        return self.rooms_matrix
