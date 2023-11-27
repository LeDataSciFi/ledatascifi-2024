def merge_type(df1,df2,on):
    '''
    This function has not been tested much. Could use test cases. E.g.: multiple key vars, missing vars within keys.
    '''
    # if there are duplicates, dropping them will shrink the key vector
    if len(df1[on]) > len(df1[on].drop_duplicates()):
        _l = "many"
    else:
        _l = "one"
    if len(df2[on]) > len(df2[on].drop_duplicates()):
        _r = "many"
    else:
        _r = "one"
    return "{}_to_{}".format(_l,_r)
