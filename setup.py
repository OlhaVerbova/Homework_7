from setuptools import setup, find_namespace_packages
setup(
          name = 'clean folder',
          version = '0.0.1',
          description = 'A folder cleaner that will sort files',
          author = 'Olha Verbova',
          author_email = 'olgaverbovap@gmail.com',
          utrl = 'https://github.com/OlhaVerbova/Homework_7',
          license = 'MIT',
          classifiers = ["Programming Language :: Python :: 3",
                         "License :: OSI Approved :: MIT License"],
          packages = find_namespace_packages(),
          entry_points = {'console_scripts': [ "clean-folder=clean_folder.main:main"]}

)