 from setuptools import setup

 setup(
     name="pyweave",
     version="0.0.1",
     description="Weave tartan.",
     py_modules=["pyweave", "tartan_weaver"],
     entry_points={
         "console_scripts": ["pyweave=pyweave:main"],
     },
 )