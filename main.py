class Tom:
    strength = 170
    stamina = 100
    health = 60


class Anna(Tom):
    health = 100


class Jim(Anna):
    strength = 230

    def __init__(self):
        print(self.strength)
        print(self.stamina)
        print(self.health)


jim = Jim()
