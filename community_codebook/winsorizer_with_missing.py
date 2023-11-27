def winsorizer_with_missing(df,low_=.01,hi_=.99,cols=None): 
    '''
    Parameters
    ----------
    df : DATAFRAME
    low_ : float, optional (default = 0.01)
        What to winsorize the left tail of each variable to.
    hi_ : float, optional (default = 0.99)
        What to winsorize the right tail of each variable to.
        Set to 0.95 for 5% winsorizing, or .99 for 1% winsorizing.
    cols : list, required
        What columns to winsorize

    Returns
    -------
    df, with columns altered by winsorizing. 
    
    Description
    -------    
    Winsorize columns of a dataframe. It ignores missing values, which 
    is usually what you want. 
        
    TIP: Put this function in your codebook to reuse easily.

    TIP/WARNING: This is a new function and hasn't been subject to much scrutiny.
    So check its work! After using it, summarize the variables you wanted to 
    winsorize and see that the max and min equal the right percentiles!

    EXTRA CREDIT: (1) Use this function such that it performs winsorization within
    groups or (2) change this function so it optionally takes an argument that specify
    groups to do the winsorizing within. 

    Warning/option for extra credit: There is NO error checking in this function.
    (For example: What happens if you set low_ = -1, or low_=1.1? What "should" this
    function do if a user sets those values?)
    
    CURIOUSITY/EXTRA CREDIT: How does this function deal with ties? Check by using 
    tiny dataframe (20 rows max, but with ties just below, right at, and just above
    the cutoffs). 
    
    '''
    if not cols: # if no cols provides, stop, and force an error in the code
        print("You didn't tell me what columns to winsorize!")
        errrrorororororororor # this will cause a break (this is not good coding practice, but works, lolz)
        
    df[cols] = df[cols].clip(lower=df[cols].quantile(low_),
                             upper=df[cols].quantile(hi_),
                             axis=1)
    return df
