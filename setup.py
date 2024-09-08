import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.0"

REPO_NAME = "olympics-all-in-all"
AUTHOR_USER_NAME ="Ankita1490"
SRC_REPO = "OlympicsDataAnalysis"
AUTHOR_EMAIL = "ankpillay@gmail.com"


setuptools.setup(
    name = SRC_REPO,
    version= __version__,
    author= AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description = "A small python package for Olympics Data Analysis",
    long_description= long_description,
    long_description_content = "text/markdown",
    url = f"http://github.com/{AUTHOR_USER_NAME}/REPO_NAME",
    project_urls ={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages= setuptools.find_packages(where = "src")
)
