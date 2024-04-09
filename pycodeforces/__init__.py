"""
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

LICENSE:
```text
    Interacts with CodeForces API.
    Copyright (C) 2024 halfstackpgr

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see https://www.gnu.org/licenses.
```
"""

__version__ = "1.0dev"


__all__ = ["AsyncMethod", "SyncMethod", "AsyncClient", "SyncClient"]

from pycodeforces.__processors__ import AsyncMethod, SyncMethod
from pycodeforces.__clients__ import AsyncClient, SyncClient
