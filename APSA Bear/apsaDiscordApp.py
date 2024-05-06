import settings
import discord
from discord.ext import commands

#variables
event_shell_bus = [] #objects that contain the event object, announcement object, and subsequent reminder message objects
bot_on = True
reminder_count = 3
reminder_min_interval = 10 #in minutes

#enable functionality
intents = discord.Intents.default()
intents.message_content = True
intents.guild_scheduled_events = True


def run_app():
    app = discord.Client(intents=intents)

    @app.event
    async def on_ready():
        print(f'{app.user} ready')

    app.run(settings.TOKEN)

#------------------------------------------
# @bot.event
# async def on_scheduled_event_create(event):
#     if bot_on == False:return
#     event_announcement = ""
#     event_announcement += "FROM: " + event.creator.display_name
#     event_announcement += "\n\n"
#     event_announcement += "TIME: " + event.start_time + " - " + event.end_time
#     event_announcement += event.description

#     await bot.get_channel(test_event_channel_id).send(event_announcement)


# @bot.event
# async def bot_on(ctx):
#     if bot_on:
#         await ctx.send(bot_name + " is already on")
#     else:
#         bot_on = True
#         await ctx.send(bot_name + " has been turned on")

# @bot.event
# async def bot_off(ctx):
#     if not bot_on:
#         await ctx.send(bot_name + " is already off")
#     else:
#         bot_on = False
#         await ctx.send(bot_name + " has been turned off")

# @bot.event
# async def bot_toggle(ctx):
#     current_status = bot_on
#     bot_on = not bot_on
#     if current_status:
#         await ctx.send(bot_name + " has been turned OFF")
#     else:
#         await ctx.send(bot_name + " has been turned ON")

# @bot.event
# async def bot_info(self):
#     pass

# @bot.event
# async def set_reminder_count(ctx, count):
#     reminder_count = count

# @bot.event
# async def set_reminder_min_interval(ctx, interval):
#     reminder_min_interval = interval

# bot.run(bot_token)


