from setuptools import setup
setup(name='RPi',
      version='0.1',
      description='Mock GPIO interface',
      url='https://github.com/onwebbe/mockGPIO.git',
      author='onwebbe',
      license='MIT',
      packages=['RPi', 'Adafruit_DHT', 'smbus'],
      zip_safe=False)