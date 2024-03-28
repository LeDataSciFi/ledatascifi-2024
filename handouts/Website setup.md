# Setting up a website to show off your work
### 04/05/2022

## PURPOSE 
- Learn how to build a website to show off some cool stuff

## GOALS
- Use GitHub Pages to build a website a resume-style website and showcase projects, including your midterm
- Use GitHub Pages to create a website for your final group project at the end of the semester
- Show examples of what you can do with GitHub Pages
- Show examples of “above and beyond” the minimal expectations for a website

## GITHUB PAGES OVERVIEW
- Fast, easy, free way to create and host a website
- Hosted on GH’s servers
- Not required to pay to register for a domain name—though you still can
- Examples:
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
	- https://donbowen-portfolio-frontier-streamlit-dashboard-app-yentvd.streamlit.app/
		- Made by https://github.com/donbowen/portfolio-frontier-streamlit-dashboard/
		
## WALKTHROUGH
### Personal website (template version)
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
- Edit midterm_summary.md 
	- This should be a high level over view (question, approach, findings, discussion)
	- Incorporate your summary of your midterm analysis or progress on it
- Practice: Convert any ipynb from the class notes folder into MD, add to website (follow steps on the regression_practice page on the website template we are using)
    - On JupyterLab, save and export any ipynb file into markdown
    - Add that resulting markdown file to your website repo
    - Link to your markdown file by editing index.md
	- Edit the layout (see regression_practice.md and the "30 second fix" below)
- Note on layout:
    - The template limits you to the “Minimal” theme preset on GitHub.com
    - For more customizability, you can create your own GitHub Pages using other theme presets with themes


### Getting started on a team project website
- Only one person on each team needs to do this.
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

## A little summary of some of your options for creating websites:

| Option                                                                                                                                 | Pros                                                                                                                                                                                                 | Cons                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Default GitHub templates and Markdown files <br> <ul> <li> https://donbowen.github.io/ </li><li> https://donbowen.github.io/teamproject/   </li></ul>                 | <ul> <li> Easy start </li><li>  Can use Plotly, Altair to make interactive charts     </li></ul>                                                                                                                                 | <ul> <li> Need explicit page links for interactive table of contents, navigation bar </li><li>  Limited customization options </li><li>  Have to “paste” output content into Markdown files </li><li>  Have to manually convert .ipynb files into MD or HTML to post </li></ul> |
| Finding templates that you like, forking, and customizing  <br> <ul> <li> **https://jekyllthemes.io/** </li><li> **http://jekyllthemes.org/** </li><li> https://html5up.net/   </li></ul> | <ul> <li> Also easy start </li><li> Better customization options </li><li> Many have already-developed interactive table of contents, navigation bar, etc. features </li><li> Can also use Plotly, Altair to make interactive charts  </li></ul> | <ul> <li> Have to learn template's repo organizations </li><li> Need to reconfigure templates’ files to suit your own needs </li><li>  Have to “paste” output content into Markdown files </li><li>  Have to manually convert .ipynb files into MD or HTML to post </li><li> Some additional setup needed  </li></ul>                                                          |
| Fastpages - https://github.com/fastai/fastpages                                                                                        | <ul> <li> Publishes ipynb files automatically </li><li> Interactive visualizations work automatically        </li></ul>                                                                                                          | <ul> <li> More overhead learning   </li></ul>                                                                                                                                                                           |
| Jupyterbooks  <br> <ul> <li> https://jupyterbook.org/ </li><li> https://ledatascifi.github.io </li></ul> | <ul> <li> Oh la la </li><li> Lots of customization options </li><li> Best for larger projects </li></ul> | <ul> <li> Have to learn template's repo organizations </li><li> Need to reconfigure templates’ files to suit your own needs </li><li> Some additional setup needed  </li></ul>                                                          |

