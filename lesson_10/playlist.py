class Playlist:
    def __init__(self,playlist_name,genre):
        self.playlist_name=playlist_name
        self.genre=genre
        self.song_list=[]
    def add (self,song_name):
        self.song_list.append(song_name)
        print(f'{song_name} has been added to your playlist')
    def remove(self,song_name):
        if song_name in self.song_list:
            self.song_list.remove(song_name)
            print(f'{song_name} removed succesfully')
        else:
            print('404  song not found')
    def display(self):
        print(f'{self.playlist_name} of genre {self.genre}')
        if len(self.song_list)==0:
            print('no songs in playlist')
        else:
            for i in range(len(self.song_list)):
                print(f'song no.{i+1}: {self.song_list[i]}')
    def __del__(self):
        print(f'{self.playlist_name} has been deleted')

i=0

while True:
    dec=input('1 for new playlist, 2 for add song, 3 for remove song 4 for delete plalist 5 for display')
    if dec=='1':
        i=i+1
        p1=input('what is the playlist u want to make')
        p1g=input('what is the genre')
        playi=Playlist(p1,p1g)
    elif dec=='2':
        addsong=input('what song to add')
        addplay=input('where add song')
        play1.add


