from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'tb3_sim'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
        ('share/' + package_name + '/maps', glob('maps/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='amitav',
    maintainer_email='amitav@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'amcl_init_pose_publisher = tb3_sim.set_init_amcl_pose:main','am = tb3_sim.example_node:main',
        ],
    },
)
