# from unittest.mock import patch

# print('hussam')

# def add(a, b):
#     return a + b

import requests

def len_joke():
    joke = get_joke()
    return len(joke)    

def get_joke():
    url = 'https://api.chucknorris.io/jokes/random'
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json()['value']
    else:
        joke = "No joke"
    return joke

if __name__== '__main__':
    print(get_joke())