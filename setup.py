from distutils.core import setup

requires = [
    'pyramid',
    'pyramid_debugtoolbar',
    'humanize',
    'prettytable',
    'pytz',
    'requests',
    'waitress',
    'sqlalchemy',
    'dateutil'
]

setup(name='pynder_web',
      version='0.0.1',
      entry_points="""\
[paste.app_factory]
main = pynder_web:main
""")
