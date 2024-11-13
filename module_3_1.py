calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string=""):
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contains(string="", list_to_search=[]):
    count_calls()
    is_true = False
    for i in list_to_search:
        if i.lower() == string.lower():
            is_true = True
            break
        else:
            continue
    return is_true


print(string_info("Hello"))
print(string_info("Dreadnout"))
print(is_contains("hi", ["HI", "Ho", "Heh"]))
print(is_contains("Pineapple", ["Orange", "Melon", "Cucumber"]))
print(calls)
