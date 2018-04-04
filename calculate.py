#!/usr/bin/env python2.7
import readline
import random

white = '\033[1;97m'
green = '\033[1;32m'
red = '\033[1;31m'
yellow = '\033[1;33m'
end = '\033[1;m'
important = '\033[35m[*]\033[1;m '
hardreturn = '\n'
info = '\033[1;33m[!]\033[1;m '
que = '\033[1;34m[?]\033[1;m '
bad = '\033[1;31m[-]\033[1;m '
good = '\033[1;32m[+]\033[1;m '
run = '\033[1;97m[~]\033[1;m '

valid_mirrors = ["converging", "diverging", "concave", "convex"]
YES = ["yes", "yup", "yeah", "ya", "sure", "affirmative"]
NO = ["no", "nope", "never", "not really", "negative"]


def get_random_no():
    return random.choice(NO).title()


def get_random_yes():
    return random.choice(YES).title()


def complete_mirrors(text, state):
    for cmd in valid_mirrors:
        if cmd.startswith(text):
            if not state:
                return cmd
            else:
                state -= 1


def get_length_object_mirror():
    try:
        return int(raw_input(que + "What is the distance between the object and the mirror? "))
    except ValueError:
        print(bad + "Invalid Object Length")
        return get_length_object_mirror()


def get_length_focal_point():
    try:
        return int(raw_input(que + "What is the length from the mirror to the focal point? "))
    except ValueError:
        print(bad + "Invalid Focal Length")
        return get_length_focal_point()


def get_type_of_mirror_lense():
    readline.parse_and_bind("tab: complete")
    readline.set_completer(complete_mirrors)
    response = raw_input(que + "What type of mirror/lense? ").strip()
    if response in valid_mirrors:
        return response
    else:
        print(bad + "Invalid Mirror Type")
        return get_type_of_mirror_lense()


def calculate_concave(length_object_mirror, length_focal_point):
    calculation = []
    if length_focal_point * 2 < length_object_mirror:
        calculation.append(get_random_yes())  # Real?
        calculation.append(get_random_no())  # Erected?
        calculation.append(get_random_yes())  # Magnification?
    elif length_focal_point * 2 == length_object_mirror:
        calculation.append(get_random_yes())  # Real?
        calculation.append(get_random_no())  # Erected?
        calculation.append(get_random_no())  # Magnification?
    elif length_focal_point * 2 > length_object_mirror and length_object_mirror > length_focal_point:
        calculation.append(get_random_no())  # Real?
        calculation.append(get_random_yes())  # Erected?
        calculation.append(get_random_yes())  # Magnification?
    elif length_object_mirror == length_focal_point:
        print(bad + "No Image")
        exit(0)
    elif length_focal_point > length_object_mirror:
        calculation.append(get_random_no())  # Real?
        calculation.append(get_random_yes())  # Erected?
        calculation.append(get_random_yes())  # Magnification?
    return calculation


def calculate_diverging_convex(length_object_mirror, length_focal_point):
    calculation = []
    calculation.append(get_random_no())  # Real?
    calculation.append(get_random_yes())  # Erected?
    calculation.append(get_random_yes())  # Magnification?
    return calculation


def calculate_converging(length_object_mirror, length_focal_point):
    calculation = []
    if length_focal_point * 2 < length_object_mirror:
        calculation.append(get_random_yes())  # Real?
        calculation.append(get_random_no())  # Erected?
        calculation.append(get_random_yes())  # Magnification?
    elif length_focal_point * 2 == length_object_mirror:
        calculation.append(get_random_yes())  # Real?
        calculation.append(get_random_no())  # Erected?
        calculation.append(get_random_no())  # Magnification?
    elif length_focal_point * 2 > length_object_mirror and length_object_mirror > length_focal_point:
        calculation.append(get_random_yes())  # Real?
        calculation.append(get_random_no())  # Erected?
        calculation.append(get_random_yes())  # Magnification?
    elif length_object_mirror == length_focal_point:
        print(bad + "No Image")
        exit(0)
    elif length_focal_point > length_object_mirror:
        calculation.append(get_random_no())  # Real?
        calculation.append(get_random_yes())  # Erected?
        calculation.append(get_random_yes())  # Magnification?
    return calculation


def calculate():
    try:
        length_object_mirror = get_length_object_mirror()
        length_focal_point = get_length_focal_point()
        type_of_mirror_lense = get_type_of_mirror_lense()
        if type_of_mirror_lense == "concave":
            return calculate_concave(length_object_mirror, length_focal_point)
        elif type_of_mirror_lense == "convex" or type_of_mirror_lense == "diverging":
            return calculate_diverging_convex(length_object_mirror, length_focal_point)
        elif type_of_mirror_lense == "converging":
            return calculate_converging(length_object_mirror, length_focal_point)
        else:
            print(bad + "Could not calculate")
            exit(1)
    except KeyboardInterrupt:
        print(bad + "Finishing...")
        exit(0)


calculation = calculate()
print(hardreturn)
print(good + "Real: " + calculation[0])
print(good + "Erected: " + calculation[1])
print(good + "Magnification: " + calculation[2])
