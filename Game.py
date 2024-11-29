import Player
import PersonCard
import WeaponCard
import RoomCard

class Game:
    def __init__(self, players, people, weapons, rooms):
        self.players = {}
        self.people = {}
        self.weapons = {}
        self.rooms = {}
