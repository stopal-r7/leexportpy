from setuptools import setup, find_packages

setup(
    name='leexportpy',
    version='0.1.5',
    author='Safa Topal',
    author_email='Safa_Topal@rapid7.com',
    packages=find_packages(exclude=['*tests*']),
    url='https://github.com/rapid7/logentries-leexportpy',
    license='MIT',
    description='Logentries by Rapid7 log export proxy for external systems.',
    long_description=open('README.md').read(),
    install_requires=['requests==2.9.1', 'datetime==4.1.1', 'daemonize==2.4.6',
                      'configobj==5.0.6', 'twisted==16.2.0'],
    entry_points={'console_scripts': ['leexportpy = leexportpy.leexport:main']},
    zip_safe=False
)
