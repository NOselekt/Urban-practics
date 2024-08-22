def all_variants(text: str):
    for start in range(len(text)):
        for end in range(start, len(text)):
            yield text[start: end + 1]

for i in all_variants('abcd'):
    print(i)