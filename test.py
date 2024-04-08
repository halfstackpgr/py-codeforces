API = "5a0cce94f9ca968dda80fa6565e65f15539527c8"
SECRET = "071f5b6c218f466fc19c90c248b24d794920a557"


from pycodeforce.processors import AsyncMethod
import asyncio
import time


async def main():
    ld = AsyncMethod(auth_key=API, unix_time=int(time.time()), secret=SECRET)
    users = await ld.get_blog_entry_comments(blog_entry_id=127719)
    if users is not None:
        for user in users:
            print(user.content)
    await ld.close()


asyncio.run(main=main())
