from twitchio.ext import commands

class Test:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hola")
    async def hello_command(self, ctx):
        await self.bot.channel.send("Hello there!")

def prepare(bot):
    bot.add_cog(Test(bot))