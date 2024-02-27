import os
from dotenv import load_dotenv
from destipy.destiny_client import DestinyClient

load_dotenv()

# Create the directory for the log file if it doesn't exist
log_dir = os.path.join('C:', os.sep, 'Users', 'neilw', 'OneDrive', 'Documents', 'GitHub', 'zooloo.me', 'logs')
os.makedirs(log_dir, exist_ok=True)

client = DestinyClient(os.getenv("bungie_token"))

async def get_user():
    user = await client.user.GetBungieNetUserById(4611686018467765462)
    return user

# Then, you can run this function using an event loop, like this:

import asyncio

user = asyncio.run(get_user())

print(user.display_name)