# LeDataSciFi

This readme is meant for myself and TAs, not students. 

This repo is the 2023 edition of LeDataSciFi. The [ledatascifi.github.io](https://ledatascifi.github.io) repo hosts the website, but simply redirects to the cover page for _**this**_ repo. In future years, make a new years' website as a new repo by cloning this one (don't forget the GH action that deploys it!), and alter the redirect from the ledatascifi.github.io to the new website. 

This repo contains the textbook, course details, data, and lecture files, making it simpler to move from year to year. The only portion of class _**outside**_ this repo is
- the org has teams for discussion and many repos for assignments, etc
- the class's discussion group is where I post assignment links, Zoom links, and schedule office hours appointments in a non-public place
- coursesite exists only to get initial link to join org to students
- the schedule and weekly tasks that are embedded in the dashboard page are an excel file on my computer

## Updating the website 

**To update the website, simply push any change in the main branch of the repo.** After a push, a GitHub Actions workflow (`.github/workflows/deploy.yml`) automatically builds and pushes the book in the `gh-pages` branch, and GitHub pages will update the website in <5 minutes. 

_Note for myself: `requirements.txt` contains the packages GitHub uses to build the website. The most "important" req is `sphinx-book-theme=0.0.39`, which implies that we are using `jupyter-book<=0.10.1`. The reason for this is that later versions use pydata themes which completely change TOC behavior. (Updating it and then reproducing the collapsing behavior and coloring would require updates to the css files, if the new pydata theme even allows collapsing.)_

## Adding new web pages, formatting changes, etc.

- **See the instructions in `building_this_site.yml`**, which tells how to build the book for _**local**_ viewing (quicker dev cycles than waiting for website to refresh)
- Typical task: After creating a new textbook page, to get this on the left navigation bar/TOC, you'll need to add that to the `_toc.yml` file. _**NOTE: The TOC uses formatting from jupyter-book 0.10.1!**_ 
- Overall website formatting is controlled by
    - `_config.yml` for most settings
    - `_toc.yml` lays out the book table of contents, ie the left nav bar
    - `_static/*` - any css or js I want to add to modify the base styling goes here
	- Be careful: jupyterbook settings and behavior are locked at v0.10.1!

## Credits

This project is created using the excellent open source [Jupyter Book project](https://jupyterbook.org/) and the [executablebooks/cookiecutter-jupyter-book template](https://github.com/executablebooks/cookiecutter-jupyter-book).


  
