from twitchio.ext import commands
from pathlib import Path
from .tokens import *

NICK = "xodibot"
CHANNEL = "xodi96"

class TwitchBot(commands.Bot):
    def __init__(self):
        self._cogs = [p.stem for p in Path(".").glob("./bot/cogs/*.py")]
        super().__init__(
            irc_token=IRC_TOKEN,
            api_token='23nbr1nu2dojmwzwd5sef2kaufpzjn',
            client_id="gp762nuuoqcoxypju8c569th9wz7q5",
            nick=NICK,
            prefix='!',
            initial_channels=(CHANNEL,),
        )

    def setup(self):
        print("Running setup...")
        for cog in self._cogs:
            self.load_module(f"bot.cogs.{cog}")
            print(f"Loaded '{cog}' cog.")
        
        print("Setup complete")

    def run(self):
        self.setup()
        print("Running bot...")
        super().run()

    async def event_ready(self):
        self.channel = self.get_channel("xodi96")
        await self.channel.send(f"/me Landed!")

    #async def event_error(self, error, data=None):
    #    pass

    async def event_command_error(self, ctx, error):
        await self.channel.send("Ups! Hi ha hagut algun error amb la comanda {command}".format(command=ctx.message.content))

    async def event_join(self, user):
        print(f"{user.name} joined!")
        if user.name.lower() == "xodibot" or user.name.lower() == self.initial_channels[0].lower() or user.name.lower() == "streamelements":
            return
        else:
            if user.name == "pakitoo96":
                await self.channel.send("UwU")
            elif user.name == "xavi_clot":
                await self.channel.send("OwO")
            else:
                await self.channel.send(f"Welcome to the stream {user.name}!")

    #async def event_raw_pubsub(self, data):
    #    print(data)
    #    await self.channel.send(f"Thanks for subscribing!")

    async def event_message(self, message):
        print(f"> {message.author.name}: {message.content}.")
        await self.handle_commands(message)

    @commands.command(name="test")
    async def test_command(self, ctx):
        await self.channel.send("This is a test! PogChamp")