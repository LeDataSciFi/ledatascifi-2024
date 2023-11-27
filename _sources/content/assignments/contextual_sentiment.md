## How to measure "contextual sentiment" in a 10-K

If you want to assess the sentiment around a specific topic in a document, you need to create variables that describe it. This is particularly interesting when a firm has an overall positive tone but speaks relatively negatively about a specific topic. It can also be useful when you're interested in that particular topic. Here's how you can do it:

First, define a list of words that indicate the topic being discussed. For instance, to capture "Detroit Sports," you could include "Detroit Lions," "Red Wings" (specific enough that "Detroit" can be omitted), "Detroit Tigers," and "Detroit Pistons." However, figuring out how many synonyms to add can be tricky. Including too many may result in false positives (such as capturing discussions about other topics that contain only "Detroit" or only "Lions"), while including too few could lead to false negatives (missing discussions). Therefore, creating a topic list requires a lot of validation and hard work. If you propose a change, test it on example sentences and see if it affects the larger dataset.

Second, define regex patterns that can identify if the topic is being discussed positively. In class, we discussed how to do this using `NEAR_regex`. Here are the steps:

1.    Provide a list of strings like `["topic1", "topic2"]` to `NEAR_regex`. This function will create a regex that looks for `"topic1"` near `"topic2"`.
1.    Replace `"topic1"` with a "list" of strings to look for any of those words near `"topic2"`.
1.    To create the regex pattern, put a "|" between each term (`"|".join(list_of_words)`) and add parentheses around the whole thing. For example, `"(Detroit Lions|Red Wings|Detroit Tigers|Detroit Pistons)"`.
1.    `NEAR_regex` will output a complex regex pattern, which we can call `detroit_sports_positive_regex`.

```{tip}
[Visit the textbook to learn about anchor phrases (which is the technique you're using here) and the `NEAR_regex` function.](../04/02d_RegexApplication)
```

Third, check if that topic is being discussed positively.

1. Select one firm from the files you downloaded and open its 10-K file as a string variable, as if you were inside the loop you set up for this purpose
1. Clean the string by removing HTML tags and other non-word characters. You can refer to the notes from class or look through the textbook for guidance. Ensure that the cleaning process is working correctly before proceeding.
1. Use the regex pattern to count the number of times the document discusses the selected topic positively: `hits = len(re.findall(detroit_sports_positive_regex,<clean_10_text>))`, and then save `hits` to the correct variable in the row corresponding to that 10-K.
1. **Manually check it by opening the 10-K on the browser - do your functions give you the same values you'd create if you did it by hand?**

Fourth, repeat.

- Repeat those steps for the negative sentiment version: `detroit_sports_negative_regex`
- Repeat those steps for a second topic to create two more variables (one each for positive and negative nearby sentiments)
- Repeat those steps for a third topic (again: positive and negative sentiment)
- For each of those,
    - Open some 10-Ks manually and read them to verify if your guess for how to check actually results in hits.
    - If it doesn't work like you think (misses obvious discussions of the risk, or finds non-discussions), tweak it.

Finally, adjust this so it works on all documents

1. Figure out how to loop (yes, an actual for loop) over the dataframe. Within each row, extract and manipulate the available variables as needed so that you can find the corresponding document.
    - Looping over rows in a pandas dataframe is a little different than normal for-loops! Look up how to do it!
    - Test this out: Loop over the dataframe and just print out the filenames it should open. 
1. Once that works, continue to integrate the code above in the for loop.
1. **IMPORTANT!** After your code has supposedly done all the work, use `.describe()` on the new variables and check for issues.
    - Make sure you have observations for most/all firms for your new measures. **If not, fix it before proceeding!**
    - If any of your variables are always 0, it's meaningless. **Change it before proceeding!**
    
## Topics you might use (non-exhaustive list)

Remember, as mentioned above, once you choose a topic, you need to specify a list of words that indicate that topic is being discussed.

- High level/MBA/Porter's 5: Sales, demand, competition, regulation, suppliers, customers, employees, investment, innovation
- Places: Ukraine, Taiwan, 
- Risks: antitrust; litigation - e.g. patent, consumer, class action; real estate; inflation; commodity; supply chain; natural disasters; weather; employees (fraud, compensation, departure); changes in tax policy; currency rates; regulatory approval; reputation; refinancing; 
- Prof. Kathleen Hanley [has a recent paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2792943) on risks. It focuses on financial firms, which isn't our sample, but nevertheless, it contains a long list of risks in Table 5 you might find interesting.

