import os
#導入Discord.py
import discord
import asyncio
import random
import datetime
import time
#client是我們與Discord連結的橋樑
intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.voice_states = True
client = discord.Client(intents=intents)
#調用event函式庫
@client.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：',client.user)
    status_w = discord.Status.online
    activity_w = discord.Activity(type=discord.ActivityType.playing, name=f"<>help | 在{len(client.guilds)}個伺服器")
    await client.change_presence(status= status_w, activity=activity_w)
    hourset = time.localtime().tm_hour
    hourset += 8
    dayset = time.localtime().tm_mday
    if hourset > 24:
      hourset -= 24
      dayset += 1
    channel = client.get_channel(902921719717691392) #機器人啟動通知頻道
    await channel.send(f'`[{time.localtime().tm_year} 年 {time.localtime().tm_mon} 月 {dayset} 日 {hourset} 點 {time.localtime().tm_min} 分 {time.localtime().tm_sec} 秒]` <a:yes:924484995727372298>機器人已開啟')
    while True:
      hourset = time.localtime().tm_hour
      hourset += 8 #條時差
      dayset = time.localtime().tm_mday
      if hourset > 24:
        hourset -= 24
        dayset += 1
      channel = client.get_channel(921708850615304192) #這裡可以改成你頻道的id
      message = await channel.fetch_message(921708924355358750) #讓機器人在那頻道發一條訊息，然後id填入這裡
      embed=discord.Embed(title="現在時間", description=f"{time.localtime().tm_year} 年 {time.localtime().tm_mon} 月 {dayset} 日 {hourset} 點 {time.localtime().tm_min} 分 {time.localtime().tm_sec} 秒", color=0xc8ff00)
      embed.set_footer(text="每10秒更新一次(只要機器人還活著)")
      await message.edit(embed=embed)
      await asyncio.sleep(10) #等待10秒

@client.event
async def on_member_join(member):
  if member.guild.id == 879352540641255436: #群組id
    channel = client.get_channel(881428719640653834) #通知頻道id
    embed=discord.Embed(title="成員加入", description=f"歡迎 <@{member.id}> 加入 (群組名稱)", color=0xf5ec00)
    embed.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed)

@client.event
async def on_member_remove(member):
  if member.guild.id == 879352540641255436: #群組id
    channel = client.get_channel(881428719640653834) #通知頻道id
    embed=discord.Embed(title="成員離開", description=f"拜拜 <@{member.id}> ，他離開了 (群組名稱)", color=0xf5ec00)
    embed.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed)

@client.event
#當有訊息時
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return
    if message.author.bot:
        return
    if message.content.startswith('<>'): #訊息內容開始為<>?
      f = open('木呱機器人指令紀錄.txt', "a+") #打開檔案
      hourset = time.localtime().tm_hour
      hourset += 8 #條時差
      dayset = time.localtime().tm_mday
      if hourset > 24:
        hourset -= 24
        dayset += 1
      f.write(f'【{message.guild.name}】[{time.localtime().tm_year} 年 {time.localtime().tm_mon} 月 {dayset} 日 {hourset} 點 {time.localtime().tm_min} 分 {time.localtime().tm_sec} 秒] {message.author} 使用指令 {message.content} \n——————————\n') #寫入檔案    
      f.close()
    if message.content == '<>help':
        await message.channel.send('使用此指令需嵌入權限，若沒出現，請允許機器人嵌入')
        embed=discord.Embed(title="指令列表", description="我教你用指令\n**[]代表必須** **()可有可無**", color=0xfefb41)
        embed.add_field(name="<>help", value="顯示指令列表", inline=False)
        embed.add_field(name="<>say [你想讓機器人說的話]", value="讓機器人說出妳想說的話", inline=False)
        embed.add_field(name="<>ping", value="查詢機器人的延遲", inline=False)
        embed.add_field(name="<>invite", value="邀請這個機器人", inline=False)
        embed.add_field(name="<>server-info", value="查看當前伺服器資訊", inline=False)
        embed.add_field(name="<>user-info", value="取得你的個人資料", inline=False)
        embed.add_field(name="<>join", value="讓機器人加入你現在在的語音頻道(但是不能播音樂)", inline=False)
        embed.add_field(name="<>Rick roll", value="讓機器人Rick roll你", inline=False)
        embed.add_field(name="<>time", value="讓機器人告訴你現在時間", inline=False)
        embed.add_field(name="<>回報 [你要回報的問題]", value="回報問題", inline=False)
        embed.add_field(name="<>embed [標題] [內容]", value="讓機器人創建一個嵌入", inline=False)
        await message.channel.send(embed=embed)
    if message.content == '<>invite':
        embed=discord.Embed(title="邀請連結", description="[點我邀請](https://discord.com/api/oauth2/authorize?client_id=900738619227119627&permissions=536870911991&scope=bot%20applications.commands)", color=0xfefb41)
        await message.channel.send(embed=embed)
    if message.content == '<>ping':
        message = await message.channel.send(f'pong')
        await asyncio.sleep(0.1)
        await message.edit(content=f"延遲為 {round(client.latency * 1000)}ms")
    #如果以「<>say」開頭
    if message.content.startswith('<>say'):
      #訊息切一刀
      tmp = message.content.split(" ",1)
      #如果分割後串列長度只有1
      if len(tmp) == 1:
        await message.channel.send("使用方式：<>say 你要讓機器人說的話")
      #否則
      else:
        await message.channel.send(tmp[1])
    if message.content == '<>server-info':
      embed=discord.Embed(title="此伺服器的資訊", color=0x00ff88)
      embed.set_thumbnail(url=f'{message.guild.icon_url}')
      embed.add_field(name=f"伺服器名稱：", value=f"{message.guild.name}", inline=False)
      embed.add_field(name=f"伺服器人數：", value=f"{message.guild.member_count}人", inline=False)
      embed.add_field(name=f"擁有者：", value=f"<@{message.guild.owner_id}>", inline=False)
      embed.add_field(name=f"創建時間：", value=f"{message.guild.created_at}", inline=False)
      await message.channel.send(embed=embed)
    if message.content == '<>user-info':
      embed=discord.Embed(title=f"{message.author}的資料", color=0xffc5ab)
      embed.add_field(name="名稱：", value=f"{message.author}", inline=False)
      embed.add_field(name="暱稱：", value=f"{message.author.nick}", inline=False)
      embed.add_field(name="Discord id：", value=f"{message.author.id}", inline=False)
      embed.add_field(name="帳號創建時間：", value=f"{message.author.created_at}", inline=False)
      embed.set_thumbnail(url=f'{message.author.avatar_url}')
      await message.channel.send(embed=embed)
    if message.content == '<>Rick roll':
        await message.channel.send('https://imgur.com/NQinKJB')
    if message.content == '<>time':
        #條時差
        hourset = time.localtime().tm_hour
        hourset += 8
        dayset = time.localtime().tm_mday
        if hourset > 24:
          hourset -= 24
          dayset += 1
        await message.channel.send(f'現在時間：`{time.localtime().tm_year} 年 {time.localtime().tm_mon} 月 {dayset} 日 {hourset} 點 {time.localtime().tm_min} 分 {time.localtime().tm_sec} 秒`')
    if message.content.startswith('<>回報'):
      tmp = message.content.split(" ",1)
      #如果分割後串列長度只有1
      if len(tmp) == 1:
        await message.channel.send("使用方式：<>回報 [你要回報的問題]")
      else:
        embed=discord.Embed(title="錯誤回報", description=f"錯誤：{tmp[1]}", color=0xff0000)
        embed.add_field(name="回報者", value=f"{message.author}．`{message.author.id}`", inline=False)
        channel = client.get_channel(906404728689274930) #回報頻道id
        await channel.send(embed=embed)
        await message.reply('你的問題已經成功回報')
    if message.content.startswith('<>embed'):
      tmp = message.content.split(" ",2)
      #如果分割後串列長度只有1
      if len(tmp) < 2:
        await message.channel.send("使用方式：<>embed [標題] [內容]")
      else:
        embed=discord.Embed(title=tmp[1], description=tmp[2], color=0xfefb41)
        embed.set_footer(text=f"發送者：{message.author}")
        await message.channel.send(embed=embed)

client.run(os.environ['TOKEN']) #TOKEN在剛剛Discord Developer那邊「BOT」頁面裡面
