movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
            ["Graham Chapman", ["Michael Palin", "John Cleese",
                "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

"""This is the “nester.py" module, and it provides one function called
print_lol() which prints lists that may or may not include nested lists"""
def print_list(the_list):
    """This is the “nester.py" module, and it provides one function called
    print_lol() which prints lists that may or may not include nested lists."""
    for each_item in the_list:
        if isinstance(each_item,list):
            print_list(each_item)
        else:
            print(each_item)