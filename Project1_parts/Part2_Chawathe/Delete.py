def Delete(Ai_depth , Bj_depth, j, LD_pairB_size):
    if( (Ai_depth>=Bj_depth) or j==LD_pairB_size):
        return 1
    else:
        return 1000 # a much higher value than others 
                    # so that it is not MIN
                    #  because min cannot run if this function returns a NoneType