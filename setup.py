from setuptools import setup, find_packages

setup(
    name="seamy-chex",
    version="0.0.1",
    description="An (unofficial) package used to integrate with the SeamlessChex API quickly and easily.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="William Hinz",
    author_email="faugermire@gmail.com",
    url="https://github.com/Faugermire/seamless-chex",
    packages=find_packages(),
    install_requires=[
        "setuptools~=74.1.2"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
)