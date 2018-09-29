import os

from .config import LANDeviceProberConfig
from .discover import LANDeviceProber


def main():
    config = LANDeviceProberConfig()

    if 'LAN_DEV_PROBER_CONFIG' not in os.environ:
        print("Environment variable LAN_DEV_PROBER_CONFIG not exists.")
        return None
    else:
        config.FromEnv('LAN_DEV_PROBER_CONFIG')

    prober = LANDeviceProber(config)

    return prober.Run()

    

if __name__ == '__main__':
    main() 