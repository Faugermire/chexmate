from setuptools import setup, find_packages

setup(
    name="seamless-chex",
    version="0.0.1",
    description="An (unofficial) package used to integrate with the SeamlessChex API quickly and easily.",
    long_description=open('README.md').read(),  # Optionally include a README file for a detailed description
    long_description_content_type='text/markdown',  # Specify the format of your long description
    author="William Hinz",  # Replace with your name or organization
    author_email="faugermire@gmail.com",  # Replace with your email
    url="https://github.com/your_username/your_project",  # Replace with the URL of your project
    packages=find_packages(),  # Automatically find packages in the project
    install_requires=[  # List the packages your project depends on
        "setuptools~=74.1.2"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Replace with your license
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12.5',  # Specify minimum Python version
)