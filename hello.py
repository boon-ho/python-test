from random import choices


def with_input(color):

    words = ["red", "yellow", "green"]
    new_color = choices(words)[0]
    color_dict = {"old": color, "new": new_color}
    return color_dict

if __name__ == "__main__":
    print(with_input("blue"))
