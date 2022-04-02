def Insert(Ai_depth , Bj_depth, i, LD_pairA_size):
    
    if(Ai_depth<=Bj_depth or i==LD_pairA_size):
        return 1
    else:
        return 1000 # a much higher value than others 
                    # so that it is not MIN
                    #  because min cannot run if this function returns a NoneType