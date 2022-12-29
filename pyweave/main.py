import argparse
from PIL import Image, ImageDraw, ImageFont

import sys

sys.path.append("/home/hum3/major_projects/tartan-weaver")
from tartan_weaver import Tartan, Weaver

def main():
    parser = argparse.ArgumentParser(
                    prog = 'ProgramName',
                    description = 'What the program does',
                    epilog = 'Text at the bottom of help')
    parser.add_argument('-o', '--output', help="output file name", default = "tartan.png")      # option that takes a value
    parser.add_argument('-c', '--colours', help="colour palette eg 'R#ff0000 B#0000ff' see https://tartandictionary.org/posts/threadcounts/")  # on/off flag
    parser.add_argument('-t', '--threadcount', help="thread counts see https://tartandictionary.org/posts/threadcounts/")  # on/off flag
    parser.add_argument('-s', '--size', help="size eg A4p, A5l, A6", default = "A4p")  # on/off flag
    args = parser.parse_args()

    print("Python weaver colours x tartan y size x")

    if args.size == "A6p":
        paper = [148, 105]  # mm
    elif args.size == "A6l":
        paper = [105, 148]  # mm
    elif args.size == "A5p":
        paper = [210, 148]  # mm
    elif args.size == "A5p":
        paper = [148, 210]  # mm
    elif args.size == "A4l":
        paper = [210, 297]  # mm
    else: # size == "A4":
        paper = [297, 210]  # mm
    
    paper_in = [mm / 25.4 for mm in paper]
    dpi = 600
    paper_pix = [int(inch) * dpi for inch in paper_in]
    size = 3 * paper_pix[0] * paper_pix[1]
    print(f"Est size of file = {size} ({paper_pix[0]},{paper_pix[1]})")
    w = Weaver(height=paper_pix[0], width=paper_pix[1])
    w.weft_gap = 0
    w.worp_gap = 0
    w.weft_width = 3
    w.worp_width = 3
    palette = {}
    colours = args.colours.split(" ")
    for colourCode in colours:
        part = colourCode.split("#")
        palette[part[0]] = part[1]
    w.tartan = Tartan.from_space_threadcount(args.threadcount)
    PALETTE = palette 
    w.weave(palette=palette)
    w.out.save(args.output, "PNG")
    w.out.show()

if __name__ == "__main__":
    main()
