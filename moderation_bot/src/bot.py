# bot.py

import discord
from discord.ext import commands
import moderation_actions
import role_management
import chat_activity_monitoring
import logging
import machine_learning
import integration
import dashboard
import updates_and_bug_fixes

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.command()
async def mute(ctx, member: discord.Member, duration: int):
    await moderation_actions.mute_member(ctx, member, duration)

@client.command()
async def kick(ctx, member: discord.Member, reason: str):
    await moderation_actions.kick_member(ctx, member, reason)

@client.command()
async def ban(ctx, member: discord.Member, reason: str):
    await moderation_actions.ban_member(ctx, member, reason)

@client.command()
async def assign_role(ctx, member: discord.Member, role: discord.Role):
    await role_management.assign_role(ctx, member, role)

@client.command()
async def remove_role(ctx, member: discord.Member, role: discord.Role):
    await role_management.remove_role(ctx, member, role)

@client.event
async def on_message(message):
    await chat_activity_monitoring.monitor_chat(message)
    await client.process_commands(message)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command, please try again.')

client.run('your_token_here')