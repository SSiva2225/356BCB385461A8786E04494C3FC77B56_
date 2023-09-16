class player:
  def player(self):
    print ('the player is playing cricket.')
class Batsman(player):
  def player(self):
    print('the batsman is batting.')
class Bowler(player):
  def player(self):
    print('the bowler is bowling.')
batsman = Batsman()
bowler = Bowler()

batsman.player()
bowler.player()
