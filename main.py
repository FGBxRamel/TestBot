import configparser as cp

import interactions as i

with open("config.ini", "r") as config_file:
    config = cp.ConfigParser()
    config.read_file(config_file)
    TOKEN = config.get("General", "token")
    SERVER_IDS = config.get("General", "server_ids").split(",")

client = i.Client(token=TOKEN)


@client.event()
async def on_ready():
    print("Ready!")


@client.command(
    name="ping",
    description="Pong!",
    scope=SERVER_IDS
)
async def ping(ctx):
    await ctx.send("Pong!")

client.run()
