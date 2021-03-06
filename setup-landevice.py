import os
import os.path
from setuptools import setup

def load_requirements():
    return [req.replace('\n', '') for req in open(os.path.join(os.getcwd(), 'requirements_landevice.txt'), 'rt').readlines()]

setup(
    name = 'LANDevice'
    , description = "LAN Device discover."
    , version = '1.0.2'
    , packages = [
        'LANDevice'
        , 'LANDevice.service'
    ]
    , install_requires = load_requirements()
    , data_files = [
        'requirements_landevice.txt'
    ]
)
