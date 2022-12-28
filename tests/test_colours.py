from tartan_weaver import tartan_colour_to_html_colour


def test_red():
    assert tartan_colour_to_html_colour("R") == "red"
