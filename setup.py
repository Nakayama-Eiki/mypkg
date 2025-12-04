import os
from glob import glob
from setuptools import setup, find_packages

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hoge',
    maintainer_email='qwertyuiop1103566@gmail.com',
    description='a pakage for practice',
    license='GPL3.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'talker = mypkg.talker:main',
            'listener = mypkg.listener:main',
        ],
    },
)
