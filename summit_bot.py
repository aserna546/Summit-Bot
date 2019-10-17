import discord

client = discord.Client()

async def change_role(roles: list, user, add, name: str):
  """
  boolean add if true adds roles otherwise removes
  """
  role = discord.utils.get(roles, name=f'{name}')
  if role is not None:
    if add:
      await user.add_roles(role)
    else:
      await user.remove_roles(role)

reactions = {
  '❤': 'Terminus of Time',
  '💟': 'Blackshard Nexus',
  '💙': 'Azure Flux',
  '💚': 'Emerald Prison',
  'PinkBean': 'Pink Bean',
  'Frostpillar': 'Frostpillar Temple',
  'Spire': 'Madrakan Spire',
  '🐋': 'Guardian of the Seas',
  'mermaid': 'The Song of the Oracle',
  '❄': 'Icethorn Ridge',
  '👻': 'Malevolent Manor',
  '🤖': 'Madrakan Ramparts',
  '😈': "Madrakan's Heart",
  '🐒': 'Berserker',
  '🔥': 'Striker',
  '1⃣': 'Archer',
  '2⃣': 'Assassin',
  '3⃣': 'Heavy Gunner',
  '4⃣': 'Knight',
  '5⃣': 'Priest',
  '6⃣': 'Runeblade',
  '7⃣': 'Soul Binder',
  '8⃣': 'Thief',
  '9⃣': 'Wizard',
  '🎧': 'DJ',
  'Summit': 'Xenon',
  'CarryMe': 'Dungeon Alt',
  '💃': 'Guild DDS',
  'Cpap': 'Level 50 Raids'
  
}

@client.event
async def on_raw_reaction_add(reaction): 
  channel = await client.fetch_channel(reaction.channel_id)
  if channel.name == 'raid-roles':
    role_list = channel.guild.roles
    #print(reaction.emoji.name)
    member = channel.guild.get_member(reaction.user_id)
    role_name = reactions.get(reaction.emoji.name)
    await change_role(role_list, member, True, role_name)

@client.event
async def on_raw_reaction_remove(reaction):
  channel = await client.fetch_channel(reaction.channel_id)
  if channel.name == 'raid-roles':
    role_list = channel.guild.roles
    #print(reaction.emoji.name)
    member = channel.guild.get_member(reaction.user_id)
    role_name = reactions.get(reaction.emoji.name)
    await change_role(role_list, member, False, role_name)

@client.event
async def on_member_join(member):
  role = discord.utils.get(member.guild.roles, name='Unverified')
  await member.add_roles(role)

@client.event
async def on_member_remove(member):
  channel = discord.utils.get(member.guild.text_channels, name='users-joining')
  await channel.send(f'{member.display_name} has left the server.')
client.run('NjMzMDgwMDk2OTUzMDczNjY1.XaQStg.AUDx5w1O8xfcNPnZbhNmzPHZYgY')
