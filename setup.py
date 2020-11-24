
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyAmongUsAPI",
    version="0.0.1",
    author="hunterg",
    author_email="redissuslolol@gmail.com",
    description="For interacting with among us",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.beyonce.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires = []
)