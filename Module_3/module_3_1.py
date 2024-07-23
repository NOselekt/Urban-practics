import random

calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string = ''):
    count_calls()
    result = (string, len(string), string.upper(), string.lower())
    return result

def is_contains(string = '', list_ = []):
    count_calls()
    string.lower()
    if string in list_:
        return True
    return False


for i in range(random.randrange(100)):
    random_string = 'd' * random.randrange(10) + 'r' * random.randrange(10) + \
                    'e' * random.randrange(10) + \
                    'a' * random.randrange(10) + 'm' * random.randrange(10)
    print(string_info(random_string))
    list_global = [set(random_string), set(random_string.upper()), set(random_string.lower())]
    print(is_contains(random_string, list_global))


print(calls)




