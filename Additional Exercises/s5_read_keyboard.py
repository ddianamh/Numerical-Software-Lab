#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 10:02:48 2023

@author: dianah
"""
#Write a Python program that calculates how much money you can spend each 
#day for lunch for the rest of the month based on today’s date and how much 
#money you currently have in your lunch account. The program should ask you: 
#(1) how much money you have in your account, (2) what today’s date is, and
#(3) how many days there are in the month. The program should return your 
#daily allowance. The results of running your program should look like this:
#How much money (in Euro) in your lunch account?  319
#What day of the month is today?  21
#How many days in this month?  30
#You can spend 31.90 Euro each day for the rest of the month.

import numpy as np

current_money = float( input("How much money (in Euro) in your lunch account? ") )
day = int( input("What day of the month is today? ") )
total_days = int( input("How many days in this month? " ) )

days_left = total_days - day + 1

money = current_money / days_left

print("You can spend ", money, "Euro each day for the rest of the month")
