anime_list = [
    {"title": "One Piece", "volumes": 108},
    {"title": "AOT", "volumes": 34},
    {"title": "One Punch Man", "volumes": 30}
]

for index, anime in enumerate(anime_list):
    print(f"{index}: {anime['title']} - {anime['volumes']} volumes")