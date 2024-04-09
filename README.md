# Py-Codeforce
## Faster | Better | Type-Safe


![Ruff](https://camo.githubusercontent.com/18c26428c337f9d641fa09b629a3a03b514e8ac84b57974a0ed7d1b38e14e060/68747470733a2f2f696d672e736869656c64732e696f2f656e64706f696e743f75726c3d68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f61737472616c2d73682f727566662f6d61696e2f6173736574732f62616467652f76322e6a736f6e) ![Passing Package](https://github.com/halfstackpgr/py-codeforces/actions/workflows/python-publish.yml/badge.svg) 
![Static Badge](https://img.shields.io/badge/python-Strict-checking?style=plastic&logo=python&label=Type-Checking&labelColor=yellow)


![image](https://github.com/halfstackpgr/py-codeforces/assets/118044992/cdb54788-3fbc-48db-b936-7f0e883f9709)


## Py-Codeforces

Py-Codeforces is a high-performance and type-safe Python library designed for seamless interaction with Codeforces. It offers both asynchronous and synchronous client handlers, allowing developers to choose the appropriate method based on their requirements.

Key Features:
1. ### Client Handlers:
   - Synchronous Handler: `SyncMethod`
   - Asynchronous Handler: `AsyncMethod`

2. ### Functionality:
   Both client handlers offer the same set of functionalities, ensuring consistency and flexibility in usage.

3. ### Authentication:
   To access user-related attributes, authentication must be enabled by setting the `enable_auth` parameter to `True`.

4. ### API Documentation:
   This library is built entirely based on the official [Codeforces API Documentation](https://codeforces.com/apiHelp/), ensuring reliability and adherence to best practices.

Example Usage:

### Asynchronous usage:

```python
import asyncio
import pycodeforces

async def main():
    api = pycodeforces.AsyncMethod()
    users = await api.get_user_info(handles="DmitriyH;Fefer_Ivan")
    # use `;` to add multiple parameters.
    async for user in users:
        print(user.avatar)

asyncio.run(main())
```

### Synchronous usage:

```python
import pycodeforces

async def main():
    get = pycodeforces.SyncMethod()
    users = get.get_user_info(handles="DmitriyH;Fefer_Ivan")
    # use `;` to add multiple parameters.
    for user in users:
        print(user.avatar)
```

## Features

- Is 100% type safe.
- For customisation in types, a specific module `abc` has been provided within the head module.
- Dual modes for specific requirements regarding auth.
-- Can be enabled by passing a `True` to `Method` constructor 

## Uses:
1. [msgspec](https://github.com/jcrist/msgspec) - for data validation and then serialisation. 
2. [ruff](https://github.com/astral-sh/ruff) - for linear code formatting and consistency.


## Installation
Installing as a user:
```sh
pip install py-codeforce
```

Installing as a developer:
```sh
pip install py-codeforce[dev]
```

## Open Source Contribution:
Want to contribute? Great!
Check the `Issues` for getting to know about further updates and solutions to occurring problems. 
Maintain the type-checking as strict.
Stack a PR to the production 


Thank you for checking out the repo. 
Give it a star if you've found it worthy.