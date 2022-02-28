import os
import keep_alive
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
    channel = client.get_channel(902921719717691392)
    await channel.send(f'`[{time.localtime().tm_year} 年 {time.localtime().tm_mon} 月 {dayset} 日 {hourset} 點 {time.localtime().tm_min} 分 {time.localtime().tm_sec} 秒]` <a:yes:924484995727372298>機器人已開啟')
    while True:
      hourset = time.localtime().tm_hour
      hourset += 8
      dayset = time.localtime().tm_mday
      if hourset > 24:
        hourset -= 24
        dayset += 1
      channel = client.get_channel(921708850615304192)
      message = await channel.fetch_message(921708924355358750)
      embed=discord.Embed(title="現在時間", description=f"{time.localtime().tm_year} 年 {time.localtime().tm_mon} 月 {dayset} 日 {hourset} 點 {time.localtime().tm_min} 分 {time.localtime().tm_sec} 秒", color=0xc8ff00)
      embed.set_footer(text="每10秒更新一次(只要機器人還活著)")
      await message.edit(embed=embed)
      await asyncio.sleep(10)

@client.event
async def on_message_delete(message):
  if message.author.id == 652938911642943498:
    return
  if message.guild.id == 879352540641255436:
    channel = client.get_channel(923204151050108968)
    embed=discord.Embed(title='訊息刪除', description=message.content, color=0xe22400)
    embed.add_field(name="作者：", value=message.author, inline=True)
    embed.add_field(name="頻道：", value=f'<#{message.channel.id}>({message.channel.id})', inline=True)
    await channel.send(embed=embed)
  if message.guild.id == 879352540641255436 or message.guild.id == 760478047047778337:
    if message.mentions != []:
      if message.author.bot:
        return
      embed=discord.Embed(title='發現ghost ping', description=f'{message.author.mention} 這樣不行喔', color=0xe22400)
      for i in message.mentions:
        embed.add_field(name="受害者：", value=i, inline=True)
      await message.channel.send(embed=embed)
  if message.channel.id == 901846613193007144:
    f = open('數數字id.txt', 'r')
    f = f.read()
    if message.id == int(f):
      if str.isdigit(message.content):
        await message.channel.send(f'<@{message.author.id}> 刪掉了他數的數字就跑，誇張欸\n他數了 {message.content}，下一個數字是 {int(message.content) + 1}')

@client.event
async def on_message_edit(before, after):
  if before.author.bot:
    return
  if before.guild.id == 879352540641255436:
    channel = client.get_channel(923204151050108968)
    embed=discord.Embed(title='訊息編輯', description=f'之前：{before.content}\n現在：{after.content}')
    embed.add_field(name="作者：", value=before.author, inline=True)
    embed.add_field(name="連結：", value=f'https://discord.com/channels/{before.guild.id}/{before.channel.id}/{before.id}', inline=True)
    await channel.send(embed=embed)

@client.event
async def on_member_join(member):
  if member.guild.id == 879352540641255436:
    channel = client.get_channel(881428719640653834)
    embed=discord.Embed(title="成員加入", description=f"歡迎 <@{member.id}> 加入木呱國\n請去<#888675405618372608> 領身分組喔", color=0xf5ec00)
    embed.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed)

@client.event
async def on_member_remove(member):
  if member.guild.id == 879352540641255436:
    channel = client.get_channel(881428719640653834)
    embed=discord.Embed(title="成員離開", description=f"拜拜 <@{member.id}> ，他離開了木呱國", color=0xf5ec00)
    embed.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed)

維修 = True
@client.event
#當有訊息時
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return
    if message.author.bot:
        return
    if ("https://disocrds.gift/" in message.content) or ("https://discorld.gift/" in message.content) or ("https://discosb.gift/" in message.content):
      await message.delete()
      await message.channel.send(f'> ⚠️ 發現經回報的詐騙連結\n> <a:yes:924484995727372298> 已刪除訊息\n> 訊息作者 <@{message.author.id}>\n(哈，笑死，你居然相信這個東西)')
    if ("<@" in message.content) and ("690557429523546143>" in message.content):
      await message.reply('他人不在，有什麼事請等待他')
    if message.content.startswith('<>'):
      f = open('木呱機器人指令紀錄.txt', "a+")
      hourset = time.localtime().tm_hour
      hourset += 8
      dayset = time.localtime().tm_mday
      if hourset > 24:
        hourset -= 24
        dayset += 1
      f.write(f'【{message.guild.name}】[{time.localtime().tm_year} 年 {time.localtime().tm_mon} 月 {dayset} 日 {hourset} 點 {time.localtime().tm_min} 分 {time.localtime().tm_sec} 秒] {message.author} 使用指令 {message.content} \n——————————\n')    
      f.close()
    if message.content.startswith('!!!'):
      f = open('伺服器小助手v.1指令紀錄.txt', "a+")
      hourset = time.localtime().tm_hour
      hourset += 8
      dayset = time.localtime().tm_mday
      if hourset > 24:
        hourset -= 24
        dayset += 1
      f.write(f'【{message.guild.name}】[{time.localtime().tm_year} 年 {time.localtime().tm_mon} 月 {dayset} 日 {hourset} 點 {time.localtime().tm_min} 分 {time.localtime().tm_sec} 秒] {message.author} 使用指令 {message.content} \n——————————\n')
      f.close()
    if message.content == '<>help':
        await message.channel.send('使用此指令需嵌入權限，若沒出現，請允許機器人嵌入')
        embed=discord.Embed(title="指令列表", description="我教你用指令\n**[]代表必須** **()可有可無**", color=0xfefb41)
        embed.add_field(name="<>help", value="顯示指令列表", inline=False)
        embed.add_field(name="<>say [你想讓機器人說的話]", value="讓機器人說出妳想說的話", inline=False)
        embed.add_field(name="<>ip", value="查詢木呱國的ip", inline=False)
        embed.add_field(name="<>ping", value="查詢機器人的延遲", inline=False)
        embed.add_field(name="<>discord", value="取得木呱國discord群組連結", inline=False)
        embed.add_field(name="<>invite", value="邀請這個機器人", inline=False)
        embed.add_field(name="<>server-info", value="查看當前伺服器資訊", inline=False)
        embed.add_field(name="<>user-info", value="取得你的個人資料", inline=False)
        embed.add_field(name="<>join", value="讓機器人加入你現在在的語音頻道(但是不能播音樂)", inline=False)
        embed.add_field(name="<>Rick roll", value="讓機器人Rick roll你", inline=False)
        embed.add_field(name="<>time", value="讓機器人告訴你現在時間", inline=False)
        embed.add_field(name="<>回報 [你要回報的問題]", value="回報問題", inline=False)
        embed.add_field(name="<>embed [標題] [內容]", value="讓機器人創建一個嵌入", inline=False)
        embed.add_field(name="<>server", value="查看木呱國狀態", inline=False)
        embed.add_field(name="<>pe-server", value="查看木呱國(基岩版)狀態", inline=False)
        embed.add_field(name="<>poll [要投票的東西] [選項1] [選項2] (選項3～10)", value="發起投票", inline=False)
        await message.channel.send(embed=embed)
    if message.content == '<>ip':
        await message.channel.send('木呱國ip\njava版:\npeterserver.tk\n基岩版:\nip:pe.peterserver.tk\n軸:10365')
    if message.content == '<>invite':
        embed=discord.Embed(title="邀請連結", description="[點我邀請](https://discord.com/api/oauth2/authorize?client_id=900738619227119627&permissions=536870911991&scope=bot%20applications.commands)", color=0xfefb41)
        await message.channel.send(embed=embed)
    if message.content == '<>discord':
        await message.channel.send('https://discord.gg/m5NQGqd9HB')
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
    if message.content == '<>刷新':
      if message.author.id == 690557429523546143:
        dm = await message.channel.send('正在刷新中⋯')
        status_w = discord.Status.online
        activity_w = discord.Activity(type=discord.ActivityType.playing, name=f"<>help | 在{len(client.guilds)}個伺服器")
        await client.change_presence(status= status_w, activity=activity_w)
      else:
        await message.channel.send('你沒有使用這個指令的權限')
    if message.content == '<>user-info':
      embed=discord.Embed(title=f"{message.author}的資料", color=0xffc5ab)
      embed.add_field(name="名稱：", value=f"{message.author}", inline=False)
      embed.add_field(name="暱稱：", value=f"{message.author.nick}", inline=False)
      embed.add_field(name="Discord id：", value=f"{message.author.id}", inline=False)
      embed.add_field(name="帳號創建時間：", value=f"{message.author.created_at}", inline=False)
      embed.set_thumbnail(url=f'{message.author.avatar_url}')
      await message.channel.send(embed=embed)
    if message.content == '<>list-server':
      if message.author.id == 690557429523546143:
        guilds = await client.fetch_guilds(limit=50).flatten()
        #遍尋 guild
        mc = ' '
        for i in guilds:
            #由於我們只要 guilds 的name 就好，當然也可以獲取 id~
            mc = f'{mc}\n{i.name}\n{i.id}'
        embed=discord.Embed(title=f"伺服器列表({len(client.guilds)}個伺服器中)", description=mc)
        await message.channel.send(embed=embed)
      else:
          await message.channel.send('你沒有使用這個指令的權限')
    if message.content == '<>list-server-2':
      if message.author.id == 690557429523546143:
        guilds = await client.fetch_guilds(limit=100).flatten()
        #遍尋 guild
        mc = ' '
        m = 0
        for i in guilds:
            #由於我們只要 guilds 的name 就好，當然也可以獲取 id~
          m += 1
          if m > 50:
            mc = f'{mc}\n{i.name}\n{i.id}'
        embed=discord.Embed(title=f"伺服器列表({len(client.guilds)}個伺服器中)", description=mc)
        await message.channel.send(embed=embed)
      else:
          await message.channel.send('你沒有使用這個指令的權限')
    if message.content == '<>join':
      await message.author.voice.channel.connect()
    if message.content.startswith('<>start'):
      tmp = message.content.split(" ",1)
      if len(tmp) == 1:
        await message.channel.send(f"{message.author.mention} 使用方式:<>start [抽獎獎項]")
      else:
        if message.author.id == 690557429523546143:
          embed=discord.Embed(title=f"{tmp[1]}", description=f"按下 🎉 來抽獎!\n結束時間: 天知道\n抽獎創建者: {message.author.mention}", color=0xfbff00)
          embed.set_footer(text="結束於 | 天知道")
          cool = await message.channel.send(content="🎉抽獎開始🎉" ,embed=embed)
          await cool.add_reaction("🎉")
        else:
          await message.channel.send('你沒有使用這個指令的權限')
    if message.channel == client.get_channel(901679794415075388):
        await message.delete()
        embed=discord.Embed(title="木呱牌願望實現器", description=f"{message.content}", color=0xff8800)
        embed.set_footer(text=f"許願者:{message.author.display_name}")
        embed.set_thumbnail(url=f'{message.author.avatar_url}')
        ok = await message.channel.send(embed=embed)
        await ok.add_reaction("<a:yes:924484995727372298>")
        await ok.add_reaction("<a:no:924485048009392149>")
    if message.channel == client.get_channel(901846613193007144):
      if message.author.bot:
        return
      f = open('數數字.txt', 'r')
      n = f.read()
      f.close()
      if message.content == n:
        f = open('數數字作者.txt', 'r')
        a = f.read()
        f.close()
        if f'{message.author.id}' == a:
          await message.add_reaction("<a:no:924485048009392149>")
          f = open('數數字.txt', 'w')
          f.write('1')
          await message.channel.send(f'欸，我們好不容易才數到{n} ，<@{message.author.id}> 都你害的啦，又要從1開始了 (一個人只能連續數一個數)')
          f.close()
          f = open('數數字作者.txt', 'w')
          f.close()
        else:
          await message.add_reaction("<a:yes:924484995727372298>")
          n1 = int(n)
          n1 = n1 + 1
          f = open('數數字.txt', 'w')
          f.write(f'{n1}')
          f.close()
          f = open('數數字作者.txt', 'w')
          f.write(f'{message.author.id}')
          f.close()
          f = open('數數字id.txt', 'w')
          f.write(f'{message.id}')
          f.close()
      elif str.isdigit(message.content):
        await message.add_reaction("<a:no:924485048009392149>")
        f = open('數數字.txt', 'w')
        f.write('1')
        await message.channel.send(f'欸，我們好不容易才數到{n} ，<@{message.author.id}> 都你害的啦，又要從1開始了')
        f.close()
        f = open('數數字作者.txt', 'w')
        f.close()
    if ("<@!900738619227119627>" in message.content):
       await message.reply('輸入 <>help 來查看指令') 
    if ("<@900738619227119627>" in message.content):
        await message.reply('輸入 <>help 來查看指令') 
    if message.content == '<>RIP':
        message = await message.channel.send(f'<a:yes:924484995727372298>上香成功 - {message.author}')
    if message.content == '<>tag':
      if message.author.id == 690557429523546143:
        await message.delete()
        await message.channel.send('偷偷tag<@676328108865093643>')
      else:
        await message.channel.send('你沒有使用這個指令的權限')
    if message.content == '<>酷欸':
      if message.author.id == 690557429523546143:
        await message.delete()
        await message.channel.send('笑死')
        await asyncio.sleep(1)
        await message.channel.send('死了')
        await asyncio.sleep(1)
        await message.channel.send('真的')
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
        channel = client.get_channel(906404728689274930)
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
    if message.content == '<>server':
      embed=discord.Embed(title="木呱國狀態", url="https://www.mc-list.xyz/banner/1-573.png")
      await message.reply(embed=embed)
    if message.content == '<>pe-server':
      embed=discord.Embed(title="木呱國(基岩版)狀態", url="https://www.mc-list.xyz/banner/1-728.png")
      await message.reply(embed=embed)
    if message.channel == client.get_channel(881422078945919066):
      await message.add_reaction("🤔")
    if message.content == 'Never Gonna Give You up':
      await message.reply('Never Gonna let U down~')
    if message.content.startswith('<>reply'):
      if message.author.id == 690557429523546143:
      #訊息切一刀
        tmp = message.content.split(" ",2)
        #如果分割後串列長度只有1
        if len(tmp) < 2:
          await message.channel.send("要兩個啦")
        #否則
        else:
          message = await message.channel.fetch_message(tmp[1])
          await message.reply(tmp[2])
      else:
        await message.reply('你沒權限啦')
    if message.content.startswith('<>edit'):
      if message.author.id == 690557429523546143:
      #訊息切一刀
        tmp = message.content.split(" ",2)
        #如果分割後串列長度只有1
        if len(tmp) < 2:
          await message.channel.send("要兩個啦")
        #否則
        else:
          message = await message.channel.fetch_message(tmp[1])
          await message.edit(content=tmp[2])
      else:
        await message.reply('你沒權限啦')
    if message.content.startswith('<>poll'):
      tmp = message.content.split(" ",1)
      if len(tmp) == 1:
        return
      tmp = tmp[1].split(" ",1)
      if len(tmp) == 1:
        return
      back = tmp[0]
      tmp = tmp[1].split(" ",9)
      #如果分割後串列長度只有1
      if len(tmp) < 2:
        await message.channel.send('用法：<>poll [要投票的東西] [選項1] [選項2] (選項3～10)')
      else:
        選項 = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']
        c = 0
        pl = ' '
        for poll in tmp:
          pl = f'{pl}\n{選項[c]}：{poll}'
          c += 1
        embed=discord.Embed(title=f"{back}", description=pl)
        embed.set_footer(text=f"{message.author} 發出的投票")
        copy = await message.channel.send(embed=embed)
        b = -1
        while c > 0:
          c -= 1
          b += 1
          await copy.add_reaction(選項[b])
    if message.channel.id == 903629842065522719:
      if message.author.id == 676328108865093643:
        if ("Traceback (most recent call last):" in message.content):
          await message.reply("在你問這個錯誤前，有沒有想過先翻譯一下呢，<#868411819654520913> 是你的最好選擇")
    if message.content == '<>test':
        await message.reply("...")
    if message.content.startswith('<>channel-say'):
      if message.author.id == 690557429523546143:
      #訊息切一刀
        tmp = message.content.split(" ",2)
        #如果分割後串列長度只有1
        if len(tmp) < 2:
          await message.channel.send("要兩個啦")
        #否則
        else:
          channel = client.get_channel(int(tmp[1]))
          await channel.send(tmp[2])
      else:
        await message.reply('你沒權限')
    if message.content.startswith('<>channel-emoji'):
      if message.author.id == 690557429523546143:
      #訊息切一刀
        tmp = message.content.split(" ",3)
        #如果分割後串列長度只有1
        if len(tmp) < 2:
          await message.channel.send("要三個啦")
        #否則
        else:
          message = await client.get_channel(int(tmp[1])).fetch_message(tmp[2])
          await message.add_reaction(tmp[3])
      else:
        await message.reply('你沒權限啦')
    if message.content.startswith('<>guild-leave'):
      if message.author.id == 690557429523546143:
        tmp = message.content.split(" ",1)
        if len(tmp) == 1:
          await message.channel.send("我要退出甚麼")
        #否則
        else:
          guild = discord.utils.get(client.guilds, id=int(tmp[1]))
          if guild == None:
            await message.channel.send('我不在那裡!')
          else:
            await guild.leave()
            await message.channel.send(f"成功退出 {guild.name} ({guild.id})")
            channel = client.get_channel(921608140712210493)
            embed=discord.Embed(title="強制退出", description=f"強制退出，機器人還在{len(client.guilds)}個群組", color=0xff2600)
            embed.add_field(name="名稱：", value=guild, inline=True)
            embed.add_field(name="id：", value=guild.id, inline=True)
            await channel.send(embed=embed)

@client.event
async def on_guild_join(guild):
  channel = client.get_channel(921608140712210493)
  embed=discord.Embed(title="機器人群組加入", description=f"他邀請了這個機器人，機器人就在{len(client.guilds)}個群組了!", color=0x00ff88)
  embed.add_field(name="名稱：", value=guild, inline=True)
  embed.add_field(name="id：", value=guild.id, inline=True)
  await channel.send(embed=embed)
  status_w = discord.Status.online
  activity_w = discord.Activity(type=discord.ActivityType.playing, name=f"<>help | 在{len(client.guilds)}個伺服器")
  await client.change_presence(status= status_w, activity=activity_w)

@client.event
async def on_guild_remove(guild):
  channel = client.get_channel(921608140712210493)
  embed=discord.Embed(title="機器人群組離開", description=f"他踢了這個機器人，機器人就只在{len(client.guilds)}個群組了qwq", color=0xff2600)
  embed.add_field(name="名稱：", value=guild, inline=True)
  embed.add_field(name="id：", value=guild.id, inline=True)
  await channel.send(embed=embed)
  status_w = discord.Status.online
  activity_w = discord.Activity(type=discord.ActivityType.playing, name=f"<>help | 在{len(client.guilds)}個伺服器")
  await client.change_presence(status= status_w, activity=activity_w)

@client.event
async def on_voice_state_update(member, before, after):
  if after.channel != None and before.channel != None:
    if before.channel == after.channel:
      return
    if before.channel.name == f'{member} 的語音頻道':
      await before.channel.delete()
  if after.channel != None:
    if after.channel.guild.id == 879352540641255436:
      if after.channel.id == 924204652524888065:
        channel = discord.utils.get(after.channel.guild.categories, name='木呱機器人臨時語音')
        channel = await after.channel.guild.create_voice_channel(name=f'{member} 的語音頻道', category=channel)
        await member.move_to(channel)
  else:
    if before.channel.guild.id == 879352540641255436:
      if before.channel.name == f'{member} 的語音頻道':
        await before.channel.delete()

keep_alive.keep_alive()

client.run(os.environ['TOKEN']) #TOKEN在剛剛Discord Developer那邊「BOT」頁面裡面
