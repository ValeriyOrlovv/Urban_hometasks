calls = 0

def count_call(calls=calls) -> int:
    """Подсчитывает значение переменной calls."""
    calls += 1  


def string_info(string: str) -> tuple:
    count_call()
    return (len(string), string.upper(), string.lower())


def is_contains(string: str, list_to_search: list) -> bool:
    count_call()
    if string in list_to_search:
        return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
