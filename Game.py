import Player
import PersonCard
import WeaponCard
import RoomCard
import Scorecard

import random

class Game:
    def __init__(self, player_count, people_count, weapon_count, room_count):
        self.players = list()
        self.people = list()
        self.weapons = list()
        self.rooms = list()

        self.init_people(people_count)
        self.init_weapons(weapon_count)
        self.init_rooms(room_count)
        self.init_players(player_count)

        self.common_knowledge = Scorecard(self.players, self.people, self.weapons, self.rooms)


    def init_players(self, player_count):
        for i in range(player_count):
            name = "Player " + i
            self.players.append(Player(name))


    def init_people(self, people_count):
        for i in range(people_count):
            name = "P" + i
            self.people.append(PersonCard(name))
        self.people[random.randint(0, people_count - 1)].set_guilty()


    def init_weapons(self, weapon_count):
        for i in range(weapon_count):
            name = "W" + i
            self.weapons.append(WeaponCard(name))
        self.weapons[random.randint(0, weapon_count - 1)].set_guilty()


    def init_rooms(self, room_count):
        for i in range(room_count):
            name = "R" + i
            self.rooms.append(RoomCard(name))
        self.rooms[random.randint(0, room_count - 1)].set_guilty()


    # Getters and Setters
    def get_players(self):
        return self.players


    def get_people(self):
        return self.people


    def get_weapons(self):
        return self.people


    def get_rooms(self):
        return self.rooms
