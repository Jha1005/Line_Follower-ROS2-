from setuptools import find_packages, setup

package_name = 'my_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'rclpy', 'std_msgs', 'pyserial','bleak','asyncio'],

    zip_safe=True,
    maintainer='pushpanjali',
    maintainer_email='pushpanjalijha005@example.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['ir_node'],
    entry_points={
        'console_scripts': [
            'ir_node = my_bot.ir_node:main',
             'motor_control = my_bot.motor_control:main',
             'blue = my_bot.blue:main',
        ],
    },
)
