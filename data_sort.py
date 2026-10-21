import csv
import tkinter as tk
from tkinter import filedialog
import sys

#Retrieves the first list from the rows library and returns teh first index as int
def point_number(rows):
    return int(rows[0])

def feature_code(rows):
    return (rows[4])

def feature_code_and_point_num(rows):
    return (rows[4], int(rows[0]))

#Establishes var to set pathfiles for retrieving and saving CSV data
root = tk.Tk()
root.withdraw()

origin_filepath = filedialog.askopenfilename(title="Select your survey CSV", filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
if not origin_filepath:
    root.destroy()
    sys.exit()

dst_filepath = filedialog.asksaveasfilename(title="Save sorted survey CSV", defaultextension=".csv", filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
if not dst_filepath:
    root.destroy()
    sys.exit()

root.destroy()
sort_by : str | None = None

#Defines used var in code and expected types
point_num : int | None = None
northing : float | None = None
easting : float | None = None
elev : float | None = None

while sort_by not in("1", "2", "3"):
    sort_by : str = input("Enter 1 to sort by point number, enter 2 to sort by feature code, or enter 3 to sort by feature code and point number order: ")
    if sort_by not in("1", "2", "3"):
        print("Not a valid entry...")


if sort_by == "1":
    with open(origin_filepath, "r", newline="") as file:
        reader = csv.reader(file)
        rows = []
        for data in reader:
            rows.append(data)
    
        rows.sort(key=point_number)


    with open(dst_filepath, "w", newline="") as output_file:
        writer = csv.writer(output_file)
        
        for row in rows:
            writer.writerow(row)
            writer.writerow([])


if sort_by == "2":
    with open(origin_filepath, "r", newline="") as file:
        reader = csv.reader(file)
        rows = []
        for data in reader:
            rows.append(data)
    
        rows.sort(key=feature_code)


    with open(dst_filepath, "w", newline="") as output_file:
        writer = csv.writer(output_file)
        current_feature_code = rows[0][4]
        
        for row in rows:
            if row[4] != current_feature_code:
                writer.writerow([])
                writer.writerow(row)
                writer.writerow([])
                
            else:
                writer.writerow(row)
                writer.writerow([])
        
            current_feature_code = row[4]


if sort_by == "3":
    with open(origin_filepath, "r", newline="") as file:
        reader = csv.reader(file)
        rows = []
        for data in reader:
            rows.append(data)
    
        rows.sort(key=feature_code_and_point_num)


    with open(dst_filepath, "w", newline="") as output_file:
        writer = csv.writer(output_file)
        current_feature_code = rows[0][4]
        
        for row in rows:
            if row[4] != current_feature_code:
                writer.writerow([])
                writer.writerow(row)
                writer.writerow([])
                
            else:
                writer.writerow(row)
                writer.writerow([])
        
            current_feature_code = row[4]