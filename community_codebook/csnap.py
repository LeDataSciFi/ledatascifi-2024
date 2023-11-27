def csnap(df, fn=lambda x: x.shape, msg=None):
    """ Custom Help function to print things in method chaining.    
        Will also print a message, which helps if you're printing a bunch of these, so that you know which csnap print happens at which point.
        Returns back the df to further use in chaining.
        
        Usage examples - within a chain of methods:
            df.pipe(csnap)
            df.pipe(csnap, lambda x: <do stuff>)
            df.pipe(csnap, msg="Shape here")
            df.pipe(csnap, lambda x: x.sample(10), msg="10 random obs")
            
        Source: Actual original writer unknown to me right now. 
    """
    if msg:
        print(msg)
    display(fn(df))
    return df
