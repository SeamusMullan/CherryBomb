from typing import final
import instaloader as il
import twint
import os
import time
import random

import CB_Functions as cbf





# Instaloader #######################################################################################################

def IL_Login(username, password):
    IL = il.Instaloader()
    try:
        IL.login(username, password)
        return IL
    except Exception as e:
        cbf.returnError(e)
        cbf.saveErrorLog(e)
        return False


def IL_FromFile(username):
    IL = il.Instaloader()
    IL.load_session_from_file(username)
    return IL


def IL_GetProfile(IL, profile):
    try:
        profile = il.Profile.from_username(IL.context, profile)
        return profile
    except Exception as e:
        cbf.returnError(e)
        cbf.saveErrorLog(e)
        return False


def IL_GetProfileFollowers(profile):
    try:
        followers = profile.get_followers()
        return followers
    except Exception as e:
        cbf.returnError(e)
        cbf.saveErrorLog(e)
        return False


def IL_GetProfileFollowing(profile):
    try:
        following = profile.get_followees()
        return following
    except Exception as e:
        cbf.returnError(e)
        cbf.saveErrorLog(e)
        return False


def IL_GetProfilePosts(profile):
    try:
        posts = profile.get_posts()
        return posts
    except Exception as e:
        cbf.returnError(e)
        cbf.saveErrorLog(e)
        return False


def IL_DownloadProfilePosts(profile, posts, path):
    if not path:
        path = f"Downloaded Posts\\{profile}\\"

    if not os.path.exists(path):
        os.makedirs(path)

    for post in posts:
        try:
            post.download_post(path)
        except Exception as e:
            cbf.returnError(e)
            cbf.saveErrorLog(e)
        finally:
            time.sleep(random.randint(1, 3))

    
#####################################################################################################################



# Twint #############################################################################################################


#####################################################################################################################



