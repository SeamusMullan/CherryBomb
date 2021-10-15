from typing import final
import instaloader as il
import twint
import os
import time
import random

import CB_Formatting as cbf
import importFirefoxInstagramCookies as ific




# Instaloader #######################################################################################################

def IL_Login(username, password):
    tries = 0
    errors = ""

    try:
        IL = il.Instaloader()
        IL.load_session_from_file(username)
        return IL
    except Exception as e:
        while tries < 3:
            try:
                if tries > 0:
                    ific.main()
                IL = il.Instaloader()
                IL.login(username, password)
                IL.save_session_to_file(username)
                return IL
            except Exception as e:
                errors += f"{e}\n"
                tries += 1
                time.sleep(random.randint(1, 3))
        cbf.returnError(errors)
        cbf.saveErrorLog(errors)
        return False


def IL_GetProfile(IL, profile):
    try:
        profile = il.Profile.from_username(IL.context, profile)
        return profile
    except Exception as e:
        cbf.returnError(e)
        cbf.saveErrorLog(e)
        return False


def IL_GetProfileFollowers(IL, profile):
    try:
        target = IL_GetProfile(IL, profile)
        followers = target.get_followers()
        return followers
    except Exception as e:
        cbf.returnError(e)
        cbf.saveErrorLog(e)
        return False


def IL_GetProfileFollowing(IL, profile):
    try:
        following = profile.get_followees()
        return following
    except Exception as e:
        cbf.returnError(e)
        cbf.saveErrorLog(e)
        return False


def IL_GetProfilePosts(IL, profile, output=False):
    posts = []
    images = []
    videos = []
    try:
        target = IL_GetProfile(IL, profile)
        for post in target.get_posts():
            posts.append(post)
            if post.is_video:
                videos.append(post)
            else:
                images.append(post)

        print("\n")
        print(f"{cbf.C.OKGREEN}{len(posts)} posts found.{cbf.C.ENDC}")
        print(f"{cbf.C.OKGREEN}{len(posts) - len(videos)} are images.{cbf.C.ENDC}")
        print(f"{cbf.C.OKGREEN}{len(posts) - len(images)} are videos.{cbf.C.ENDC}")
        print("\n")

        if output:            
            for post in posts:
                if post.is_video:
                    print(f"{cbf.C.CVIOLET}{post.caption}{cbf.C.ENDC}\n")
                else:
                    print(f"{cbf.C.OKCYAN}{post.caption}{cbf.C.ENDC}\n")

        return posts

    except Exception as e:
        cbf.returnError(e)
        cbf.saveErrorLog(e)
        return False


def IL_DownloadProfilePosts(IL, profileUsername, path="Downloaded Posts\\"):

    path = path + profileUsername + "\\"

    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

    posts = IL_GetProfilePosts(IL, profileUsername)

    for post in posts:
        try:
            IL.download_post(post, target=profileUsername)
            print(f"Downloaded post: {post.shortcode}")
        except Exception as e:
            cbf.returnError(e)
            cbf.saveErrorLog(e)
        finally:
            time.sleep(random.randint(1, 3))


def IL_GetFollowees(IL, username):
    count = 0
    theprofile = IL_GetProfile(IL, username)
    flist = []
    try:
        followees = theprofile.get_followees()
        for uname in followees:
            count += 1
            flist.append(uname)
        print(f"{cbf.C.OKGREEN}{count} followees found.{cbf.C.ENDC}")
        return flist

    except Exception as e:
        cbf.returnError(e)
        cbf.saveErrorLog(e)
        return False

def IL_GetFollowers(IL, username):
    count = 0
    theprofile = IL_GetProfile(IL, username)
    flist = []
    try:
        followees = theprofile.get_followers()
        for uname in followees:
            count += 1
            flist.append(uname)
        print(f"{cbf.C.OKGREEN}{count} followers found.{cbf.C.ENDC}")
        return flist

    except Exception as e:
        cbf.returnError(e)
        cbf.saveErrorLog(e)
        return False



#####################################################################################################################



# Twint #############################################################################################################




#####################################################################################################################



