from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="register_package",
    version="0.0.1",
    author="Davi",
    author_email="davi.pultrini@gmail.com",
    description="This a code make image Register",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pultrini/image_register_package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
