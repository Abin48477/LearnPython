class Playlist:
    def __init__(self,name):
        self.name = name
        self.songs = []

    def add_song(self,song):
        self.songs.append(song)
        print(f"{song} is Added")

    def remove_song(self, song):
        self.songs.remove(song)
        print(f"{song} is removed.")

    def show_song(self):
        print(f"Playlist '{self.name}")
        for song in self.songs:
            print(f"- {song}")

p1 = Playlist("my_fevbrate")
p1.add_song("hare krishna song")
p1.add_song("kritan mela")
del Playlist.remove_song
p1.show_song()
p1.remove_song("kritan mela")




# delete methods
# using the del keyword

            