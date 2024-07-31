import time

class User:

    def __init__(self, nickname, password, age):
        self.__nickname = nickname
        self.__password = hash(password)
        self.__age = age
        if age >= 18:
            self.__is_adult = True
        else:
            self.__is_adult = False

    def _get_nickname(self):
        return self.__nickname

    def get_password(self):
        return self.__password

    def get_age(self):
        return self.__age

    def is_adult(self):
        return self.__is_adult


class Video:

    def __init__(self, title = '', duration = 0, adult_mode = False):
        self._title = title
        self._duration = duration
        self._adult_mode = adult_mode
        self.time_stop = 0

    def get_title(self):
        return self._title

    def get_duration(self):
        return self._duration


    def get_adult_mode(self):
        return self._adult_mode



class UrTube:
    __users = {}
    __videos = {}
    __current_user = None

    def register(self, nickname, password, age):
        if self.__users.get(nickname):
            print('There\'s already a user with such nickname, please choose another one.')
        else:
            self.__users[nickname] = User(nickname, password, age)
            self.__current_user = nickname
            print('Welcome to UrTube!')

    def log_in(self, nickname, password):
        password = hash(password)
        user = self.__users.get(nickname)
        if user and user.get_password() == password:
            self.__current_user = nickname
            print('Nice to see you again!')
        else:
            print('Either nickname or password are incorrect, please check them again or register.')

    def log_out(self):
        self.__current_user = None
        print('Goodbye!')

    def add(self, *videos):
        for i in videos:
            title = i.get_title().lower()
            if not self.__videos.get(title):
                self.__videos[title] = i

    def get_videos(self, key_word):
        key_word = key_word.lower()
        found_videos = []
        for i in self.__videos.keys():
            if key_word in i:
                found_videos.append(self.__videos[i].get_title())
        return found_videos

    def watch_video(self, title):
        if self.__current_user:
            title = title.lower()
            video = self.__videos.get(title)
            if video:
                if not video.get_adult_mode() or \
                        (video.get_adult_mode() and self.__users[self.__current_user].is_adult()):
                    for i in range(1, video.get_duration() + 1):
                        video.time_stop = i
                        print(i)
                        time.sleep(1)
                else:
                    print('You are under 18, so you can\'t watch the video.')
        else:
            print('Please, log in to watch videos.')

    def get_current_user(self):
        return self.__current_user