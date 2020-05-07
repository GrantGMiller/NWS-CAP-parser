from distutils.core import setup
import glob

setup(
    name='nwscapparser3',
    version='3.0.0',
    description='NWS CAP Parser for Python3',
    author='Grant Miller. Based on the work of Robert Morris (robert@emthree.com)',
    author_email='grant@grant-miller.com',
    url='https://github.com/GrantGMiller/NWS-CAP-parser',
    packages=['nwscapparser3', 'requests', 'lxml'],
    data_files=[
        ('', glob.glob('*.xml')),
        ('', ['demo.py', 'readme.md', 'LICENSE'])]
)
