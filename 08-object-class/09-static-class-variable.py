class Player:
    counter = 0

    def __init__(self, ply_id, name, age):
        self.Ply_Id = ply_id
        self.Name = name
        self.Age = age
        Player.counter += 1

    def details(self):
        # Player.counter += 1
        print('Id: ', self.Ply_Id, 'Name: ', self.Name, 'Age: ', self.Age)


print('Total player', Player.counter)
pl1 = Player(101, 'Jakir', 35)
pl2 = Player(101, 'Jakir', 35)
pl1.details()
print('Total Player is ', Player.counter)
