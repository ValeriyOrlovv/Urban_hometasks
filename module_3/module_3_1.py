calls = 0

def count_calls() -> int:
    """Подсчитывает значение переменной calls."""
    global calls
    calls += 1  


def string_info(string: str) -> tuple:
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contains(string: str, list_to_search: list) -> bool:
    count_calls()
    unified_list = [line.lower() for line in list_to_search]
    if string.lower() in unified_list:
        return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
