import time

class User:

    def __init__(self, nickname, password, age):
        self.__nickname = nickname
        self.__password = hash(password)
        self.__age = age

    def get_nickname(self):
        return self.__nickname

    def get_password(self):
        return self.__password

    def get_age(self):
        return self.__age


class Video:

    def __init__(self, title = '', duration = 0, adult_mode = False):
        self._title = title
        self._duration = duration
        self._adult_mode = adult_mode
        self._time_stop = 0

    def get_title(self):
        return self._title

    def get_duration(self):
        return self._duration

    def get_time_stop(self):
        return self._time_stop

    def get_adult_mode(self):
        return self._adult_mode

    def set_time_stop(self, time):
        if time >= 0:
            self._time_stop = time
            return 0
        return 1


class UrTube:
    __users = []
    __videos = []
    __current_user = None

    def register(self, nickname, password, age):
        for i in self.__users:
            if nickname == i.get_nickname():
                print('There\'s already a user with such nickname, please choose another one.')
        newbie = User(nickname, password, age)
        self.__users.append(newbie)
        self.__current_user = newbie.get_nickname()
        print('Welcome to UrTube!')

    def log_in(self, nickname, password):
        password = hash(password)
        for i in self.__users:
            if nickname == i.get_nickname() and password == i.get_password():
                self.__current_user = i
                print('Nice to see you again!')
        print('Either nickname or password are incorrect, please check them again or register.')

    def log_out(self):
        self.__current_user = None

    def add(self, *videos):
        if self.__videos:
            for i in videos:
                for j in self.__videos:
                    if i.get_title().lower() != j.get_title().lower():
                        self.__videos.append(i)
        else:
            for i in videos:
                self.__videos.append(i)

    def get_videos(self, key_word):
        key_word = key_word.lower()
        found_videos = []
        for i in self.__videos:
            if key_word in i.get_title().lower():
                found_videos.append(i.get_title())
        return found_videos

    def watch_video(self, title):
        title = title.lower()
        for i in self.__videos:
            tit = i.get_title().lower()
            if title == i.get_title().lower():
                for j in range(1, i.get_duration() + 1):
                    print(j)
                    time.sleep(1)

    def get_current_user(self):
        return self.__current_user