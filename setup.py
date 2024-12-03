from setuptools import setup, find_packages
from post_install import PostInstallCommand

setup(
    name="mkpj-python",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mkpjp=mkpj.main:main',
        ],
    },
    install_requires=[
        # Add any dependencies here
    ],
    include_package_data=True,
    package_data={
        # Include any package data files here
    },
    data_files=[
        ('config', ['mkpj/config.py']),
    ],
    cmdclass={
        'install': PostInstallCommand,
    },
)