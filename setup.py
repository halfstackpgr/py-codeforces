from setuptools import setup

setup(
    name="py-codeforces",
    packages=["py-codeforces"],
    version="1.0dev",
    license="GPL 3.0",
    description="Py-Codeforces is a high-performance and type-safe Python library designed for seamless interaction with Codeforces. It offers both asynchronous and synchronous client handlers, allowing developers to choose the appropriate method based on their requirements.",
    author="Parth Mishra",  # Type in your name
    author_email="halfstackpgr@gmail.com",  # Type in your E-Mail
    url="https://github.com/halfstackpgr/py-codeforces",  # Provide either the link to your github or to your website
    keywords=["python", "codeforces", "api", "wrapper", "async", "sync"],
    install_requires=[
        "aiohttp",
        "requests",
        "msgspec",
        'tomli; python_version < "3.11"',
    ],
    classifiers=[
        "License :: OSI Approved :: GPL 3.0 License",
        "Development Status :: 1 - Alpha/Unstable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
