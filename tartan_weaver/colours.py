# https://www.tartanregister.gov.uk/docs/Colour_shades.pdf

from .utils import TartanException

PALETTE = None

TartanColours = (
    ("LR", "Light Red", (0xE8CCB8, 0x878787, 0xEC34C4)),
    ("R", "Red"),
    ("DR", "Dark Red"),
    ("O", "Orange"),
    ("DO", "Dark Orange"),
    ("LY", "Light Yellow"),
    ("Y", "Yellow"),
    ("DY", "Dark Yellow"),
    ("LG", "Light Green"),
    ("G", "Green"),
    ("DG", "Dark Green"),
    ("LB", "Light Blue"),
    ("B", "Blue"),
    ("DB", "Dark Blue"),
    ("LP", "Light Purple"),
    ("P", "Purple"),
    ("DP", "Dark Purple"),
    ("W", "White"),
    ("LN", "Light Grey"),
    ("N", "Grey"),
    ("DN", "Dark Grey"),
    ("K", "Black"),
    ("LT", "Light Brown"),
    ("T", "Brown"),
    ("DT", "Dark Brown"),
)


def tartan_colour_to_html_colour(colour):
    global PALETTE
    if PALETTE:
        html_colour = PALETTE[colour]
        return html_colour
    if colour == "LR":
        return "lightred"
    elif colour == "R":
        return "red"
    elif colour == "DR":
        return "darkred"
    elif colour == "O":
        return "orange"
    elif colour == "DO":
        return "darkorange"
    elif colour == "LY":
        return "lightyellow"
    elif colour == "Y":
        return "yellow"
    elif colour == "DY":
        return "#BC8C00"
    elif colour == "LG":
        return "lightreen"
    elif colour == "G":
        return "green"
    elif colour == "DG":
        return "darkreen"
    elif colour == "LB":
        return "lightblue"
    elif colour == "B":
        return "blue"
    elif colour == "DB":
        return "darkblue"
    elif colour == "LP":
        return "lightpurple"
    elif colour == "P":
        return "purple"
    elif colour == "DP":
        return "darkpurple"
    elif colour == "W":
        return "white"
    elif colour == "LN":
        return "lightgray"
    elif colour == "N":
        return "gray"
    elif colour == "DN":
        return "darkgray"
    elif colour == "K":
        return "black"
    elif colour == "LT":
        return "lightbrown"
    elif colour == "T":
        return "brown"
    elif colour == "DT":
        return "darkbrown"
    else:
        raise TartanException(f"Colour {colour} is not defined")
