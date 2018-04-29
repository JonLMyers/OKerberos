from setuptools import setup, find_packages
install_requires = [
    'pysha3~=1.0.2',
    'flask>=0.10.1',
    'flask-cors~=3.0.0',
    'flask-restful~=0.3.0',
    'requests~=2.9',
    "gevent>=1.2.1",
    "colorlog>=3.0.1",
    'PyNaCl~=1.1.0',
    'base58~=0.2.2'

]
setup(
    name='OKerberos',
    version="0.1.0",
    description= 'Simple Keberos Protocol',
    long_description=(
        "Package contains a client and authentication server"
        ),
    url='https://github.com/JonLMyers/OKerberos',
    author='Daniel Harrington',
    author_email='dxh7006@rit.edu',
    license='Apache Software License 2.0',
    zip_safe=False,
    packages=find_packages(exclude=['tests*']),
    entry_points={
        'console_scripts': [
             'okerberos = okerberos.commands:execute',
        ],
    },
    install_requires=install_requires,
)
