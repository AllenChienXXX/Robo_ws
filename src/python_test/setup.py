from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'python_test'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='4ll3n',
    maintainer_email='allen71090@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'wheel = python_test.wheel_pub:main',
            'sensor = python_test.sensor:main',
        ],
    },

)
