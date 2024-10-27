from setuptools import find_packages, setup # type: ignore

# Read the content of your requirements.txt file
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="mlops_practice",  # Replace with your project name
    version="0.1.0",
    author="Kiriti Aajad",
    author_email="kiriti.aajad@gmail.com",
    description="A simple ML project for MLOps practice.",
    packages=find_packages(),  # Automatically finds and lists all packages in src/
    install_requires=requirements,  # Dependencies listed in requirements.txt
    include_package_data=True,  # Includes any data files specified in MANIFEST.in
    license="MIT",
    url="https://github.com/yourusername/mlops_practice",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
