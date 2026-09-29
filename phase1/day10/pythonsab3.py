def high_rating_average(high_rating_scores):
    return sum(high_rating_scores)/len(high_rating_scores)
movies = [
    {"title": "映画A", "rating": 8.2, "genre": "action"},
    {"title": "映画B", "rating": 6.5, "genre": "comedy"},
    {"title": "映画C", "rating": 9.1, "genre": "action"},
    {"title": "映画D", "rating": 7.0, "genre": "drama"},
    {"title": "映画E", "rating": 8.7, "genre": "action"}
]
high_rating_movis=[]
high_rating_scores=[]
action_movies=[]
for movie in movies:
    title=movie["title"]
    rate=movie["rating"]
    genre=movie["genre"]
    if rate>=8.0:
        high_rating_movis.append(title)
        high_rating_scores.append(rate)
    if genre=="action":
        action_movies.append(title)
avg=high_rating_average(high_rating_scores)
print(high_rating_movis)
print(action_movies)
print(avg)
    
