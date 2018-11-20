from __future__ import absolute_import

# third party modules
from setuptools import setup
install_requires = [
    'django-jsonfield',
    'future',
    'minibelt',
    'python-dateutil',
    ]


long_description='package to tune django password authentification',

setup(
    name='django-pwdtk',
    version='0.0.1',
    description='package to tune django password authentification',
    #long_description=long_description,
    #long_description_content_type="text/x-rst",
    classifiers=[
        'Development Status :: 3 - Alpha',
        ],
    keywords='django authentification password',
    url='https://www.teledomic.eu',
    author='MHComm',
    author_email='info@mhcomm.fr',
    license="MIT",
    packages=[
      'pwdtk',
      'pwdtk.testproject',
      'pwdtk.testproject.dj18',
      'pwdtk.testproject.dj1',
      'pwdtk.testproject.dj21',
      'pwdtk.tests',
      ],
    scripts=[],
    entry_points={
        'console_scripts': [
          ]
    },
    project_urls={
      'Documentation': "https://github.com/mhcomm/django-pwdtk",
      'Source': "https://github.com/mhcomm/django-pwdtk",
      'SayThanks': "https://github.com/mhcomm",
      'Funding': 'https://donate.pypi.org',
      'Tracker': "https://github.com/mhcomm/django-pwdtk/issues",
    },
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest',
        ],
    include_package_data=True,
    )