#Task 1: Sales Data Cloning and Modification
#Gain practical experience in copying dictionaries and modifying data, crucial skills in data analysis.
#Problem Statement:
#You have a dictionary representing weekly sales data for a store. Your task is to create a deep copy of this data and update the sales 
#figures for a specific week.
#Given Sales Data:
#weekly_sales = {
#    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
#    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
#}
#Create a deep copy of weekly_sales.
#Update the sales figure for "Electronics" in "Week 2" to 18000 in the copied data.
import copy

weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

sales_copy = copy.deepcopy(weekly_sales)
sales_copy["Week 2"]["Electronics"] = 18000
print(f"Original: {weekly_sales}")
print(f"Deep Copy Updated: {sales_copy}")