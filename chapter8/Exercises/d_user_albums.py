def make_album(artist_name, album_title, number_of_songs = None):
    """Builds and returns a dictionary about a music album"""
    
    if number_of_songs:
        music_album = {"name": artist_name.title(), "title": album_title.title(), "number of songs": number_of_songs}
    else: 
        music_album = {"name": artist_name.title(), "title": album_title.title()}

    
    return music_album

print(make_album("kendrick lamar", "damn"))
print(make_album("capitol hill baptis church", "the dead's alive", 26))
print(make_album("timothy brindle", "killing sin"))