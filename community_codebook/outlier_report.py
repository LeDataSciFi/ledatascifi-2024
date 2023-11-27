def outlier_report(df,vars_to_examine=None,color='red',thres=4,
                   return_df=False,no_print=False):
    '''
    Parameters
    ----------
    df : DATAFRAME
        Input dataframe
    vars_to_examine : LIST, optional
        List of variables to examine from dataframe. The default is df.columns.
    color : STRING, optional
        Color for cell highlighting. The default is 'red'.
    thres : int, optional
        Highlight cells where z score is above thres. The default is 4.
    return_df : Boolean, optional
        If true, will return the df obj (without styling) for further use. 
        The default is False.
    no_print : Boolean, optional
        If true, will not print. 
        The default is False.
    
    Displays (if no_print=False)
    -------
    Table with distribution of z-scores of variables of interest. 
    
    Returns (if return_df=True)
    -------
    Table with distribution of z-scores of variables of interest (without styling).     
    '''
        
    def highlight_extreme(s):
        '''
        Highlight extreme values in a series.
        '''
        is_extreme = abs(s) > thres
        return ['background-color: '+color if v else '' for v in is_extreme]
    
    if vars_to_examine==None:
        vars_to_examine=df.columns
    
    _tab = (
            # compute z scores
            ((df[vars_to_examine] - df[vars_to_examine].mean())/df[vars_to_examine].std())
            # output dist of z   
            .describe(percentiles=[.01,.05,.25,.5,.75,.95,.99]).T
            # add a new column = highest of min and max column
            .assign(max_z_abs = lambda x: x[['min','max']].abs().max(axis=1))
            # now sort on it
            .sort_values('max_z_abs',ascending = False)
    )
    
    if no_print == False:
        
        fdict = { c:('{:,.2f}' if c != 'count' else  '{:,.0f}') for c in _tab.columns   }

        display(_tab
             .style.format(fdict)
                   .apply(highlight_extreme, 
                          subset=['mean', 'std', 'min', '1%', '5%', '25%', '50%', '75%', '95%','99%', 'max', 'max_z_abs'])
        ) 

    
    if return_df == True:
        return _tab

