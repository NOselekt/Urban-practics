from Constants import ACCESS_TOKEN, GENIUS_API_URL, RANDOM_GENRE_API_URL, GENIUS_URL
from threading import Thread, Event
import pprint
import requests
import queue


class GetGenre(Thread):
    def __init__(self, queue: queue.Queue, stop_event: Event):
        self.queue = queue
        self.stop_event = stop_event
        super().__init__()

    def run(self):
        while not self.stop_event.is_set():
            genre = requests.get(RANDOM_GENRE_API_URL).json()
            self.queue.put(genre)


class Genius(Thread):
    def __init__(self, queue: queue.Queue, all_songs: list):
        super().__init__()
        self.queue = queue
        self.all_songs = all_songs

    def run(self):
        for _ in range(1000):
            genre = self.queue.get()
            data = requests.get(GENIUS_API_URL, params={'access_token': ACCESS_TOKEN, 'q': genre}).json()
            try:
                song_id = data['response']['hits'][0]['result']['api_path']
                self.all_songs.append(f'{GENIUS_URL + song_id}/apple_music_player')
                break
            except IndexError: ...
