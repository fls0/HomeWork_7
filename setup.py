from setuptools import setup

setup(name='clean_folder',
      version='1',
      description='Programm for cleaning folders',
      url='https://github.com/fls0/clear_folder',
      author='fls',
      author_email='mackss.1337@ex.ua',
      license='MIT',
      packages=['clean_folder'],
      entry_points={'console_scripts': ['clean-folder = clean_folder.main:run']}
    )