from setuptools import setup
setup(
    name = 'projectidea-cli',
    version = '1.0',
    packages = ['projectidea'],
    entry_points = {
        'console_scripts': [
            'projectidea = projectidea.__main__:main'
        ]
    })