from Project2_parts.gui_functions.get_Full_Indexing_Cosine import get_Full_Indexing_Cosine
from Project2_parts.gui_functions.get_Full_Indexing_PCC import get_Full_Indexing_PCC
from Project2_parts.gui_functions.get_Full_NoIndexing_Cosine import get_Full_NoIndexing_Cosine
from Project2_parts.gui_functions.get_Full_NoIndexing_PCC import get_Full_NoIndexing_PCC
from Project2_parts.gui_functions.get_IDF_Indexing_Cosine import get_IDF_Indexing_Cosine
from Project2_parts.gui_functions.get_IDF_Indexing_PCC import get_IDF_Indexing_PCC
from Project2_parts.gui_functions.get_IDF_NoIndexing_Cosine import get_IDF_NoIndexing_Cosine
from Project2_parts.gui_functions.get_IDF_NoIndexing_PCC import get_IDF_NoIndexing_PCC
from Project2_parts.gui_functions.get_TED import getTED
import os
from Project2_parts.gui_functions.get_TF_Indexing_Cosine import get_TF_Indexing_Cosine
from Project2_parts.gui_functions.get_TF_Indexing_PCC import get_TF_Indexing_PCC
from Project2_parts.gui_functions.get_TF_NoIndexing_Cosine import get_TF_NoIndexing_Cosine

from Project2_parts.gui_functions.get_TF_NoIndexing_PCC import get_TF_NoIndexing_PCC

#Start button conditions 

def Start_btn(strings,Query, Combo1, Combo2, Combo3):
    # combo1 
        #   0: TF  
        #   1:IDF 
        #   2:Full
    # combo2 
        #  0: no indexing 
        #  1: with
    # combo3 
        #   0: PCC 
        #   1: Cosine        


    #No indexing 
        
        #TF

    if(Combo1.current()==0 and Combo2.current()==0 and Combo3.current()==0):
        #TF No_Indexing PCC
        get_TF_NoIndexing_PCC(strings, Query)

    elif(Combo1.current()==0 and Combo2.current()==0 and Combo3.current()==1):
        #TF No_Indexing Cosine
        get_TF_NoIndexing_Cosine(strings, Query)


        #IDF

    elif(Combo1.current()==1 and Combo2.current()==0 and Combo3.current()==0):
        #IDF No_Indexing PCC
        get_IDF_NoIndexing_PCC(strings, Query)

    elif(Combo1.current()==1 and Combo2.current()==0 and Combo3.current()==1):
        #IDF No_Indexing Cosine
        get_IDF_NoIndexing_Cosine(strings, Query)


        #Full

    elif(Combo1.current()==2 and Combo2.current()==0 and Combo3.current()==0):
        #Full No_Indexing PCC
        get_Full_NoIndexing_PCC(strings, Query)

    elif(Combo1.current()==2 and Combo2.current()==0 and Combo3.current()==1):
        #Full No_Indexing Cosine
        get_Full_NoIndexing_Cosine(strings, Query)

    

    #With indexing 
        
        #TF

    if(Combo1.current()==0 and Combo2.current()==1 and Combo3.current()==0):
        #TF Indexing PCC
        get_TF_Indexing_PCC(strings,Query)

    elif(Combo1.current()==0 and Combo2.current()==1 and Combo3.current()==1):
        #TF Indexing Cosine
        get_TF_Indexing_Cosine(strings,Query)


        #IDF

    elif(Combo1.current()==1 and Combo2.current()==1 and Combo3.current()==0):
        #IDF Indexing PCC
        get_IDF_Indexing_PCC(strings,Query)

    elif(Combo1.current()==1 and Combo2.current()==1 and Combo3.current()==1):
        #IDF Indexing Cosine
        get_IDF_Indexing_Cosine(strings,Query)


        #Full

    elif(Combo1.current()==2 and Combo2.current()==1 and Combo3.current()==0):
        #Full Indexing PCC
        get_Full_Indexing_PCC(strings,Query)

    elif(Combo1.current()==2 and Combo2.current()==1 and Combo3.current()==1):
        #Full INdexing Cosine
        get_Full_Indexing_Cosine(strings,Query)

    





