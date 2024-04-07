from setuptools import setup

package_name = 'Snake_game'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='walter_white',
    maintainer_email='walter_white@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ["Snake_game=Snake_game.Snake:main",
                            "Snake_game2=Snake_game.Snake2:main",
        ],
    },
)
