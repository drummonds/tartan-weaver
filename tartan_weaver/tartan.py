"""This describes a tartan pattern.
It is assumed to be half set symetric patterns
"""
import re
from .colours import PALETTE

PATTERN = re.compile("([a-zA-Z]*)([0-9]*)")


def split_thread(threadcount):
    """Given a thread count such as R14, will split to R and integer 14"""
    threadcount = threadcount.replace("/","")
    match = re.search(PATTERN, threadcount)
    if match:
        return match.group(1), match.group(2)
    return threadcount, ""


class Stripe:
    def __init__(self, short_colour, count):
        self.short_colour = short_colour
        self.count = int(count)

    def __str__(self):
        return f"{self.short_colour}{self.count}"


class Tartan:
    def __init__(self):
        self.stripes = []

    @classmethod
    def from_space_threadcount(cls, threadcount, palette):
        global PALETTE
        if palette:
            PALETTE = {}
            colours = palette.split(" ")
            for colourCode in colours:
                part     = colourCode.split("#")
                PALETTE[part[0]] = part[1]
        tartan = cls()
        threads = threadcount.split(" ")
        for thread in threads:
            colour, count = split_thread(thread)
            tartan.stripes.append(Stripe(colour, count))
        return tartan

    def __str__(self):
        s = " ".join([f"{s}" for s in self.stripes])
        return s

    @property
    def threadcount(self):
        tc = 0
        for stripe in self.stripes:
            tc += stripe.count
        return tc

    def create_generator(self):
        forwards = True
        index = 0
        while True:  # Change stripe
            stripe = self.stripes[index]
            for thread in range(stripe.count):
                yield stripe.short_colour
            # Implement symmetry of pattern
            if forwards:
                if index == len(self.stripes) - 1:
                    forwards = False
                else:
                    index += 1
            else:
                if index == 0:
                    forwards = True
                else:
                    index -= 1
