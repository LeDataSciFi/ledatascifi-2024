# Machine learning

We will spend the rest of class learning 
1. how to build a prediction model
1. how to optimize a prediction model
1. making that work with real world (messy!) data

## References

1. [Chap 7 explains many of the _**WHYS**_ behind why we are doing what we are doing](https://ledatascifi.github.io/ledatascifi-2024/content/05/03_ML.html) and introduces the new vocabulary you'll need to learn
1. [Chap 8 gives concrete code and pseudo code so you can get to work](https://ledatascifi.github.io/ledatascifi-2024/content/05/04a_SKLearn.html)
1. `sklearn` is the python package that most ML is built on (and other packages use identical or similar syntax).
    - [**Must read:** Getting started, a few short examples](https://scikit-learn.org/stable/getting_started.html) 
    - **[BOOKMARK NOW: You will visit its user guide frequently, it's really good!](https://scikit-learn.org/stable/user_guide.html)**
    - [Glossary of terms](https://scikit-learn.org/stable/glossary.html)
    - [The pipeline page](https://scikit-learn.org/stable/modules/compose.html)
    - [Preprocessing options](https://scikit-learn.org/stable/modules/preprocessing.html)
    - [Dealing with missing values](https://scikit-learn.org/stable/modules/impute.html)
    - Do you have too many variables? Two options: [Supervised feature selection](https://scikit-learn.org/stable/modules/feature_selection.html) or [unsupervised](https://scikit-learn.org/stable/modules/unsupervised_reduction.html)
    - [The "menu" of supervised learning models](https://scikit-learn.org/stable/supervised_learning.html) - go here if you are want to learn more about a model we run in class or see what's possible
    - Info on [cross validation](https://scikit-learn.org/stable/modules/cross_validation.html)
    - [How to optimize a model](https://scikit-learn.org/stable/modules/grid_search.html)
    - [What scoring functions can I set a model to optimize?](https://scikit-learn.org/stable/modules/model_evaluation.html)
1. EDA. Remember: ONLY do EDA on the training sample (never on the holdout sample)
    - `ydata-profiling` is great with two caveats: can be slow, generic insights
    - `dabl` is great - will suggest cleaning options and help see likely drivers of good models, and will even BUILD a starter model for you. But: BLACK BOX! And Caveat: It doesn't do CV.

## Notes and Vocab

You can take notes here if you want. I'll get you started:
- pipeline
- estimator
- transformer
- fit
- predict 
