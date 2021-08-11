import win32com.client as win32
import win32com
import os
import sys

outlook = win32.Dispatch('Outlook.Application')
mail = outlook.CreateItem(0)
mail.To = 'charlesfrancois.ghanime@se.com'
mail.Subject = 'Testing automated email sending'
mail.Body = 'Dear Myself'
mail.send()