def Update(Ai_depth, Ai_tag ,Bj_depth,Bj_tag):
    if(Ai_depth==Bj_depth):
        if(Ai_tag==Bj_tag):
            return 0
        else:
            return 1
    else:
        return 1000 # a much higher value than others 
                    # so that it is not MIN
                    #  because min cannot run if this function returns a NoneType -Charbel 