from setuptools import setup

setup(
    name='snack',
    packages=['snack'],
    include_package_data=True,
    install_requires=[
        'snack',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
