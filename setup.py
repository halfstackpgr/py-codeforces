from setuptools import setup

setup(
    name="py-codeforces",
    packages=["pycodeforces"],
    version="1.0dev",
    license="GPL 3.0",
    description="Py-Codeforces is a high-performance and type-safe Python library designed for seamless interaction with Codeforces. It offers both asynchronous and synchronous client handlers, allowing developers to choose the appropriate method based on their requirements.",
    author="Parth Mishra",
    author_email="halfstackpgr@gmail.com",
    url="https://github.com/halfstackpgr/py-codeforces",
    keywords=["python", "codeforces", "api", "wrapper", "async", "sync"],
    install_requires=[
        "aiohttp",
        "requests",
        "msgspec",
        'tomli; python_version < "3.11"',
    ],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Development Status :: 1 - Alpha/Unstable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
