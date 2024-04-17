import asyncio
import pycodeforces


KEY = "5a0cce94f9ca968dda80fa6565e65f15539527c8"
SECRET = "071f5b6c218f466fc19c90c248b24d794920a557"


async def main():
    api = pycodeforces.AsyncMethod(enable_auth=True, auth_key=KEY, secret=SECRET)
    users = await api.get_user(handles="DmitriyH;Fefer_Ivan")
    # use `;` to add multiple parameters.
    if users:
        for user in users:
            print(user.avatar)


asyncio.run(main())
