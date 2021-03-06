import pathlib
from setuptools import setup

README = pathlib.Path(__file__).parent / "README"
README = README.read_text()

setup(
    name="Jinja Recurse",
    version="0.0.1",
    author="diginc",
    author_email="adam@diginc.us",
    description=("Jinja Recursive Templating for the CLI"),
    license="MIT",
    keywords="jinja templater",
    url="https://www.github.com/diginc/jinjarecurse",
    packages=["jinjarecurse"],
    long_description=README,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
        "docopt==0.6.2",
        "jinja2==2.11.1",
        "markupsafe==1.1.1",
        "pathlib2==2.3.5",
        "pyyaml==5.3",
        "six==1.14.0",
    ],
    entry_points={
        'console_scripts': [ 'jinjarecurse = jinjarecurse.main:main']
    }
)
