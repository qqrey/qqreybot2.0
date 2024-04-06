import asyncio
from asyncio import tasks
import csv
import discord
from discord.ext import commands
import os
import time
import sys
import csv_data
import tracemalloc
import datetime
import schedule
import threading
import subprocess
import traceback
#import keep_alive

try:
    starttime = datetime.datetime.now()
    starttimes=time.time()
    tracemalloc.start()
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('traceback')
    intents = discord.Intents.all()
    intents.members=True
    #intents.typing=True
    activity=discord.Streaming(name="listening_lofi",url="https://www.youtube.com/watch?v=jfKfPfyJRdk",platform="YouTube")
    main_bot=commands.Bot(command_prefix="/",intents=intents,activity=activity)

    start_time_all=time.time()

    stzt=time.strftime("%Y")
    stzt1=time.strftime("%m")
    stzt2=time.strftime("%d")
    stzt3=time.strftime("%H")
    stzt4=time.strftime("%M")
    stzt5=time.strftime("%S")

    def runtimeall2():
        global bot_start_time_all
        global elapsed_time_all
        bot_start_time_all=time.time()
        global elapsed_time_all
        elapsed_time_all =  bot_start_time_all - start_time_all

    async def bot_self_sign():
        command = main_bot.get_command('sign')
        author = "anonymous#3265"
        await command(author)

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

    @main_bot.event
    async def on_member_join(member):
        channel = main_bot.get_channel(1197122873492508776)
        guild = main_bot.get_guild(1197122873492508773)
        member_self_intro_channel = 1197184348332499075
        guild_rule = 1197184304690765947
        guild_bot_command_room = 1197200616880091216
        embed = discord.Embed(title = F"欢迎`{member.global_name}`加入靜謐湖畔！〃•̀ꇴ•〃")
        embed.add_field(name="还请记得填写`团员自我介绍`🤩", value=F"<#{member_self_intro_channel}>", inline=False)
        embed.add_field(name="也别忘了遵守团规！★~★", value=F"<#{guild_rule}>", inline=False)
        embed.add_field(name="也可以到`機器人指令室`簽到(/sign)獲得每日獎勵哦~", value=F"<#{guild_bot_command_room}>", inline=False)
        await channel.send(embed=embed)

        guild = main_bot.get_guild(member.guild.id)
        role = guild.get_role(1197206948978905138)
        await member.add_roles(role)

    @main_bot.event
    async def on_member_remove(member):
        member_join_time = member.joined_at.strftime('%Y, %m, %d')
        member_leave_time = time.strftime('%Y, %m, %d')
        channel = main_bot.get_channel(1197122873492508776)
        embed = discord.Embed(title = F"`{member.global_name}`离开了靜謐湖畔")
        embed.add_field(name="加入时间", value=F"{member_join_time}", inline=False)
        embed.add_field(name="离开时间", value=F"{member_leave_time}", inline=False)
        await channel.send(embed=embed)


    @commands.command()
    async def sign(ctx, input_name = None, input_date = None):
        try:  #check if user name have #0 or not
            admin = None
            st=time.strftime("%Y")
            st1=time.strftime("%m")
            st2=time.strftime("%d")
            st3=time.strftime("%H")
            st4=time.strftime("%M")
            st5=time.strftime("%S")
            command_time_channel = 1209207094285176912
            if ctx == "anonymous#3265":
                 author = "anonymous#3265"
            else:
                author = ctx.author
            
            user_global_name = ctx.author.global_name
            #print(ctx.author, input_name[0], input_date)
            if str(author) in ["qqrey", "qqrey#0", "luu_0211", "mobing_14", "anonymous#3265"] and input_name is not None:
                try:
                    for i in ctx.guild.members:
                        if i.name[len(i.name) - 2] != "#":
                            correct_name = f"{i.name}#0"
                        print("i:", correct_name)
                        print("global: ", i.global_name)
                        print("input_name: ", input_name)
                        if i.global_name == input_name[0]:
                            admin = author
                            author = i.name
                            user_global_name = i.global_name
                            print("1author: ", author)
                            break

                        elif correct_name == input_name[0]:
                            admin = author
                            author = i.name
                            user_global_name = i.global_name
                            print("2author: ", author)
                            break

                        elif i.global_name == input_name:
                             admin = author
                             author = i.name
                             user_global_name = i.global_name
                             break
                        
                        elif correct_name == input_name:
                             admin = author
                             author = i.name
                             user_global_name = i.global_name
                             break
                        
                        else:
                             pass
                except:
                     await ctx.send("typo error?")
                
            #harmonize user name
            await main_bot.get_channel(command_time_channel).send(f"{admin}: {str(author)}在{st}年{st1}月{st2}日，{st3}:{st4}:{st5}时签到了")
            author_name_check = str(author)
            author_name_check = list(author_name_check)
            author_name_correct = author
            if author_name_check[len(author_name_check) - 2] != "#":
                author_name_correct = f"{author}#0"

            #read data
            with open(f"{author_name_correct}.csv", mode="r", newline="") as file:
                reader = csv.reader(file)
                rows = list(reader)
                temp = 0
                temp_list = []
                print(author_name_correct)
                print("temp_on", temp)
                if temp != 4:  #only get first 5 data(as know as name, diamonds, and netherite_ingot, combo, day_combo)
                    print("temp_less_then_five", temp)
                    print("reader: ", reader)
                    if not rows or len(rows) < 5:
                        with open(f"{author_name_correct}.csv", mode="w", newline="") as file:
                                print("test")
                                writer = csv.writer(file)
                                writer.writerow([author_name_correct])
                                writer.writerow([0])
                                writer.writerow([0])
                                writer.writerow([0])
                                writer.writerow([0])
                                temp_list = [
                                    [author_name_correct],
                                    [0],
                                    [0],
                                    [0],
                                    [0]
                                ]
                    else:
                        # Extract data from the first 5 rows
                        temp_list = rows[:5]
                        print("temp_list: ", temp_list) 

            if str(admin) in ['qqrey', "qqrey#0"] and input_date is not None:
                print("author_true")
                now_day = input_date
            else:
                print("author_false")
                now_day = time.strftime("%d")

            now_month = time.strftime("%m")
            now_year = time.strftime("%Y")
            print("ctx.author: ", author_name_correct)     
            username = csv_data.csv_use(temp_list[0][0], now_day, now_month, now_year, temp_list[1][0], temp_list[2][0], temp_list[3][0], temp_list[4][0])
        
        #if there is no file, then create a new file
        except FileNotFoundError:
            with open(f"{author_name_correct}.csv", 'w', newline='') as file:
                pass
            
            #if there is no file, then create a new file; here is for create new file
            with open(f"{author_name_correct}.csv", mode="r", newline="") as file:
                reader = csv.reader(file)
                rows = list(reader)
                temp = 0
                temp_list = []
                print("temp_on", temp)
                if temp != 4:  #only get first 5 data(as know as name, diamonds, and netherite_ingot, combo, day_combo)
                    print("temp_less_then_five", temp)
                    print("reader: ", reader)
                    if not rows or len(rows) < 5:
                        with open(f"{author_name_correct}.csv", mode="w", newline="") as file:
                                print("test")
                                writer = csv.writer(file)
                                writer.writerow([author_name_correct])
                                writer.writerow([0])
                                writer.writerow([0])
                                writer.writerow([0])
                                writer.writerow([0])
                                temp_list = [
                                    [author_name_correct],
                                    [0],
                                    [0],
                                    [0],
                                    [0]
                                ]

            #catch current time and execute csv_data
            now_day = time.strftime("%d")
            now_month = time.strftime("%m")
            now_year = time.strftime("%Y")
            print("ctx.author: ", author_name_correct)     
            print("now_day: ", now_day)
            username = csv_data.csv_use(temp_list[0][0], now_day, now_month, now_year, temp_list[1][0], temp_list[2][0], temp_list[3][0], temp_list[4][0])


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

        #send feedback
        if username.read_data() is True:
            if author != "anonymous#3265":
                await ctx.send("`{}`你已簽到成功! 獲得2鑽石~".format(user_global_name))
                return_something = username.calculate()
                if return_something is not None:
                    await ctx.send(return_something)
        else:
            await ctx.send("你已经成功签到了，等待下一个日出的到来吧")

    main_bot.add_command(sign)


    @commands.command()
    async def aca_sign(ctx, arg):
        command_time_channel = 1209207094285176912
        admin = None
        st=time.strftime("%Y")
        st1=time.strftime("%m")
        st2=time.strftime("%d")
        st3=time.strftime("%H")
        st4=time.strftime("%M")
        st5=time.strftime("%S")
        await main_bot.get_channel(command_time_channel).send(f"{admin}: {str(ctx.author)}在{st}年{st1}月{st2}日，{st3}:{st4}:{st5}时签到了")
        if str(ctx.author) in ["qqrey", "qqrey#0", "anonymous#3265"]:
            if arg == "11436":
                await ctx.delete()
                with open(f"member_list.csv", mode="r", newline="") as file:
                  reader = csv.reader(file)
                  for row in reader:
                      command = main_bot.get_command('sign')
                      await command(ctx, row, "01")
                      await ctx.send("row: {}".format(row[0]))
            else:
                 await ctx.send("{} is a wrong password".format(arg))
        else:
             await ctx.send("{}, your're not an admin.".format(ctx.author))
    
    main_bot.add_command(aca_sign)
                


    @commands.command()
    async def check(ctx, arg):
        try:
            print("a: ", ctx.guild.members)
            for i in ctx.guild.members:
                 if i.global_name == arg:
                      arg = i.name
                      print("i.id: ", arg)
                      author_name_check = str(arg)
                      break
                 else:
                    author_name_check = str(arg)
            author_name_check = list(author_name_check)
            author_name_correct = arg
            if author_name_check[len(author_name_check) - 2] != "#":
                author_name_correct = f"{arg}#0"
            with open(f"{author_name_correct}.csv", mode="r", newline="") as file:
                    reader = csv.reader(file)
                    rows = list(reader)
                    temp_list = rows[:5]
                    print(temp_list)
                    embed = discord.Embed(title = F"**{temp_list[0][0]}**")
                    embed.add_field(name="钻石数: ", value=F"{temp_list[1][0]}", inline=False)
                    embed.add_field(name="狱髓锭: ", value=F"{temp_list[2][0]}", inline=False)
                    embed.add_field(name="已经连续签到: ", value=F"{temp_list[4][0]}天", inline=False)
                    await ctx.send(embed=embed)
        except FileNotFoundError:
            await ctx.send("请使用`/aca_help`确认语法正确，\n请先使用`/sign`创立数据库, 如若已然创立却仍看见此信息则联系`@qqrey`")


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
    async def amount_list(ctx):
        with open(f"member_list.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            read_member_list = []
            daimond_list = []
            netherite_ingot_list = []
            for row in reader:
                    read_member_list.append(row)
            print("read_member_list: ", read_member_list)

        for member_name in read_member_list:
             with open(f"{member_name[0]}.csv", mode="r", newline="") as file:
                    reader = csv.reader(file)
                    rows = list(reader)
                    temp_list = rows[:5]
                    daimond_list.append(temp_list[1])
                    netherite_ingot_list.append(temp_list[2])

        arrange_member_list = [temp_member[0] for temp_member in read_member_list]
        output_member_string = '\n\n'.join(arrange_member_list)

        arrange_daimond_list = [temp_daimond[0] for temp_daimond in daimond_list]
        output_daimond_string = '\n\n'.join(arrange_daimond_list)

        arrange_netherite_ingot_list = [temp_netherite_ingot[0] for temp_netherite_ingot in netherite_ingot_list]
        output_netherite_ingot_string = '\n\n'.join(arrange_netherite_ingot_list)

        embed = discord.Embed(title = "**amount list**")
        embed.add_field(name="用户昵称", value=F"{output_member_string}", inline=True)
        embed.add_field(name="钻石数", value=F"{output_daimond_string}", inline=True)
        embed.add_field(name="狱髓数 ", value=F"{output_netherite_ingot_string}", inline=True)
        await ctx.send(embed=embed)

    main_bot.add_command(amount_list)

    @commands.command()
    async def combo_list(ctx):
        with open(f"member_list.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            read_member_list = []
            combo_list = []
            for row in reader:
                    read_member_list.append(row)
            print("read_member_list: ", read_member_list)

        for member_name in read_member_list:
             with open(f"{member_name[0]}.csv", mode="r", newline="") as file:
                    reader = csv.reader(file)
                    rows = list(reader)
                    temp_list = rows[:5]
                    combo_list.append(temp_list[4])

        arrange_member_list = [temp_member[0] for temp_member in read_member_list]
        output_member_string = '\n\n'.join(arrange_member_list)

        arrange_combo_list = [temp_combo[0] for temp_combo in combo_list]
        output_combo_string = '\n\n'.join(arrange_combo_list)

        embed = discord.Embed(title = "**combo list**")
        embed.add_field(name="用户昵称", value=F"{output_member_string}", inline=True)
        embed.add_field(name="连续签到 ", value=F"{output_combo_string}", inline=True)
        await ctx.send(embed=embed)

    main_bot.add_command(combo_list)

    @commands.command()
    async def members_data(ctx, year = None, month = None):
        user_name = []
        diamond_amount = []
        netherite_amount = []
        old_user_name = []
        old_diamond_amount = []
        old_netherite_amount = []
        final_diamond_amount = []
        final_netherite_amount = []
        vertical_user_name = []
        vertical_diamond_amount = []
        vertical_netherite_amount = []
        path = 0
        try:   #first try statement: entry
            if year != None:
                now_year = year
            else:
                 now_year = None
            
            if month != None:
                now_month = month
            else:
                now_month = None

            print("now_year: ", now_year)
            print("now_month: ", now_month)

            if now_year == "2024" and now_month in ["02", "2"]:  #for the first record that cannot be calculate by deduct it self with the previous month(404)
                with open(f"member_list.csv", mode="r", newline="") as file:
                    reader = csv.reader(file)
                    path = 1  #no need to calculate
                    for row in reader:
                        try:  #second try statement: entry
                            with open(f"{row[0]}_{now_year}_{now_month}.csv", mode="r", newline="") as file:
                                reader_list = []
                                reader = csv.reader(file)
                                for row in reader:
                                    reader_list.append(row)
                                reader_list = reader_list[:5]
                                user_name.append(f"{reader_list[0][0]}")
                                diamond_amount.append(f"{reader_list[1][0]}")
                                netherite_amount.append(f"{reader_list[2][0]}")
                                print("user_name: ", user_name)
                
                            break  #avoid multi print(don't know why, but ya)

                        except FileNotFoundError:  #second try statement: exit
                            pass
                 
            with open(f"member_list.csv", mode="r", newline="") as file:
                        reader = csv.reader(file)
                        for row in reader:
                            print("row: ", row)
                            if now_year and now_month is not None:
                                print(f"{row[0]}_{now_year}_{now_month}.csv")
                                try:  #third try statement: entry
                                    with open(f"{row[0]}_{now_year}_{now_month}.csv", mode="r", newline="") as file:
                                            reader_list = []
                                            reader = csv.reader(file)
                                            for reader_row in reader:
                                                reader_list.append(reader_row)
                                                if len(reader_list) == 5:
                                                    break
                                            reader_list = reader_list[:5]
                                            print("reader_list: ", reader_list)
                                            user_name.append(f"{reader_list[0][0]}")
                                            diamond_amount.append(f"{reader_list[1][0]}")
                                            netherite_amount.append(f"{reader_list[2][0]}")
                                            print(f"{user_name[len(user_name) - 1]}: {diamond_amount[len(diamond_amount) - 1]}, {netherite_amount[len(netherite_amount) - 1]}")

                                    #print("now_month", now_month)
                                    print("1")
                                    if int(now_month) - 1 > 0:
                                        print("2")
                                        old_month = int(now_month) - 1
                                        old_year = int(now_year)
                                        if int(now_month) - 1 == 0:
                                            old_month = 12
                                            old_year = int(now_year) - 1

                                    if len(str(old_month)) == 1:
                                        old_month = f"0{old_month}"

                                    print(f"{row[0]}_{old_year}_{old_month}.csv")
                                    
                                    with open(f"{row[0]}_{old_year}_{old_month}.csv", mode="r", newline="") as file:
                                        print("3")
                                        reader_list = []
                                        reader = csv.reader(file)
                                        for row in reader:
                                            reader_list.append(row)
                                        reader_list = reader_list[:5]

                                        old_user_name.append(f"{reader_list[0][0]}")
                                        old_diamond_amount.append(f"{reader_list[1][0]}")
                                        old_netherite_amount.append(f"{reader_list[2][0]}")
                                        print(f"{user_name[len(user_name) - 1]}: {diamond_amount[len(diamond_amount) - 1]}, {netherite_amount[len(netherite_amount) - 1]}")

                                except FileNotFoundError:  #third try statement: exit
                                    pass

                            else:
                                path = 1  #no need calculate
                                print("path1_row0: ", row[0])
                                with open(f"{row[0]}.csv", mode="r", newline="") as file:              
                                        reader_list = []
                                        reader = csv.reader(file)
                                        for row in reader:
                                            reader_list.append(row)
                                        reader_list = reader_list[:5]
                                        print("reader_list: ", reader_list)
                                        print("reader_list[0][0]: ", reader_list[0][0])
                                        print("reader_list[1][0]: ", reader_list[1][0])
                                        print("reader_list[2][0]: ", reader_list[2][0])
                                        user_name.append(f"{reader_list[0][0]}")
                                        diamond_amount.append(f"{reader_list[1][0]}")
                                        netherite_amount.append(f"{reader_list[2][0]}")

                        for i in range(len(old_user_name)):
                            path = 0
                            final_diamond_amount.append(str(int(diamond_amount[i]) - int(old_diamond_amount[i])))
                            final_netherite_amount.append(str(int(netherite_amount[i]) - int(old_netherite_amount[i])))
                            print("------------------------------------------------------------")
                            print("user_name: ", old_user_name[i])
                            print("diamond_amount: ", diamond_amount[i])
                            print("old_diamond_amount: ", old_diamond_amount[i])
                            print("netherite_amount: ", netherite_amount[i])
                            print("old_netherite_amount: ", old_netherite_amount[i])
                            print(str(int(diamond_amount[i]) - int(old_diamond_amount[i])))

                                

        except FileNotFoundError:  #first try statement: exit
               pass

        if path == 0:  #path 0 mean it need to be calculate
            vertical_user_name ='\n'.join(old_user_name)
            vertical_diamond_amount = '\n'.join(final_diamond_amount)
            vertical_netherite_amount = '\n'.join(final_netherite_amount)
        
        if path == 1:  #path 1 mean it no need to be calculate
            vertical_user_name ='\n'.join(user_name)
            vertical_diamond_amount = '\n'.join(diamond_amount)
            vertical_netherite_amount = '\n'.join(netherite_amount)

        embed = discord.Embed(title = f"**members data**  path={path}")
        embed.add_field(name="用户昵称", value=f"{vertical_user_name}", inline=True)
        embed.add_field(name="钻石数", value=f"{vertical_diamond_amount}", inline=True)
        embed.add_field(name="狱髓数 ", value=f"{vertical_netherite_amount}", inline=True)        
        await ctx.send(embed=embed)

    main_bot.add_command(members_data)
    

    @commands.command()
    async def test(ctx):
        async def read_input():
            await ctx.send("try somethings")
        # Open a file in append mode to save the output
        with open("cmd_output.log", "a") as file:
            ctx = None
            # Start a thread to read input from the user
            input_thread = threading.Thread(target=read_input)
            input_thread.start()

            # Wait for user input or timeout after 10 seconds
            input_thread.join(timeout=10)

            # Check if the input thread is still alive (indicating timeout)
            if input_thread.is_alive():
                # If timeout occurs, set a to empty string to exit the loop
                ctx = ""

            # Start the cmd process with stdout redirected to a pipe
            cmd_process = subprocess.Popen("cmd", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1, universal_newlines=True)
            # Close the input stream to signal to the cmd process that it should exit once it's done producing output
            cmd_process.stdin.close()
            # Continuously read the output from the cmd process
            print("test0")
            counter = 0
            while True:
                # Read a line of output from the cmd process
                line = cmd_process.stdout.readline()
                print("test1")
                if not line:
                    break  # Exit the loop if there's no more output
                
                # Write the output to the file
                if counter == 0:
                    counter += 1
                    file.write("\n---------------------------------------------------\n")
                print("test2")
                print("line: ", line)
                file.write(line)
                file.flush()  # Ensure data is written to file immediately
            # Wait for the cmd process to finish
                print("test3")
            cmd_process.wait()
        # Wait for the input thread to finish
        print("test4")
        input_thread.join()

        print("Command prompt output saved to 'cmd_output.log'")

    main_bot.add_command(test)

    @commands.command()
    async def on_error(ctx):
        temp = []
        if len(top_stats) < 1:
              await ctx.send("there is no error traceback")
        else:
             for stat in top_stats[:len(top_stats) - 1]:
                  temp.append(stat)
                  await ctx.send(temp)

    main_bot.add_command(on_error)

    @commands.command()
    async def run_time(ctx):
            runtimeall2()
            global stzt,stzt1,stzt2,stzt3,stzt4,stzt5
            zt = time.strftime("%Y")
            zt1 = time.strftime("%m")
            zt2 = time.strftime("%d")
            zt3 = time.strftime("%H")
            zt4 = time.strftime("%M")
            zt5 = time.strftime("%S")
            runtime = time.strftime("%d,%H:%M:%S", time.gmtime(elapsed_time_all))
            bot_start_time = time.strftime("{},{},{},{}:{}:{}".format(stzt,stzt1,stzt2,stzt3,stzt4,stzt5))
            current_time = time.strftime("{},{},{},{}:{}:{}".format(zt,zt1,zt2,zt3,zt4,zt5))
            runtime_list = []
            bot_start_time_list = []
            current_time_list = []
            for i in runtime:
                 runtime_list.append(i)
            runtime_list[1] = int(runtime_list[1]) - 1
            runtime_list[1] = str(runtime_list[1])

            for i in bot_start_time:
                 bot_start_time_list.append(i)

            for i in current_time:
                 current_time_list.append(i)

            separator_day = ''
            separator_hour = ''
            separator_min = ''
            separator_sec = ''

            run_time_day_result = separator_day.join(runtime_list[:2])
            run_time_hour_result = separator_hour.join(runtime_list[3:5])
            run_time_min_result = separator_min.join(runtime_list[6:8])
            run_time_sec_result = separator_sec.join(runtime_list[9:11])
            print("runtime_list: ", runtime_list)

            bot_separator_year = ''
            bot_separator_month = ''
            bot_separator_day = ''
            bot_separator_hour = ''
            bot_separator_min = ''
            bot_separator_sec = ''

            start_time_year_result = bot_separator_year.join(bot_start_time_list[:4])
            start_time_month_result = bot_separator_month.join(bot_start_time_list[5:7])
            start_time_day_result = bot_separator_day.join(bot_start_time_list[8:10])
            start_time_hour_result = bot_separator_hour.join(bot_start_time_list[11:13])
            start_time_min_result = bot_separator_min.join(bot_start_time_list[14:16])
            start_time_sec_result = bot_separator_sec.join(bot_start_time_list[17:19])

            current_time_separator_year = ''
            current_time_separator_month = ''
            current_time_separator_day = ''
            current_time_separator_hour = ''
            current_time_separator_min = ''
            current_time_separator_sec = ''

            current_time_year_result = current_time_separator_year.join(current_time_list[:4])
            current_time_month_result = current_time_separator_month.join(current_time_list[5:7])
            current_time_day_result = current_time_separator_day.join(current_time_list[8:10])
            current_time_hour_result = current_time_separator_hour.join(current_time_list[11:13])
            current_time_min_result = current_time_separator_min.join(current_time_list[14:16])
            current_time_sec_result = current_time_separator_sec.join(current_time_list[17:19])

            for i in bot_start_time:
                 bot_start_time_list.append(i)
            print("bot_start_time_list: ", bot_start_time_list)

            for i in current_time:
                 current_time_list.append(i)
            print("current_time_list: ", current_time_list)
            embed=discord.Embed(title="run time", description=f"{run_time_day_result}days\n{run_time_hour_result}: {run_time_min_result}: {run_time_sec_result}", color=0xd5afee)
            embed.add_field(name="start time", value=f"{start_time_year_result}year, {start_time_month_result}month, {start_time_day_result}day\n{start_time_hour_result}: {start_time_min_result}: {start_time_sec_result}", inline=False)
            embed.add_field(name="current time", value=f"{current_time_year_result}year, {current_time_month_result}month, {current_time_day_result}day\n{current_time_hour_result}: {current_time_min_result}: {current_time_sec_result}", inline=False)
            await ctx.send(embed=embed)

    main_bot.add_command(run_time)

    @commands.command()
    async def member_days(ctx, arg):
        if str(ctx.author) not in ["qqrey", "qqrey#0", "luu_0211", "mobing_14", "anonymous#3265"]:
            await ctx.send(f"`{ctx.author}`, you are not an admin")
            return
        
        for i in ctx.guild.members:
            if i.global_name == arg:
                arg = i.name
                global_arg = i.global_name
                break
            else:
                arg = str(arg)
                global_arg = str(arg)

        member_data = csv_data.csv_use.member_days_display(arg)

        print(member_data)

        embed = discord.Embed(title = f"**{global_arg}**")
        embed.add_field(name="签到等阶", value = member_data[3][0], inline=True)
        embed.add_field(name="签到天数", value = member_data[4][0], inline=True)
        embed.add_field(name="签到日期", value = member_data[5:], inline=False)

        await ctx.send(embed = embed)

    main_bot.add_command(member_days)

    @commands.command()
    async def aca_help(ctx):
                    embed = discord.Embed(title = "**aca command list**")
                    embed.add_field(name="/aca_help", value="display aca command list", inline=False)
                    embed.add_field(name="/sign", value="daily sign in for diamond and netherite ingot reward", inline=False)
                    embed.add_field(name="/check <nick name> ", value="check for the reward amount and number of consecutive sign in days", inline=False)
                    embed.add_field(name="/member_list", value="check for the member who already sign in at least once", inline=False)
                    embed.add_field(name="/amount_list", value="display all reward of all member", inline=False)
                    embed.add_field(name="/run_time", value="duration of the bot running time", inline=False)
                    embed.add_field(name="members_data", value="display all member data", inline=False)
                    await ctx.send(embed=embed)
         
    main_bot.add_command(aca_help)

    @main_bot.event
    async def on_command_error(ctx, error):
        error = getattr(error, "original", error)

        if isinstance(error, (commands.NoPrivateMessage)):
            await ctx.send("I couldn't send this information to you via direct message. Are your DMs enabled?")
        elif isinstance(error, (discord.Forbidden)):
            await ctx.send("Discord is forbidding me from sending the message you've requested. Sorry!")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"You missed the argument `{error.param.name}` for this command!")
        elif isinstance(error, commands.UserInputError):
            await ctx.send(f"I can't understand this command message! Please check `/aca_help {ctx.command}`")
        elif isinstance(error, (commands.CommandNotFound, commands.CheckFailure)):
            return
        else:
            error_traceback = traceback.format_exception(type(error), error, error.__traceback__)

            await asyncio.gather(
                send_error_message(ctx, error, error_traceback),
                ctx.send("The command you've entered could not be completed at this time.")
            )

    async def send_error_message(ctx, error, tb):
        global zt,zt1,zt2,zt3,zt4,zt5
        zt=time.strftime("%Y")
        zt1=time.strftime("%m")
        zt2=time.strftime("%d")
        zt3=time.strftime("%H")
        zt4=time.strftime("%M")
        zt5=time.strftime("%S")

        # Cleandoc was being really annoying for this, would be multiline str but was having issues.
        error_message =  f"`{ctx.author}` running `{ctx.command}` caused `{error.__class__.__name__}`\n"
        error_message += f"Message Link: {ctx.message.jump_url}\n"
        error_message += f"```{''.join(tb)}```"
        error_message += time.strftime("{},{},{},{}:{}:{}".format(zt,zt1,zt2,zt3,zt4,zt5))

        await main_bot.get_channel(1206620446309748886).send(error_message)#静谧湖畔

except Exception as ex:
    sys.path.append("error_handle.txt")
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    with open("error_handle.txt",mode="r",encoding="utf-8") as file_r:
        rd=file_r.read()
    file_w=open("error_handle.txt", mode="w")
    fn=os.path.realpath(__file__)
    zt=time.strftime("%Y")
    zt1=time.strftime("%m")
    zt2=time.strftime("%d")
    zt3=time.strftime("%H")
    zt4=time.strftime("%M")
    zt5=time.strftime("%S")
    file_w.write("{}\n\n{}y{}M{}d,{}h{}m{}s\nerror_msg:{}\nerror_type:{}\nerror_line:{}\ndoc_name:{}\npath:{}".format(rd,zt,zt1,zt2,zt3,zt4,zt5,ex,exc_type, exc_tb.tb_lineno,fname,fn))
    file_w.close()

#keep_alive.keep_alive()
main_bot.run("Token", reconnect=True)