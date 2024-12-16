import cmd

class GameInterface(cmd.Cmd):
    prompt = ">>"
    intro = "Welcome to Cluedo. Type 'help' for available commands."


    def create_game(self, line):
        print("boobs")


    def exit(self, line):
        return True


if __name__ == '__main__':
    GameInterface().cmdloop()
