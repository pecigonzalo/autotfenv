import json
from codecs import open
from os import environ, path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open('Pipfile.lock') as fd:
    lock_data = json.load(fd)
    install_requires = [
        "pyhcl"
    ]
    tests_require = [
        package_name for package_name in lock_data['develop'].keys()
    ]

setup(
    name='autotfenv',
    version=environ.get("TRAVIS_TAG", "0.0.0"),
    author_email='pecigonzalo@users.noreply.github.com',
    author='Gonzalo Peci',
    long_description=open('README.md').read(),
    python_requires='>=3.6',
    install_requires=install_requires,
    extras_require={
        'test': tests_require,
    },
    packages=['autotfenv'],
    entry_points={
        'console_scripts': [
            'autotfenv = autotfenv.cli:main'
        ]
    }
)
