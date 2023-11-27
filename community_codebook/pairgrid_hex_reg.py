def pairgrid_hex_reg(df, variables=None, x_vars=None, y_vars=None, hex=True, hex_size=15, n_x_bins=15):
    '''
    For larger datasets, better than pairgrid or anything that creates scatterplots. 
    Plots hexbins with a linear and lowess best fit line for each combination
    of variables.   
    
    Optional vars:
    variables         - list of variable names to plot 
    x_vars and y_vars - to separately control which variables to plot on x and y axis, 
                        use these instead of variables 
    hex               - bool 
                        if true, plots hexbins and hex_size is relevant
                        else, bins x into n_x_bins is binned with avg +/- sd
    hex_size          - int  (larger numbers makes hexbins smaller)
    n_x_bins          - int 
    '''
    
    import matplotlib.pyplot as plt
    import seaborn as sns 
    
    def hexbin(x, y, color, **kwargs):
        '''
        sns doesn't have a hexbin plot but matplotlib does
        '''
        cmap = sns.light_palette(color, as_cmap=True)
        plt.hexbin(x, y, gridsize=hex_size, cmap=cmap, **kwargs)
            
    if x_vars and y_vars:
        g = sns.PairGrid(df, x_vars=x_vars, y_vars=y_vars,)
        g.map(sns.regplot,scatter=False,lowess=True,line_kws={"color": "C1"})
                
        if hex:
            g.map(sns.regplot,scatter=False,line_kws={"color": "C2"})
            g.map(hexbin)
        else:
            g.map(sns.regplot,line_kws={"color": "C2"},x_bins=n_x_bins,x_ci='sd')
       
    else: # square plot with all vars, diag is hist 
    
        if variables: # reduce to subset of vars if requested 
            df = df[variables]
    
        g = sns.PairGrid(df, corner=True)
    
        g.map_diag(sns.histplot)
        g.map_lower(sns.regplot,scatter=False,lowess=True,line_kws={"color": "C1"})
        
        if hex:
            g.map_lower(sns.regplot,scatter=False,line_kws={"color": "C2"})
            g.map_lower(hexbin)
        else:
            g.map_lower(sns.regplot,line_kws={"color": "C2"},x_bins=n_x_bins,x_ci='sd')       
        
    return g
