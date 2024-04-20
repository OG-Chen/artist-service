import requests


def test_get_all_artists(url: str):
    res = requests.get(url).json()
    assert (res == [{'artists_id': 1,
                     'name': 'Kany West',
                     'age': '47',
                     'auditions': '1 billion',
                     'genre': 'rap, R&B, electronic, gospel'},
                    {'artists_id': 2,
                     'name': 'Валерий Меладзе',
                     'age': '58',
                     'auditions': '45 millions',
                     'genre': 'поп, рок, эстрадная песня'},
                    {'artists_id': 3,
                     'name': 'Billie Eilish',
                     'age': '22',
                     'auditions': '300 millions',
                     'genre': 'rap, pop'},
                    {'artists_id': 4,
                     'name': 'The Weeknd',
                     'age': '34',
                     'auditions': '700 millions',
                     'genre': 'rap, R&B'},
                    {'artists_id': 5,
                     'name': 'Eminem',
                     'age': '51',
                     'auditions': '1 billion',
                     'genre': 'rap, hip-hop'}])


def test_get_artist_by_id(url: str):
    res = requests.get(url).json()
    assert (res == {'artists_id': 1,
                    'name': 'Kany West',
                    'age': '47',
                    'auditions': '1 billion',
                    'genre': 'rap, R&B, electronic, gospel'})


if __name__ == '__main__':
    URL = 'http://127.0.0.1:80/api/v1/artists/'
    test_get_artist_by_id(URL + '1')
    test_get_all_artists(URL)
