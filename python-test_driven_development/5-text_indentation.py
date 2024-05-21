#!/usr/bin/python3
"""  """


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    jumpers = [".", "?", ":"]
    new_txt = ""
    no_space = False
    for char in text:
        if char in jumpers:
            new_txt += char + "\n\n"
            no_space = True
        else:
            if no_space and char == " ":
                continue
            new_txt += char
            skip_space = False
    print(new_txt)



