import Scorecard

class Player:
    def __init__(self, players, people, weapons, rooms):
        self.other_players = players
        self.other_players.remove(self)
        self.scorecard = Scorecard(players, people, weapons, rooms)


    def deal(self, card):
        self.scorecard.update_card(self, card, 100)
        for player in self.other_players:
            self.scorecard.update_card(player, card, 0)


    def suggest(self, person, weapon, room):
        pass
