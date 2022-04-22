from Project2_parts.Part1_CompareVectors.vector.Filter_Text import Filter_Text


def my_upd(query,myVar):
    query=myVar.get()
    text_to_search_for=query
    #remove special characters, I, a
    filtered_text_to_search_for = Filter_Text(text_to_search_for)
    #remove leading / trailing whitespaces
    Query = filtered_text_to_search_for.strip()
    print(Query)
    return Query
