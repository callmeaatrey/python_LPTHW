class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
happy_bday = Song(["Happy Birthday to you", "May god bless you", "Sorry, i crashed the wrong party."])

happy_bday.sing_me_a_song()