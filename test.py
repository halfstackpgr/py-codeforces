API = "5a0cce94f9ca968dda80fa6565e65f15539527c8"
SECRET = "071f5b6c218f466fc19c90c248b24d794920a557"


from pycodeforce.processors import AsyncMethod
import asyncio
import time


async def main():
    ld = AsyncMethod(auth_key=API, unix_time=int(time.time()), secret=SECRET)
    await ld.get_user(handles="halfstackpgr", check_historic_handles=False)
    await ld.close()


asyncio.run(main=main())
