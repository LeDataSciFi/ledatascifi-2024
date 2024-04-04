def df_after_transform(estimator,data):
    '''
    Do you want to run "estimator.fit_transform(data)" and then examine your data?
    ("estimator" being a pipeline or ColumnTransformer)
    
    Well, as of early 2021, sk-learn won't robustly give you the variable names. This 
    function will. 
    
    ==================================================================
    
    Usage example:
    
        from sklearn.pipeline import make_pipeline
        from sklearn.preprocessing import StandardScaler, OneHotEncoder
        from sklearn.impute import SimpleImputer
        from sklearn.compose import ColumnTransformer
        from sklearn.linear_model import Lasso
        
        X_train = pd.DataFrame({'prof_a': [23,12, 12, -4.5],
                              'industry': ['medical','medical', 'tech','tech']})        
        numeric_columns = ['prof_a']
        cat_columns     = ['industry']

        numeric_pipeline = make_pipeline(SimpleImputer(strategy='median'), StandardScaler())
        cat_pipeline     = make_pipeline(SimpleImputer(strategy='most_frequent'), OneHotEncoder())

        transformers = [
        ('num', numeric_pipeline, numeric_columns),
        ('cat', cat_pipeline, cat_columns),
        ]

        combined_pipe = ColumnTransformer(transformers, remainder='passthrough')

        df_after_transform(combined_pipe,X_train)

        >         prof_a  industry_medical  industry_tech
        >    0  1.260252               1.0            0.0
        >    1  0.140028               1.0            0.0
        >    2  0.140028               0.0            1.0
        >    3 -1.540308               0.0            1.0

        ######################################################################
        # warning - this function ONLY works with a ColumnTransformer object
        # for example, these next two commands will NOT work:
        ######################################################################
        
        # if your pipeline has an estimator after the CT, this fcn will fail:
        
        df_after_transform(make_pipeline(combined_pipe,Lasso()), X_train)
        
        # if your pipeline is just a simple transformer, this fcn will fail:
        
        df_after_transform(SimpleImputer(), X_train)        

    ==================================================================
    
    Source: https://stackoverflow.com/a/57534118
    
    "Right now, any method that uses the transformer api in sklearn returns a numpy array 
    as its results. Usually this is fine, but if you're chaining together a multi-step 
    process that expands or reduces the number of columns, not having a clean way to track 
    how they relate to the original column labels makes it difficult to use this section of 
    the library to its fullest."
        -Jonathan Bechtel

    "SKlearn still doesn't have complete support for tracking the feature_names...
    Anyhow, we can create wrappers to get the feature names of the ColumnTransformer"
        -Venkatachalam

    '''
    
    import sklearn
    if not isinstance(estimator, sklearn.compose._column_transformer.ColumnTransformer):
        raise Exception('This function only accepts a column transformer')
        
    from sklearn.feature_extraction.text import _VectorizerMixin
    from sklearn.feature_selection._base import SelectorMixin
    import pandas as pd
    from sklearn.pipeline import Pipeline
    import scipy

    def get_feature_out(estimator, feature_in):
        
        if hasattr(estimator,'get_feature_names_out'):
            if isinstance(estimator, _VectorizerMixin):
                # handling all vectorizers
                return [f'vec_{f}' \
                    for f in estimator.get_feature_names_out()]
            else:
                return estimator.get_feature_names_out(feature_in)
        elif isinstance(estimator, SelectorMixin):
            return np.array(feature_in)[estimator.get_support()]
        else:
            return feature_in


    def get_ct_feature_names(ct):
        # handles all estimators, pipelines inside ColumnTransfomer
        # doesn't work when remainder =='passthrough'
        # which requires the input column names.
        output_features = []

        for name, estimator, features in ct.transformers_:
            if name!='remainder':
                if isinstance(estimator, Pipeline):
                    current_features = features
                    for step in estimator:
                        current_features = get_feature_out(step, current_features)
                    features_out = current_features
                else:
                    features_out = get_feature_out(estimator, features)
                output_features.extend(features_out)
            elif estimator=='passthrough':
                output_features.extend(ct._feature_names_in[features])

        return output_features  
    
    trans_df = estimator.fit_transform(data)
    if type(trans_df) == scipy.sparse.csr.csr_matrix:
        trans_df = trans_df.toarray()
        
    return pd.DataFrame(trans_df,columns=get_ct_feature_names(estimator))

