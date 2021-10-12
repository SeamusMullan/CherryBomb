import CB_Formatting as cbform
import CB_Functions as cbfunc


def main():
    L = cbfunc.IL_Login("notasnakepython", "44B6p&fCx#")
    if L:
        print("Login Successful")
    else:
        print("Login Failed")

    print(cbfunc.IL_GetFollowees(L, "notasnakepython"))

main()