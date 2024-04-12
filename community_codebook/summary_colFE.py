# summary_col author:  @adrianmoss 
# author of this file: @donbowen, adapting code by @adrianmoss

from functools import reduce
from statsmodels.iolib.summary2 import Summary, _col_params, _col_info, _make_unique
import numpy as np
import pandas as pd

def summary_col(results, float_format='%.4f', model_names=(), stars=False,
                info_dict=None, regressor_order=(), drop_omitted=False,
                include_r2=True, fixed_effects=None, fe_present='Yes', fe_absent=''):
    """
    Summarize multiple results instances side-by-side (coefs and SEs) with
    optional fixed effects and summary cleaning.

    Parameters
    ----------
    results : statsmodels results instance or list of result instances
    float_format : str, optional
        float format for coefficients and standard errors
        Default : '%.4f'
    model_names : list[str], optional
        Must have same length as the number of results. If the names are not
        unique, a roman number will be appended to all model names
    stars : bool
        print significance stars
    info_dict : dict, default None
        dict of functions to be applied to results instances to retrieve
        model info. To use specific information for different models, add a
        (nested) info_dict with model name as the key.
    regressor_order : list[str], optional
        list of names of the regressors in the desired order. All regressors
        not specified will be appended to the end of the list.
    drop_omitted : bool, optional
        Includes regressors that are not specified in regressor_order.
    include_r2 : bool, optional
        Includes R2 and adjusted R2 in the summary table.
    fixed_effects : list[str], optional
        List of categorical variables for which to indicate presence of fixed effects.
    fe_present : str, optional
        String to indicate the presence of fixed effects. Default is "Yes".
    fe_absent : str, optional
        String to indicate the absence of fixed effects. Default is empty string.
    
    Returns
    -------
    Summary : statsmodels.iolib.summary2.Summary table instance, with improved FE display formatting
    
    Example
    --------
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import statsmodels.formula.api as smf
    from summary_colFE import summary_col # available at https://github.com/LeDataSciFi/ledatascifi-2024/tree/main/community_codebook
                                          # overrides, so don't use this: from statsmodels.iolib.summary2 import summary_col
                                          # pending PR in statsmodels: https://github.com/statsmodels/statsmodels/pull/9191 
    
    # Load the diamonds dataset
    diamonds = sns.load_dataset('diamonds')
    
    regressions = [
        (smf.ols('np.log(price) ~ carat', data=diamonds).fit(), 'log(Price) ~ Carat'),
        (smf.ols('np.log(price) ~ np.log(carat)', data=diamonds).fit(), 'log(Price) ~ log(Carat)'),
        (smf.ols('np.log(price) ~ C(cut)', data=diamonds).fit(), 'log(Price) ~ C(Cut)'),
        (smf.ols('np.log(price) ~ C(clarity)', data=diamonds).fit(), 'log(Price) ~ C(Clarity)'),
        (smf.ols('np.log(price) ~ carat + C(cut) + C(clarity)', data=diamonds).fit(), 'log(Price) ~ Carat + C(Cut) + C(Clarity)')
    ]
    
    info_dict={
           'No. observations' : lambda x: f"{int(x.nobs):d}"}

    summary = summary_col([reg[0] for reg in regressions],
                        model_names=[f'{i}. '+reg[1] for i, reg in enumerate(regressions, 1)],
                        stars=True, info_dict=info_dict, 
                        fixed_effects=['cut', 'clarity'],
                        )
    summary
    """

    if not isinstance(results, list):
        results = [results]

    cols = [_col_params(x, stars=stars, float_format=float_format,
                        include_r2=include_r2) for x in results]

    # Unique column names (pandas has problems merging otherwise)
    if model_names:
        colnames = _make_unique(model_names)
    else:
        colnames = _make_unique([x.columns[0] for x in cols])
    for i in range(len(cols)):
        cols[i].columns = [colnames[i]]

    def merg(x, y):
        return x.merge(y, how='outer', right_index=True, left_index=True)

    # Changes due to how pandas 2.2.0 handles merge
    index = list(cols[0].index)
    for col in cols[1:]:
        for key in col.index:
            if key not in index:
                index.append(key)
    for special in (('R-squared', ''), ('R-squared Adj.', '')):
        if special in index:
            index.remove(special)
            index.insert(len(index), special)

    summ = reduce(merg, cols)
    summ = summ.reindex(index)

    if regressor_order:
        varnames = summ.index.get_level_values(0).tolist()
        vc = pd.Series(varnames).value_counts()
        varnames = vc.loc[vc == 2].index.tolist()
        ordered = [x for x in regressor_order if x in varnames]
        unordered = [x for x in varnames if x not in regressor_order]
        new_order = ordered + unordered
        other = [x for x in summ.index.get_level_values(0)
                 if x not in new_order]
        new_order += other
        if drop_omitted:
            for uo in unordered:
                new_order.remove(uo)
        summ = summ.reindex(new_order, level=0)

    idx = []
    index = summ.index.get_level_values(0)
    for i in range(0, index.shape[0], 2):
        idx.append(index[i])
        if (i + 1) < index.shape[0] and (index[i] == index[i + 1]):
            idx.append("")
        else:
            idx.append(index[i + 1])
    summ.index = idx

    # add fixed effects info
    if fixed_effects:
        if not info_dict:
            info_dict = {}
        for fe in fixed_effects:
            info_dict[fe + ' FE'] = lambda x, fe=fe, fe_present=fe_present, fe_absent=fe_absent: fe_present if any(param.startswith(f'C({fe})') for param in x.params.index) else fe_absent

    # add infos about the models.
    if info_dict:
        cols = [_col_info(x, info_dict.get(x.model.__class__.__name__,
                                           info_dict)) for x in results]
    else:
        cols = [_col_info(x, getattr(x, "default_model_infos", None)) for x in
                results]
    # use unique column names, otherwise the merge will not succeed
    for df, name in zip(cols, _make_unique([df.columns[0] for df in cols])):
        df.columns = [name]

    info = reduce(merg, cols)
    dat = pd.DataFrame(np.vstack([summ, info]))  # pd.concat better, but error
    dat.columns = summ.columns
    dat.index = pd.Index(summ.index.tolist() + info.index.tolist())
    summ = dat

    summ = summ.fillna('')

    # fixed effects processing
    if fixed_effects:
        index_series = pd.Series(summ.index, index=summ.index)
        skip_flag = index_series.apply(lambda x: any(x.startswith(f'C({fe})') for fe in fixed_effects))
        skip_next_flag = skip_flag.shift(fill_value=False)
        final_skip = skip_flag | skip_next_flag
        summ = summ[~final_skip]

        r_squared_rows = summ.index[summ.index.str.contains('R-squared')]
        r_squared_section = summ.loc[r_squared_rows]
        summ = summ.drop(index=r_squared_rows)
        summ = pd.concat([summ, r_squared_section])

    smry = Summary()
    smry._merge_latex = True
    smry.add_df(summ, header=True, align='l')
    smry.add_text('Standard errors in parentheses.')
    if stars:
        smry.add_text('* p<.1, ** p<.05, ***p<.01')

    return smry

if __name__ == '__main__':
    
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import statsmodels.formula.api as smf

    # Load the diamonds dataset
    diamonds = sns.load_dataset('diamonds')

    # Adapted regressions for the diamonds dataset
    regressions = [
        (smf.ols('np.log(price) ~ carat', data=diamonds).fit(), 'log(Price) ~ Carat'),
        (smf.ols('np.log(price) ~ np.log(carat)', data=diamonds).fit(), 'log(Price) ~ log(Carat)'),
        (smf.ols('np.log(price) ~ C(cut)', data=diamonds).fit(), 'log(Price) ~ C(Cut)'),
        (smf.ols('np.log(price) ~ C(clarity)', data=diamonds).fit(), 'log(Price) ~ C(Clarity)'),
        (smf.ols('np.log(price) ~ carat + C(cut) + C(clarity)', data=diamonds).fit(), 'log(Price) ~ Carat + C(Cut) + C(Clarity)')
    ]
    
    info_dict={
           'No. observations' : lambda x: f"{int(x.nobs):d}"}

    summary = summary_col([reg[0] for reg in regressions],
                        model_names=[f'{i}. '+reg[1] for i, reg in enumerate(regressions, 1)],
                        stars=True, info_dict=info_dict, 
                        fixed_effects=['cut', 'clarity'],
                        )
    summary