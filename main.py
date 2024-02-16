import asyncio
import csv
import discord
from discord.ext import commands
import os
import time
import sys
import csv_data
import tracemalloc
#import keep_alive

try:
    tracemalloc.start()
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('traceback')
    intents=discord.Intents.default()
    intents.members=True
    #intents.typing=True
    intents = discord.Intents.all()
    activity=discord.Streaming(name="listening_lofi",url="https://www.youtube.com/watch?v=jfKfPfyJRdk",platform="YouTube")
    main_bot=commands.Bot(command_prefix="/",intents=intents,activity=activity)

    @main_bot.event
    async def on_ready():
        print("ready")

    @main_bot.event
    async def on_connect():
        print("==========================================")
        print("bot on connect")
        print("==========================================")

    @main_bot.event
    async def on_disconnect():
        print("bot disconnect")
        await asyncio.sleep(60)
        main_bot.run("MTIwNjQ0NTc0MzQ4NTg4NjU2Ng.GwR5CV.f5GKJT12sgNruT1lm2iYoD18HlXA9EZtZN5pHc", reconnect=True)

    @main_bot.event
    async def on_member_join(member):
        channel = main_bot.get_channel(1197122873492508776)
        guild = main_bot.get_guild(1197122873492508773)
        member_self_intro_channel = 1197184348332499075
        guild_rule = 1197184304690765947
        embed = discord.Embed(title = F"欢迎`{member}`加入靜謐湖畔！〃•̀ꇴ•〃")
        embed.add_field(name="还请记得填写`团员自我介绍`🤩", value=F"<#{member_self_intro_channel}>", inline=False)
        embed.add_field(name="也别忘了遵守团规！★~★", value=F"<#{guild_rule}>", inline=False)
        await channel.send(embed=embed)
        guild=main_bot.get_guild(member.guild.id)
        role = guild.get_role(1197206948978905138)
        await member.add_roles(role)

    @main_bot.event
    async def on_member_remove(member):
        member_join_time = member.joined_at.strftime('%Y, %m, %d')
        member_leave_time = time.strftime('%Y, %m, %d')
        channel = main_bot.get_channel(1197122873492508776)
        embed = discord.Embed(title = F"`{member}`离开了靜謐湖畔")
        embed.add_field(name="加入时间", value=F"{member_join_time}", inline=False)
        embed.add_field(name="离开时间", value=F"{member_leave_time}", inline=False)
        await channel.send(embed=embed)




    @commands.command()
    async def sign(ctx):
        try:
            author_name_check = str(ctx.author)
            author_name_check = list(author_name_check)
            author_name_correct = ctx.author
            if author_name_check[len(author_name_check) - 2] != "#":
                author_name_correct = f"{ctx.author}#0"

            with open(f"{author_name_correct}.csv", mode="r", newline="") as file:
                reader = csv.reader(file)
                rows = list(reader)
                temp = 0
                temp_list = []
                print(author_name_correct)
                print("temp_on", temp)
                if temp != 4:  #only get first 4 data(as know as name, diamonds, and netherite_ingot, combo)
                    print("temp_less_then_four", temp)
                    print("reader: ", reader)
                    if not rows or len(rows) < 4:
                        with open(f"{author_name_correct}.csv", mode="w", newline="") as file:
                                print("test")
                                writer = csv.writer(file)
                                writer.writerow([author_name_correct])
                                writer.writerow([0])
                                writer.writerow([0])
                                writer.writerow([0])
                                temp_list = [
                                    [author_name_correct],
                                    [0],
                                    [0],
                                    [0]
                                ]
                    else:
                        # Extract data from the first 4 rows
                        temp_list = rows[:4]
                        print("temp_list: ", temp_list)  
            now_day = time.strftime("%d")
            now_month = time.strftime("%m")
            now_year = time.strftime("%Y")
            print("ctx.author: ", author_name_correct)     
            username = csv_data.csv_use(temp_list[0][0], now_day, now_month, now_year, temp_list[1][0], temp_list[2][0], temp_list[3][0])
        
        except FileNotFoundError:
            with open(f"{author_name_correct}.csv", 'w', newline='') as file:
                pass

            with open(f"{author_name_correct}.csv", mode="r", newline="") as file:
                reader = csv.reader(file)
                rows = list(reader)
                temp = 0
                temp_list = []
                print("temp_on", temp)
                if temp != 4:  #only get first 4 data(as know as name, diamonds, and netherite_ingot, combo)
                    print("temp_less_then_four", temp)
                    print("reader: ", reader)
                    if not rows or len(rows) < 4:
                        with open(f"{author_name_correct}.csv", mode="w", newline="") as file:
                                print("test")
                                writer = csv.writer(file)
                                writer.writerow([author_name_correct])
                                writer.writerow([0])
                                writer.writerow([0])
                                writer.writerow([0])
                                temp_list = [
                                    [author_name_correct],
                                    [0],
                                    [0],
                                    [0]
                                ]
                    else:
                        # Extract data from the first 4 rows
                        temp_list = rows[:4]
                        print("temp_list: ", temp_list)  
            now_day = time.strftime("%d")
            now_month = time.strftime("%m")
            now_year = time.strftime("%Y")
            print("ctx.author: ", author_name_correct)     
            print("now_day: ", now_day)
            username = csv_data.csv_use(temp_list[0][0], now_day, now_month, now_year, temp_list[1][0], temp_list[2][0], temp_list[3][0])


        #check is user in the list or not
        with open(f"member_list.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            old_data = []
            temp_count = 0
            for row in reader:
                    old_data.append(row)
            
            for i in old_data:    #if user name already exist 
                print("debug_use: ", i)
                if author_name_correct == i[0]:
                    temp_count = 1
                    print("debug_use_old_data: ", old_data)
                    print("user name already exsit")
            
            if temp_count == 0:    #if not, add into list
                with open("member_list.csv", 'w', newline='') as file:
                    writer = csv.writer(file)
                    author = temp_list[0][0]
                    old_data.append([author])
                    print(old_data)
                    writer.writerows(old_data)


        if username.read_data() is True:
            await ctx.send("`{}`你已簽到成功! 獲得2鑽石~".format(author_name_correct))
            return_something = username.calculate()
            if return_something is not None:
                await ctx.send(return_something)
        else:
            await ctx.send("你已经成功签到了，等待下一个日出的到来吧")

    main_bot.add_command(sign)



    @commands.command()
    async def check(ctx, arg):
        try:
            with open(f"{arg}#0.csv", mode="r", newline="") as file:
                    reader = csv.reader(file)
                    rows = list(reader)
                    temp_list = rows[:4]
                    embed = discord.Embed(title = F"**{temp_list[0][0]}**")
                    embed.add_field(name="钻石数: ", value=F"{temp_list[1][0]}", inline=False)
                    embed.add_field(name="狱髓锭: ", value=F"{temp_list[2][0]}", inline=False)
                    await ctx.send(embed=embed)
        except FileNotFoundError:
            await ctx.send("请先使用`/sign`创立数据库, 如若已然创立却仍看见此信息则联系`@qqrey`")


    main_bot.add_command(check)


    @commands.command()
    async def member_list(ctx):
        with open(f"member_list.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            old_data = []
            for row in reader:
                    old_data.append(row)
            embed = discord.Embed(title = "member_list")
            print("old_data", old_data)
            for i in old_data:
                embed.add_field(name = "", value= i[0], inline=False)
            await ctx.send(embed=embed)

    main_bot.add_command(member_list)

    @commands.command()
    async def on_error(ctx):
        if len(top_stats) < 1:
              await ctx.send("there is no error traceback")
        else:
             for stat in top_stats[:len(top_stats) - 1]:
                  await ctx.send(stat)

    main_bot.add_command(on_error)

except Exception as ex:
    sys.path.append(r"C:\Users\User\OneDrive\桌面\error_handle.txt")
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    with open(r"C:\Users\User\OneDrive\桌面\error_handle.txt",mode="r",encoding="utf-8") as file_r:
        rd=file_r.read()
    file_w=open(r"C:\Users\User\OneDrive\桌面\error_handle.txt", mode="w")
    fn=os.path.realpath(__file__)
    zt=time.strftime("%Y")
    zt1=time.strftime("%m")
    zt2=time.strftime("%d")
    zt3=time.strftime("%H")
    zt4=time.strftime("%M")
    zt5=time.strftime("%S")
    file_w.write("{}\n\n{}y{}M{}d,{}h{}m{}s\nerror_msg:{}\nerror_type:{}\nerror_line:{}\ndoc_name:{}\npath:{}".format(rd,zt,zt1,zt2,zt3,zt4,zt5,ex,exc_type, exc_tb.tb_lineno,fname,fn))
    file_w.close()
    #try to let the bot reboot if there is any exception error
    activity=discord.Streaming(name="listening_lofi",url="https://www.youtube.com/watch?v=jfKfPfyJRdk",platform="YouTube")
    main_bot=commands.Bot(command_prefix="+",intents=intents,activity=activity)
    main_bot.run("token", reconnect=True)

#keep_alive.keep_alive()
main_bot.run("token", reconnect=True)