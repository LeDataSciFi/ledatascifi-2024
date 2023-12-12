# Assignment 9: A website to show off your work

This webpage is a walkthrough that we will follow on a class day during the semester. After that class, you will have a working personal website and a website for your team project. 

## PURPOSE 
- Learn how to build a website to show off your portfolio of work
- You should update and improve the website, which will be graded for professionalism
- [Grading details are below](#Grading)

_Students with preexisting websites can use and update theirs._

## GOALS
- Use GitHub Pages to build a website a resume-style website and showcase projects, including your midterm
- Use GitHub Pages to create a website for your final group project at the end of the semester
- Show examples of what you can do with GitHub Pages
- Show examples of "above and beyond" the minimal expectations for a website

## GITHUB PAGES OVERVIEW
- Fast, easy, free way to create and host a website
- Hosted on GH's servers
- Can pay if you want the website to be at a custom URL

Examples:
- https://julioveracruz.github.io/
    - Made by https://github.com/julioveracruz/julioveracruz.github.io 
- https://julioveracruz.github.io/testwebsite/
    - Made by https://github.com/julioveracruz/testwebsite  
- https://donbowen.github.io/slides/
    - Made by https://github.com/donbowen/slides
- https://square.github.io/
    - Made by https://github.com/square/square.github.io 
- https://yelp.github.io/
    - Made by https://github.com/Yelp/yelp.github.io 
		
## WALKTHROUGH

### Personal website via a template

_Students with preexisting websites can use and update theirs._

To make it easier to build a website, we are going to make one using a template. 

- Go to https://github.com/donbowen/donbowen.github.io 
- Click the green [Use this template] button
- Name it *username*.github.io
    - If you already have a *username*.github.io repo, give it any name you want (perhaps something like, “personal-website”)
        - In the resulting repo, click Settings, then Pages, then make sure the source is the main branch, then save.
- Change the link in the about area to your username. Then go look at the website
- Edit config (to change the left sidebar picture and links)
    - Editable sections are text in blue
- Edit index.md (text and picture, portfolio descriptions, and links, etc)
    - Can edit directly on GitHub.com or through GitHub Desktop
- Replace the first portfolio item on the template with your midterm report file
    - In JupyterLab, open your report file 
        - Click File > "save and export as" > Markdown
        - This will generate a zip file (likely "report.zip"), extract the folder from this and upload the whole folder to your website repo.  
    - In index.md, it says `_**[Natural language processing 10-Ks to identify risks](midterm_summary)**_`. 
        - Update this to a name that fits your midterm report 
        - Update the link from `midterm_summary` (the path to my file) with yours ("report/report" if it is inside a folder or just "report" otherwise)
        - Update the summary description 
        - Update the picture by changing `<img src="images/dummy_thumbnail.jpg?raw=true"/>` to point at one of the pictures inside your report folder.
    - Save and commit these changes. After the website updates, refresh it 
        - Check the grammar, pictures, and if the link to the report works
        - Look at the report webpage
    - Update the report.md file so it looks better. Add these lines to the top of the file:
         ```text
         ---
         layout: wide_default
         ---  
         
         ```     
         
**Awesome! You have a working site! You should continue to improve it to include more things you want to show off.**
- Check that all links work
- Improve grammar 
- Add your team project
- Add additional portfolio items (links to reports and projects from other classes, for example)
    
_Note on layout: The template limits you to the “Minimal” theme preset on GitHub.com. For more customizability, you can create your own GitHub Pages using other theme presets._ 
    
    
### Getting started on a team project website

_Note: If your team's key output is a dashboard/app instead of a report, you can skip the team website._

- **Only one person on each team should do this.**
    - Your work for the project will be in a different repo I set up, but your project's website will be this one.
- Go to https://github.com/donbowen/teamproject
- Click the green [Use this template] button
- Name it something related to the project
    - You can change this later, but any links to the website will need to change
- In the resulting repo, click Settings, then Pages, then make sure the source is the main branch.
    - You can choose a different theme here if you want
- Change the link in the code/about area to the website URL. Then go look at the website
- Settings > Collaborators:
    - Add all teammates, and add the TA and Professor Bowen
- In each person's personal website, change the eventual project link to link to that website

### MOVING FORWARD

- GitHub Pages is just the start of what you could do with creating websites
- Above and beyond..
- Other templates, resources
    - https://github.com/mmistakes/mm-github-pages-starter/generate
    - https://github.com/fastai/fastpages 
    - https://html5up.net/
- HTML, CSS, Javascript-savvy users welcomed
- Open your webpage in Edge browser and ask the AI Copilot for suggestions to improve it


## A little summary of some of your options for creating websites:

| Option                                                                                                                                 | Pros                                                                                                                                                                                                 | Cons                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Default GitHub templates and Markdown files <br> <ul> <li> https://donbowen.github.io/ </li><li> https://donbowen.github.io/teamproject/   </li></ul>                 | <ul> <li> Easy start </li><li>  Can use Plotly, Altair to make interactive charts     </li></ul>                                                                                                                                 | <ul> <li> Need explicit page links for interactive table of contents, navigation bar </li><li>  Limited customization options </li><li>  Have to “paste” output content into Markdown files </li><li>  Have to manually convert .ipynb files into MD or HTML to post </li></ul> |
| Finding templates that you like, forking, and customizing  <br> <ul> <li> **https://jekyllthemes.io/** </li><li> **http://jekyllthemes.org/** </li><li> https://html5up.net/   </li></ul> | <ul> <li> Also easy start </li><li> Better customization options </li><li> Many have already-developed interactive table of contents, navigation bar, etc. features </li><li> Can also use Plotly, Altair to make interactive charts  </li></ul> | <ul> <li> Have to learn template's repo organizations </li><li> Need to reconfigure templates’ files to suit your own needs </li><li>  Have to “paste” output content into Markdown files </li><li>  Have to manually convert .ipynb files into MD or HTML to post </li><li> Some additional setup needed  </li></ul>                                                          |
| Fastpages - https://github.com/fastai/fastpages                                                                                        | <ul> <li> Publishes ipynb files automatically </li><li> Interactive visualizations work automatically        </li></ul>                                                                                                          | <ul> <li> More overhead learning   </li></ul>                                                                                                                                                                           |
| Jupyterbooks  <br> <ul> <li> https://jupyterbook.org/ </li><li> https://ledatascifi.github.io </li></ul> | <ul> <li> Oh la la </li><li> Lots of customization options </li><li> Best for larger projects </li></ul> | <ul> <li> Have to learn template's repo organizations </li><li> Need to reconfigure templates’ files to suit your own needs </li><li> Some additional setup needed  </li></ul>                                                          |

## Grading

The parts of the grade:
1. Professionalism - How would a potential employer looking at it feel about it
2. Deductions for non-working links
3. Deduction if duplicate template photo remains
4. Deductions for other unchanged template portions
5. At least two "portfolio items":
   - You can add or subtract the number of things you show. I included spots in the template for midterm, regression, team project, and something else. You don't need to use any or all of these. You should have at least 2 things, but there is no requirement about _what_ you show.
   - You can update any materials from our class. For example, if you want to include your midterm work, you can update and modify it however you'd like to so that it shows off what you've learned. 


