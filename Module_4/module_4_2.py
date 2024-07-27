def test_function():
    result = 0
    def inner_function():
        print('I\'m in the test_function\'s scope!')
        nonlocal result
        if __name__ != '__main__':
            result = 1
    inner_function()
    return result

#inner_fuction() - Error

print(test_function())