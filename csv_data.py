import csv
import datetime

class csv_use:

    def __init__(self, pname, pdate, pmonth, pyear, pdiamond, pnetherite_ingot, pcombo, dcombo) -> None:
        self.name = pname
        self.date = pdate
        self.month = pmonth
        self.year = pyear
        self.diamond = pdiamond
        self.netherite_ingot = pnetherite_ingot
        self.combo = pcombo
        self.daily_combo = dcombo


    def write_data(self, old_data, number):
        # Write data to the CSV file
        with open(f"{self.name}.csv", 'w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            if number == 0:   #ordinary day
                #print("self.date_2: " ,self.date)
                if old_data == []:
                    # Write a new row if old_data is empty
                    #print("new_loop")
                    writer.writerow([self.name])
                    writer.writerow([self.diamond])
                    writer.writerow([self.netherite_ingot])
                    writer.writerow([self.combo])
                    writer.writerow([self.daily_combo])
                    writer.writerow([self.date])
                else:
                    #print("old_loop")
                    # Append the new data to the old_data list
                    old_data.append([self.date])
                    # Write all data to the CSV file
                    writer.writerows(old_data)   
            #print("here is true")
            else:    #first day in a month
                with open(f"{self.name}_{self.year}_{self.month}.csv", 'w', newline='', encoding="utf-8") as file:
                    writer = csv.writer(file)
                    #print("old_data1", old_data)
                    for i in old_data:
                        #print("i: ", i)
                        writer.writerow(i)
                with open(f"{self.name}_{self.year}_{self.month}.csv", 'r', newline='', encoding="utf-8") as file:
                    reader = csv.reader(file)
                    back_data = list(reader)
                    with open(f"{self.name}.csv", 'w', newline='', encoding="utf-8") as file:
                        #print("back_data: ", back_data)
                        writer = csv.writer(file)

                        #print(new_data)
                        count = 0
                        for i in back_data:   
                            if count < 4:
                                if count != 3:
                                    #print("new_i: ", i)
                                    writer.writerow(i)
                                    count += 1
                                else:
                                    #print("new_i: ", i)
                                    #print("change_i: ", 0)
                                    writer.writerow("0")
                                    count += 1

                        #writer.writerow(f'{self.date}')
                                    


    def read_data(self):
        # Read data from the CSV file
        with open(f"{self.name}.csv", mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            all_data = list(reader)  # Store all data read from the CSV file

        #print("list: ", all_data)

        # Check if it's the first day of the month
        if self.date == 1:
            self.combo = 0
            self.daily_combo = 0
            #print("last_all_data: ", all_data)
            self.write_data(all_data, 1)  # Pass all data to write_data
            #all_data.clear()  # Clear the list
            #all_data.append(cover_data)  # Append cover_data
            #print("all_data_after_append: ", all_data)
            #self.write_data(all_data, 0)

        
        old_data = []
        # Read data from the CSV file again for further processing
        with open(f"{self.name}.csv", mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                    old_data.append(row)

        if old_data:
            #print("full_row:" ,row)
            #print("row: ", row[0])
            #print("old_data: ", old_data)
            #print("old_data: ", old_data[len(old_data) - 1][0])
            #print("self_date: ", self.date)
            if str(row[0]) == str(self.date):
                #print("false")
                return False
            else:
                self.write_data(old_data, 0)
                return True
        else:
            self.write_data(old_data, 0)
            return True
        
            
    def calculate(self):
        with open(f"{self.name}.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            read_data = []
            for row in reader:
                if row == []:
                    return "you have not sign in before"
                else:
                    read_data.append(row)
            
            temp_list = read_data[:5]   #only store the first five element(as know as name, diamonds, and netherite_ingot, combo, daily_combo)
            print(temp_list)

            player_name = temp_list[0][0]
            diamond_amount = temp_list[1][0]
            netherite_ingot_amount = temp_list[2][0]
            combo_tier = temp_list[3][0]
            daily_combo = temp_list[4][0]
            print(player_name)
            print(diamond_amount)
            print(netherite_ingot_amount)
            print("read_data", read_data)

            if self.date == 1:    #if there is first day of the month
                with open(f"{self.name}.csv", 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([player_name])
                    writer.writerow([diamond_amount])
                    writer.writerow([netherite_ingot_amount])
                    writer.writerow(0)      #reset combo when the first day in a month
                    writer.writerow(0)      #also daily combo
                    writer.writerow([self.date])
            else:  #if there is an ordinary day
                if int(len(read_data)) > 11 and int(read_data[len(read_data) - 2][0]) == int(self.date) - 1:  #make sure that data len is enough long or it will be an error for the specific number of days in a row   #7day+5data=12len   #second last will be now day - 1 to make sure there is in a row 
                    #if there is specific number of the days in a row(7,14,21,28)
                    if int(read_data[len(read_data) - 1][0]) - int(read_data[5][0]) == 6 and int(combo_tier) == 0:#7day
                        with open(f"{self.name}.csv", 'w', newline='') as file:
                            writer = csv.writer(file)
                            read_data[1][0] = int(diamond_amount) + 4
                            read_data[2][0] = int(netherite_ingot_amount) + 3
                            read_data[3][0] = 1
                            read_data[4][0] = int(daily_combo) + 1
                            writer.writerows(read_data)
                            return "你已連續簽到7天!而外獲得3玉髓錠+2鑽石~"

                    elif int(read_data[len(read_data) - 1][0]) - int(read_data[5][0]) == 13 and int(combo_tier) == 1:#14day
                        with open(f"{self.name}.csv", 'w', newline='') as file:
                            writer = csv.writer(file)
                            read_data[1][0] = diamond_amount + 4
                            read_data[2][0] = netherite_ingot_amount + 3
                            read_data[3][0] = 2
                            read_data[4][0] = daily_combo + 1
                            writer.writerows(read_data)
                            return "你已連續簽到14天!而外獲得5玉髓錠+2鑽石~"

                    elif int(read_data[len(read_data) - 1][0]) - int(read_data[5][0]) == 20 and int(combo_tier) == 2:#7day
                        with open(f"{self.name}.csv", 'w', newline='') as file:
                            writer = csv.writer(file)
                            read_data[1][0] = diamond_amount + 4
                            read_data[2][0] = netherite_ingot_amount + 3
                            read_data[3][0] = 3
                            read_data[4][0] = daily_combo + 1
                            writer.writerows(read_data)
                            return "你已連續簽到21天!而外獲得8玉髓錠+2鑽石~"

                    elif int(read_data[len(read_data) - 1][0]) - int(read_data[5][0]) == 27 and int(combo_tier) == 3:#7day
                        with open(f"{self.name}.csv", 'w', newline='') as file:
                            writer = csv.writer(file)
                            read_data[1][0] = diamond_amount + 4
                            read_data[2][0] = netherite_ingot_amount + 3
                            read_data[3][0] = 4
                            read_data[4][0] = daily_combo + 1
                            writer.writerows(read_data)
                            return "你已連續簽到28天!而外獲得10玉髓錠+2鑽石~"
                    
                    elif int(read_data[len(read_data) - 2][0]) == int(self.date) - 1:
                        with open(f"{self.name}.csv", 'w', newline='') as file:
                            writer = csv.writer(file)
                            read_data[1][0] = int(diamond_amount) + 2
                            read_data[4][0] = int(daily_combo) + 1
                            writer.writerows(read_data)

                    else: #if combo is break
                        with open(f"{self.name}.csv", 'w', newline='') as file:
                            writer = csv.writer(file)
                            read_data[1][0] = int(diamond_amount) + 2
                            read_data[4][0] = 1
                            writer.writerows(read_data)
                else:#if the data len is not enough 7days in a row
                    if int(read_data[len(read_data) - 2][0]) == int(self.date) - 1:
                        with open(f"{self.name}.csv", 'w', newline='') as file:
                            writer = csv.writer(file)
                            read_data[1][0] = int(diamond_amount) + 2
                            read_data[4][0] = int(daily_combo) + 1
                            writer.writerows(read_data)

                    else: #if combo is break
                        with open(f"{self.name}.csv", 'w', newline='') as file:
                            writer = csv.writer(file)
                            read_data[1][0] = int(diamond_amount) + 2
                            read_data[4][0] = 1
                            writer.writerows(read_data)
