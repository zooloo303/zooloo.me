import asyncio
from dotenv import load_dotenv
import os
from bungio import Client
from bungio.models import BungieMembershipType, DestinyActivityModeType, DestinyUser

load_dotenv()
# create the client obj with our bungie authentication
client = Client(
    bungie_client_id=os.getenv("client_id"),
    bungie_client_secret=os.getenv("client_secret"),
    bungie_token=os.getenv("bungie_token"),
)

async def main():
    # create a user obj using a known bungie id
    user = DestinyUser(membership_id=4611686018467765462, membership_type=BungieMembershipType.TIGER_STEAM)

    # iterate thought the raids that user has played
    async for activity in user.yield_activity_history(mode=DestinyActivityModeType.RAID):

        # print the date of the activity
        print(activity.period)

# bungio is by nature asynchronous, it can only be run in an asynchronous context
asyncio.run(main())