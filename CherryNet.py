from pyvis.network import Network
import networkx as nx

import CB_Functions as cbfunc
import CB_Formatting as cbform

import instaloader as il

import threading as th

mesh = Network(height="100%", width="100%", bgcolor="#222222", font_color="white")


L = il.Instaloader()
L.load_session_from_file("notasnakepython")

nxg = nx.Graph()

target = str(input("Target: "))
amtDepth = int(input("Depth: "))


level1 = cbfunc.IL_GetFollowers(L, target)


def levelDown(L, i):
    nxg.add_node(i.username, length=amtDepth*400, color="white")
    nxg.add_edge(0, i.username)

    for x in cbfunc.IL_GetFollowers(L, i.username):
        nxg.add_node(x.username, length=amtDepth*25, color="blue")
        nxg.add_edge(i.username, x.username)


if level1 != False:
    threads = []
    for i in level1[0:amtDepth]:
        xth = th.Thread(target=levelDown, args=(L, i, ))
        threads.append(xth)
        xth.start()

    threads2 = []
    for i in level1[0:amtDepth]:
        xth = th.Thread(target=levelDown, args=(L, i, ))
        threads2.append(xth)
        xth.start()
else:
    print("Error")
    print(f"{cbform.C.CRED}Error getting list of followers{cbform.C.ENDC}")
    
while [x for x in threads if x.is_alive()]:
    while [x for x in threads2 if x.is_alive()]:
        pass
else:
    mesh.from_nx(nxg)
    mesh.show(f"{target}.html")