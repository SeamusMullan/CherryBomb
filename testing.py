from pyvis.network import Network
import networkx as nx
import instaloader as il
import CB_Functions as cbfunc
import CB_Formatting as cbform


L = il.Instaloader()
L.load_session_from_file("notasnakepython")


# for i in cbfunc.IL_GetFollowees(L, "rohho_music"):
#     print(f"{cbform.C.OKBLUE}{i.username}{cbform.C.ENDC}")


# motivational.lizard.daily

# for every post, check if "rohho_music" commented on it


for post in cbfunc.IL_GetProfile(L, "motivational.lizard.daily").get_posts():
    for comment in post.get_comments():
        if comment.owner.username == "rohho_music":
            print(f"{cbform.C.OKGREEN}{comment.owner.username} commented on {post.owner.username}'s post: {cbform.C.ENDC}")
            print(f"{cbform.C.OKBLUE}{comment.text}{cbform.C.ENDC}")
            print("\n")