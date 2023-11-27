# The GitHub Workflow


If you are
1. Working on an assignment,
2. Working on a project,
3. Or taking notes in class (aka every class meeting)

**Then use the 3 step GitHub workflow below!**

```{admonition} In summary:
:class: tip

**Fetch first, commit frequently, push often!**

This habit will help you avoid disasters so that you get the positive features of GitHub without the headaches.
```
_Being careful about these steps might seem pointless during solo projects, but I encourage you to practice these good habits now so that when you do collaborative work, you're protected from mistakes._

## The workflow, explained

````{dropdown} 1. Make your coffee, open GitHub Desktop, and **FETCH** the project(s) you'll work on. 
1. Change the "current repository" to the assignment you want to work on (or project, or your notes repo, etc.)
1. Click "Fetch origin" to download any changes from the master repo on the GitHub servers. This is important because if someone else changed the files while you were sleeping, you'll get the most updated files to work on. 
1. Start your work on your computer. 

![](https://media.giphy.com/media/xUOrwpPFzqDh48XEek/giphy.gif)

```{warning}
If you don't "fetch" your project before you start, it becomes easier to change a file someone else changed differently, creating a conflict. When this happens, you have to resolve the conflicting files before moving on. 
```

```{admonition} Tips
:class: tip
1. Fetch the textbook repo every day before and after class. I add lecture slides as the semester goes on. 
1. Doing this makes it easy to copy textbook code into your own repos when it's useful. 
1. Don't do any work inside the textbook repo because your work will get ignored and overwritten. Work instead in your class notes repo. 
```

````

````{dropdown} 2. **"COMMIT" FREQUENTLY** (say every 30 minutes or so, but depends on the team/task): 

A "commit" records changes to files in the repo. 

- Save the files you're working on. (Just like you would while working on a Powerpoint or Word document.) 
- When you save the file, GitHub Desktop (GHD) will notice it has been changed. 
- Now go to GDH. Notice that your file is listed as a "changed" file. 
- **Describe those changes in the "Summary" and (optionally) "Description" boxes, and click the blue "Commit" button**. 
- Try to do this every time you save your files! It will make rolling back changes easier. 
- **Do this early and often**

```{panels}
![](https://media.giphy.com/media/l4KhSYN6hQ7Y0FZS0/giphy.gif)
---
![](https://media.giphy.com/media/dxITs87fTAxTncZ6WL/giphy.gif)
```
````

```{dropdown} 3. **"PUSH" OFTEN, but probably less than you commit** (say every 60-90 minutes or so, but depends on the team/task): 

A "push" updates the remote 

- Push your changes to the cloud by clicking the blue "push" button in GHD. 
- Now, you've got an up-to-date backup, and teammates can see the changes and work with the latest files.
- GHD will warn you if someone else made a change in the meantime. If this happens, click "fetch" to download what they did. If there is a conflict between your work and your teammate's, you'll have to resolve it. 

![](https://i.imgflip.com/4m0jf6.jpg)

```

```{admonition} On your last push of any day
:class: warning

At the end of your work session, before your last push of the day: **Clear all outputs, delete temp files, and then run the whole directory (whether it is multiple scripts or a single script) to make sure the outputs reproduce!** (Check: Did it work right?) 

Quick trick: [If the project uses notebook files, always look to see if the first executed code block has "[1]" next to it and that all the subsequent code blocks are numbered consecutively.](../01/06_python.html?highlight=golden#clear-output-and-rerun-from-the-start) 

```






