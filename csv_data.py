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
            if number == 0:
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
            else:
                with open(f"{self.name}_{self.year}_{self.month}.csv", 'w', newline='', encoding="utf-8") as file:
                    writer = csv.writer(file)
                    print("old_data1", old_data)
                    for i in old_data:
                        print("i: ", i)
                        writer.writerow(i)
                with open(f"{self.name}_{self.year}_{self.month}.csv", 'r', newline='', encoding="utf-8") as file:
                    reader = csv.reader(file)
                    back_data = list(reader)
                    with open(f"{self.name}.csv", 'w', newline='', encoding="utf-8") as file:
                        print("back_data: ", back_data)
                        writer = csv.writer(file)

                        #print(new_data)
                        count = 0
                        for i in back_data:   
                            if count < 4:
                                if count != 3:
                                    print("new_i: ", i)
                                    writer.writerow(i)
                                    count += 1
                                else:
                                    print("new_i: ", i)
                                    print("change_i: ", 0)
                                    writer.writerow("0")
                                    count += 1

                        #writer.writerow(f'{self.date}')
                                    


    def read_data(self):
        # Read data from the CSV file
        with open(f"{self.name}.csv", mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            all_data = list(reader)  # Store all data read from the CSV file

        print("list: ", all_data)
        cover_data = [self.name,
                      self.diamond,
                      self.netherite_ingot,
                      self.combo,
                      self.daily_combo,
                      self.date]
        print("cover_data", cover_data)

        # Check if it's the first day of the month
        if self.date == 1:
            self.combo = 0
            self.daily_combo = 0
            print("last_all_data: ", all_data)
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
                if row == []:
                    break
                else:
                    old_data.append(row)

        if old_data:
            print("row: ", row[0])
            print("old_data: ", old_data)
            print("old_data: ", old_data[len(old_data) - 1][0])
            print("self_date: ", self.date)
            if str(row[0]) == str(self.date):
                print("false")
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
            old_data = []
            for row in reader:
                if row == []:
                    return "you have not sign in before"
                else:
                    old_data.append(row)
            
            temp = 0
            temp_list = []
            if temp != 5:  #only get first 5 data(as know as name, diamonds, and netherite_ingot, combo, daily_combo)
                for row in old_data:
                    if row == []:
                        return
                    else:
                        temp_list.append(row)
                        temp+=1
            
            
            player_name = temp_list[0][0]
            diamond_amount = int(temp_list[1][0])
            netherite_ingot_amount = int(temp_list[2][0])
            combo = int(temp_list[3][0])
            daily_combo = int(temp_list[4][0])
            diamond_amount_count = 0
            netherite_ingot_count = 0
            combo_count = 0
            path_check = 0
            print("cal_temp_list: ", temp_list)

            if self.date == 1:    #if there is first day of the month
                with open(f"{self.name}.csv", 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([player_name])
                    writer.writerow([diamond_amount])
                    writer.writerow([netherite_ingot_amount])
                    writer.writerow(0)      #reset combo when the first day in a month
                    writer.writerow(0)      #also daily combo
                    writer.writerow([self.date])

            print("old_data: ", old_data)
            print("len_old_data: ", len(old_data))
            if int(len(old_data)) > 11:  #exclude first five data
                #calculate if the is at least 7 data in a row
                if int(old_data[len(old_data) - 1][0]) - int(old_data[len(old_data) - 7][0]) == 6 and combo == 0:
                    diamond_amount_count = diamond_amount + 2
                    netherite_ingot_count = netherite_ingot_amount + 3
                    combo_count = combo + 1
                    daily_combo += 1
                    path_check = 1
                    print("7 days in a row")

                if len(old_data) > 18:
                    if int(old_data[len(old_data) - 1][0]) - int(old_data[len(old_data) - 14][0]) == 13 and combo == 1:
                        diamond_amount_count = diamond_amount + 2
                        netherite_ingot_count = netherite_ingot_amount + 5
                        combo_count = combo + 1
                        daily_combo += 1
                        path_check = 2
                        print("14 days in a row")
                if len(old_data) < 25:
                    if int(old_data[len(old_data) - 1][0]) - int(old_data[len(old_data) - 21][0]) == 20 and combo == 2:
                        diamond_amount_count = diamond_amount + 2
                        netherite_ingot_count = netherite_ingot_amount + 8
                        combo_count = combo + 1
                        daily_combo += 1
                        path_check = 3
                        print("21 days in a row")
                if len(old_data) > 32:
                    if int(old_data[len(old_data) - 1][0]) - int(old_data[len(old_data) - 28][0]) == 27 and combo == 3:
                        diamond_amount_count = diamond_amount + 2
                        netherite_ingot_count = netherite_ingot_amount + 10
                        combo_count = combo + 1
                        daily_combo += 1
                        path_check = 4
                        print("28 days in a row")
                else:
                    diamond_amount_count = diamond_amount + 2
                    daily_combo += 1
                    combo = 0
                    print("less then 7 day in a row")
            else:
                diamond_amount_count = diamond_amount + 2
                daily_combo += 1
                combo = 0
                print("less then 7 day in a row")

            print("calculate_old_data_1: ", old_data)
            print("calc_netherite: ", netherite_ingot_count)
            if netherite_ingot_count > 2 and combo_count > 0:
                old_data[0][0] = player_name
                old_data[1][0] = diamond_amount_count
                old_data[2][0] = netherite_ingot_count
                old_data[3][0] = combo_count
                old_data[4][0] = daily_combo
            else:
                old_data[0][0] = player_name
                old_data[1][0] = diamond_amount_count
                old_data[2][0] = netherite_ingot_amount
                old_data[3][0] = combo
                old_data[4][0] = daily_combo
            print("diamond_count: ", diamond_amount_count)
            print("calculate_old_data_2: ", old_data)
            with open(f"{self.name}.csv", 'w', newline='') as file:
                writer = csv.writer(file)
                temp_list_old_data = []
                for i in old_data:
                    temp_list_old_data.append(i)
                print("temp_list: ", temp_list_old_data)
                writer.writerows(temp_list_old_data)
        if path_check == 1:
            return "你已連續簽到7天!而外獲得3玉髓錠+2鑽石~"
        elif path_check == 2:
            return "你已連續簽到14天!而外獲得5玉髓錠+2鑽石~"
        elif path_check == 3:
            return "你已連續簽到21天!而外獲得8玉髓錠+2鑽石~"
        elif path_check == 4:
            return "你已連續簽到28天!而外獲得10玉髓錠+2鑽石~"