Client = discord.Client()
client = commands.Bot(command_prefix = "no")

@client.event
async def on_ready():
    print("I'm online, ya eggface!")
        
            
            @client.event
            async def on_message(message):
              print(message.content)
                if message.content.upper().startswith("RINGS!"):
                    await client.send_message(message.channel, "You can never have too many rings!")
                        
                          if message.content.upper().startswith("BOUNCEPAD?"):
                              await client.send_message(message.channel, "Bouncepad!")
                                  
                                    if message.content.upper().startswith("MORE RINGS!"):
                                        await client.send_message(message.channel, "It's like they're drawn to me!")
                                            
                                              if message.content.upper().startswith("PRETEND, OK?"):
                                                  await client.send_message(message.channel, "Yeah, just for a second, pretend i'm not online.")
                                                    
                                                      if message.content.upper().startswith("I DON'T LIKE YOU."):
                                                          await client.send_message(message.channel, "How to say this delicately... You're a horrible member and no one in this server likes you.")
                                                              
                                                                if message.content.upper().startswith("THAT'S PRETTY EDGY."):
                                                                      await client.send_message(message.channel, "Being a role model is overrated. I much rather be... hilariously edgy.")
                                                                            
                                                                            
                                                                            client.run("BOT_TOKEN")
