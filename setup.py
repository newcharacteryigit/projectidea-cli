from setuptools import setup
setup(
    name = 'projectidea-cli',
    version = '1.0',
    author = 'Yigit K.',
    author_email = 'projectideacli@gmail.com',
    description = ('You can find different project ideas easily with this cli!'),
    license = 'MIT',
    packages = ['projectidea'],
    entry_points = {
        'console_scripts': [
            'projectidea = projectidea.__main__:main'
        ]
    })