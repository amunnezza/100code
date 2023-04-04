""" ho errore perche alcuni post non hanno like e quindi mi da un KeyError
    la soluzsione semplicemtente e catturare except e mettere in questo caso un like
    pari a 0 """
facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        #post['Likes'] = 0
        pass


print(total_likes)