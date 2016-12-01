class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_btday = Song(["Happy birthday to you", "I don't want to get sued", "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family", "With pockets full of shells"])

all_my_life = Song(["All my life I've been searching for something", "Something never comes never leads to nothing", "Nothing satisfies but I'm getting close", "Closer to the prize at the end of the rope"])

happy_btday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
all_my_life.sing_me_a_song()
