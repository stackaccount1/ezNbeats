from setuptools import setup, find_packages

setup(name='ezNbeats',
      version='0.0',
      description='ezNbeats',
      url='na',
      author='stackaccount1',
      author_email='na',
      license='',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      package_data={'ezNbeats': ['data/*.csv']},
      install_requires=[
          'sklearn~=0.0',],
      zip_safe=False)
      
     
