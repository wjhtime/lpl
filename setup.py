from setuptools import setup, find_packages

setup(
      name='lpl',
      version=0.1,
      description="lpl game based on Python",
      long_description='lpl game based on Python',
      classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords=('lpl', 'lol'),
      author='wjh',
      author_email='wjhokey@gmail.com',
      url='https://github.com/wjhtime/lpl',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'prettytable',
          'requests',
          'termcolor',
          'click'
      ],
      entry_points={
          'console_scripts': [
              'lpl = lpl.lpl:main'
          ]
      },
)