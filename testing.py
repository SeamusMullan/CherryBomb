import CherryFacade as cfac
import CB_Formatting as cbform
import threading as th
import instaloader as il
import instabot as ibot

username = str(input("Username: "))
password = str(input("Password: "))

# L = il.Instaloader()
# L.login(username, password)

ibot = ibot.Bot()
ibot.login(username, password)



