import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
b
setuptools.setup(
    name="skyscrapers_project_bmykhaylivvv",
    version="0.0.1",
    author="Bohdan Mykhayliv",
    author_email="bohdan.mykhailiv@ucu.edu.ua",
    description="Project which checks if there is a winning combination \
    for \"Skyscrapers game\" on the board ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bmykhaylivvv/coding_semester_2/tree/main/lab_1/skyscapers",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8'
