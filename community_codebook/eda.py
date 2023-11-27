###############################################################
#
# This function is... INSUFFICIENT. It was developed as an 
# illustration of EDA lessons in the 2021 class. It's quick and 
# works well. 
# 
# Want a  higher grade version of me? Then try pandas-profiling: 
# https://github.com/pandas-profiling/pandas-profiling
# 
###############################################################


def insufficient_but_starting_eda(df,cat_vars_list=None):
    '''
    
    Parameters
    ----------
    df : DATAFRAME
    cat_vars_list : LIST, optional
        A list of strings containing variable names in the dataframe
        for variables where you want to see the number of unique values
        and the 10 most common values. Likely used for categorical values.

    Returns
    -------
    None. It simply prints.
    
    Description
    -------    
    This function will print a MINIMUM amount of info about a new dataframe. 
    
    You should ****look**** at all this output below and consider the data
    exploration and cleaning questions from 
    https://ledatascifi.github.io/ledatascifi-2021/content/03/02e_eda_golden.html#member
    
    Also LOOK at more of the data manually. 
    
    Then write up anything notable you observe.
    
    TIP: put this function in your codebook to reuse easily.
    
    PROTIP: Improve this function (better outputs, better formatting).
    
    FEATURE REQUEST: optionally print the nunique and top 10 values under the describe matrix
    
    FEATURE REQUEST: optionally print more stats (percentiles)
    
    '''
    print(df.head(),  '\n---')
    print(df.tail(),  '\n---')
    print(df.columns, '\n---')
    print("The shape is: ",df.shape, '\n---')
    print("Info:",df.info(), '\n---') # memory usage, name, dtype, and # of non-null obs (--> # of missing obs) per variable
    print(df.describe(), '\n---') # summary stats, and you can customize the list!
    if cat_vars_list != None:
        for var in cat_vars_list:
            print(var,"has",df[var].nunique(),"values and its top 10 most common are:")
            print(df[var].value_counts().head(10), '\n---')
        
