"""
Copyright 2021 Raghu Valusa

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
 
from setuptools import setup, find_packages
 
# See note below for more information about classifiers
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: POSIX :: Linux',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 2.7',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='toy_robot_simulator',
  version='0.0.1',
  description='toy robot simulation which takes input commands from a file. Robot rotates and moves one step at a time and reports the position to STD out',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  # the URL of your package's home page e.g. github link
  author='Raghu Valusa',
  author_email='raghu.valusa@gmail.com',
  license='MIT', # note the American spelling
  classifiers=classifiers,
  keywords='robot_toy toy_robot toy_robot_simulator', # used when people are searching for a module, keywords separated with a space
  packages=find_packages(),
  install_requires=[''] # a list of other Python modules which this module depends on.  For example RPi.GPIO
)