import pprint

from Classes import GetGenre, Genius, Event
import queue


all_songs = []

stop_event = Event()
queue = queue.Queue()

genres_list = []
genius_list = []

for _ in range(10):
    genre = GetGenre(queue, stop_event)
    genre.start()
    genres_list.append(genre)

for _ in range(10):
    genius = Genius(queue, all_songs)
    genius.start()
    genius_list.append(genius)

for genius in genius_list:
    genius.join()

stop_event.set()

print(queue.qsize())
pprint.pprint((all_songs))
print(len(all_songs))