import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="usocketgen",
    version="0.0.8",
    author="phoenix.lv",
    author_email="phoenix.grey0108@gmail.com",
    description="lib and code generator to create unix domain socket server and client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hellstein/unix-socket-cs",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
