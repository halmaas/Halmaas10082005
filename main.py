'''Implement a class called Player that represents a cricket player. The player class should have a
method called  play() which prints "The player is playing cricket.Derive a two classes, Batsman and 
Bowler, from the player class.overside the play() method in each derived class the print. The  batsman 
is batting" and "The blower is blowing",respectively.Write a program to create subjects or both the
Batsman and Bowler classes and call the play() method for each object.'''


# Define the base class Player
class Player:
    def play(self):
     print("The player is playing cricket.")

# define the derived class Batsman 
class Batsman(Player):
    def play(self):
      print("The batsman is batting .")

# define the derived class Bowler
class Bowler(Player):
    def play(self):
      print("The bowler is bowling.")

# create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# call the play() method for each object 
batsman.play()
bowler.play()