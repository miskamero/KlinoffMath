from setuptools import setup

setup(
    name='klinoff-math',
    version='0.1.2',
    description='A simple klinoff math library by Klinoff Corp (See Github)',
    author='Klinoff Corp',
    py_modules=['klinoffmath'],
    install_requires=['simpleaudio'],
    package_data={'': ['*.wav']},
    include_package_data=True,
)
