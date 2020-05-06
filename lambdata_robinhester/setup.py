# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata_robinhester", # the name that you will install via pip
    version="1.1",
    author="Robin Hester",
    author_email="robin.hester@yahoo.com",
    description="Functions that can used with predictive modeling",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/robinhester/lambdata_package",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)