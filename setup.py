import setuptools

with open('README.md', 'r') as file:
    long_description=file.read()

setuptools.setup(
    name='Pterodactyle.py',
    version='0.0.0',
    author='MaxPython110331',
    author_email='max.gamil110331@gmail.com',
    description='The python package which is easy to manage your Pterodactyle\'s panel.',
    long_description=long_description,
    url='https://github.com/max-github110331/Pterodactyl.py',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Natural Langage :: English :: Chinese',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.10',
    install_requires=[
        'requires >=2.32.3'
    ]
)