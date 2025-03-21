class CricketTeam:
    total_run = 0   # static/class variable

    def __init__(self, run):
        self.Run = run      # instance variable

    def hit_four(self):
        self.Run += 4
        CricketTeam.total_run += 4

    def hit_six(self):
        self.Run += 6
        CricketTeam.total_run += 6


pl1 = CricketTeam(0)
pl1.hit_four()
pl1.hit_four()
pl1.hit_six()
print('Player 1 run is ', pl1.Run)
pl2 = CricketTeam(0)
pl2.hit_four()
pl2.hit_six()
print('Player 2 run is ', pl2.Run)

print('Team run is ', CricketTeam.total_run)
