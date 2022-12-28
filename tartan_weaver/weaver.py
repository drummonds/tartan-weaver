from PIL import Image, ImageDraw

from .colours import tartan_colour_to_html_colour
from .tartan import Tartan


class TwillHarness:
    def __init__(self):
        self.state = 0
        self.state_start = 0
        self.is_s = True

    def new_weft(self):
        if self.is_s:
            self.state_start = self.dec_state(self.state_start)
        else:
            self.state_start = self.inc_state(self.state_start)
        self.state = self.state_start

    def inc_state(self, count):
        count += 1
        if count > 3:
            count = 0
        return count

    def dec_state(self, count):
        count -= 1
        if count < 0:
            count = 3
        return count

    def create_generator(self):
        while True:  # Change harness
            if self.state == 0:
                yield (False)
            elif self.state == 1:
                yield (False)
            elif self.state == 2:
                yield (True)
            else:
                yield (True)
            self.state = self.inc_state(self.state)


class Weaver:
    """wefts are the shuttle threads and have to be in pairs.  They are synonmous with rows.  Worp
    are the fix threads attached to harnesses that go up and down.  They synonmous with cols."""

    def __init__(self, height=300, width=300):
        self.out = Image.new("RGB", (width, height), (250, 250, 255))
        self.dwg = ImageDraw.Draw(self.out)
        self.height = height
        self.width = width
        self.weft_counter = 0  # Start from bottom and prob up 2
        self.weft_width = 25
        self.weft_gap = 10
        self.worp_width = 25
        self.worp_gap = 10
        self.edge = 5
        self.tartan = Tartan.from_space_threadcount("R1 B2", "R#ff0000 B#0000ff")
        self.twill_harness = TwillHarness()

    @property
    def num_wefts(self):
        return int((self.height - self.edge * 2) // self.weft_size)

    @property
    def num_worps(self):
        return int((self.width - self.edge * 2) // self.worp_size)

    @property
    def weft_size(self):
        return self.weft_width + self.weft_gap

    @property
    def worp_size(self):
        return self.worp_width + self.worp_gap

    def weft_counter_to_y(self):
        return self.height - ((1 + self.weft_counter) * self.weft_size)

    def add_weft(self):
        colour = tartan_colour_to_html_colour(next(self.weft_gen))
        x0 = int(self.edge)
        x1 = int(self.width - self.edge)
        y0 = int(self.weft_counter_to_y())
        y1 = int(y0 + self.weft_width)
        self.dwg.rectangle(
            (x0, y0, x1, y1), fill=colour, width=0
        )  # Remove stroke="black" as at high resolutions interferes with patterns

    def add_worp(self, worp_count):
        colour = tartan_colour_to_html_colour(next(self.worp_gen))
        if next(self.twill_gen):  # over
            x0 = int(self.edge + worp_count * self.worp_size)
            x1 = int(x0 + self.worp_width)
            y0 = int(self.weft_counter_to_y() - self.weft_gap / 2)
            y1 = int(y0 + 0.1 + self.weft_size)
            self.dwg.rectangle(
                (x0, y0, x1, y1), fill=colour, width=0
            )  # Remove stroke="black" as at high resolutions interferes with patterns
        # else:  # print underneath
        #     self.dwg.add(dwg.rect(
        #         insert=(self.edge + worp_count * self.worp_size,self.weft_counter_to_y()-self.weft_gap/2),
        #         size=(self.worp_width,self.weft_gap/2), fill="black"))
        #     self.dwg.add(dwg.rect(
        #         insert=(self.edge + worp_count * self.worp_size,self.weft_counter_to_y()+self.weft_width),
        #         size=(self.worp_width,self.weft_gap/2), fill="black"))

    def weave(self):
        """Weaving starts for bottom left going up and right"""
        self.twill_gen = self.twill_harness.create_generator()
        self.weft_gen = self.tartan.create_generator()
        for i in range(self.num_wefts):
            self.add_weft()
            self.worp_gen = (
                self.tartan.create_generator()
            )  # TODO reset rather than renew
            for j in range(self.num_worps):
                self.add_worp(j)
            self.twill_harness.new_weft()
            self.weft_counter += 1
