import asyncio
import csv
import discord
from discord.ext import commands
import os
import time
import datetime
import sys
import idle
import csv_data
#import keep_alive

try:
    intents=discord.Intents.default()
    intents.members=True
    #intents.typing=True
    intents = discord.Intents.all()

    activity=discord.Streaming(name="listening_lofi",url="https://www.youtube.com/watch?v=jfKfPfyJRdk",platform="YouTube")
    main_bot=commands.Bot(command_prefix="+",intents=intents,activity=activity)

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
        i = 0
        while i < 10:
            await asyncio.sleep(60)
            i+=1
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
        now_day = time.strftime("%d")
        now_month = time.strftime("%m")
        now_year = time.strftime("%Y")
        try:
            with open(f"{ctx.author}.csv", mode="r", newline="") as file:
                reader = csv.reader(file)
                rows = list(reader)
                temp = 0
                temp_list = []
                print("temp_on", temp)
                if temp != 4:  #only get first 4 data(as know as name, diamonds, and netherite_ingot, combo)
                    print("temp_less_then_four", temp)
                    print("reader: ", reader)
                    if not rows or len(rows) < 4:
                        with open(f"{ctx.author}.csv", mode="w", newline="") as file:
                                print("test")
                                writer = csv.writer(file)
                                writer.writerow([ctx.author])
                                writer.writerow([0])
                                writer.writerow([0])
                                writer.writerow([0])
                                temp_list = [
                                    [ctx.author],
                                    [0],
                                    [0],
                                    [0]
                                ]
                    else:
                        # Extract data from the first 4 rows
                        temp_list = rows[:4]
                        print("temp_list: ", temp_list)  
            print("ctx.author: ", ctx.author)     
            username = csv_data.csv_use(temp_list[0][0], now_day, now_month, now_year, temp_list[1][0], temp_list[2][0], temp_list[3][0])
        
        except FileNotFoundError:
            with open(f"{ctx.author}.csv", 'w', newline='') as file:
                pass

            with open(f"{ctx.author}.csv", mode="r", newline="") as file:
                reader = csv.reader(file)
                rows = list(reader)
                temp = 0
                temp_list = []
                print("temp_on", temp)
                if temp != 4:  #only get first 4 data(as know as name, diamonds, and netherite_ingot, combo)
                    print("temp_less_then_four", temp)
                    print("reader: ", reader)
                    if not rows or len(rows) < 4:
                        with open(f"{ctx.author}.csv", mode="w", newline="") as file:
                                print("test")
                                writer = csv.writer(file)
                                writer.writerow([ctx.author])
                                writer.writerow([0])
                                writer.writerow([0])
                                writer.writerow([0])
                                temp_list = [
                                    [ctx.author],
                                    [0],
                                    [0],
                                    [0]
                                ]
                    else:
                        # Extract data from the first 4 rows
                        temp_list = rows[:4]
                        print("temp_list: ", temp_list)  
            print("ctx.author: ", ctx.author)     
            username = csv_data.csv_use(temp_list[0][0], now_day, now_month, now_year, temp_list[1][0], temp_list[2][0], temp_list[3][0])
                
        if username.read_data() is True:
            await ctx.send("`{}`你已簽到成功! 獲得2鑽石~".format(ctx.author))
        else:
            await ctx.send("你已经成功签到了，等待下一个日出的到来吧")

    main_bot.add_command(sign)

    @commands.command()
    async def calculat(ctx):
        username = csv_data.csv_use(ctx.author)
        username.calculate()


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
    main_bot.run("MTIwNjQ0NTc0MzQ4NTg4NjU2Ng.GwR5CV.f5GKJT12sgNruT1lm2iYoD18HlXA9EZtZN5pHc", reconnect=True)

#keep_alive.keep_alive()
main_bot.run("token", reconnect=True)
