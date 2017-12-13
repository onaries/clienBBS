from setuptools import setup


setup(
    name='clienBBS',
    version='0.30',
    description='clienBBS: Retro-style BBS interface for the Clien.net community',
    long_description='',
    url='https://github.com/liza183/clienBBS',
    author='Matt Sangkeun Lee',
    author_email='johnleespapa@gmail.com',
    license='Private',  # 알맞게 고쳐주세요!
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
    ],
    packages=[],
    py_modules=['clien'],
    python_requires='>=3.5',
    install_requires=[
        'urllib3',
        'bs4',
        'certifi',
        'requests',
        'pyreadline',
        'lxml',
        'image',
    ],
    entry_points={
        'console_scripts': [
            'clien = clien:main',
        ]
    },
)
