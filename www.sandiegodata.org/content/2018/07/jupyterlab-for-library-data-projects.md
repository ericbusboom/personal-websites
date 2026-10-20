---
title: "JupyterLab For Library Data Projects"
date: 2018-07-08T16:00:17+00:00
draft: false
categories: ["News"]
author: "eric"
description: "Hosted Jupyter notebooks ( JupyterLab!) for Library data analysts with a Redmine account."
---

One of the difficult parts of working on a Data Library project is setting up all of the tools, including Python, Jupyter, Metatab, Pandas and several others. To make it easier to get started, I've set up a hosted instance of JupyterHub, which will allow analysts to run Jupyter notebooks in the cloud. And, the instance uses Redmine for authentication, so you won't need to create yet another account.

Once you have [joined a project](<http://www.sandiegodata.org/projects/join/>) and gotten a [Redmine account](<https://redmine.civicknowledge.com/>), you can use your Redmine account username and password to log into [jupyter.civicknowledge.com](<https://jupyter.civicknowledge.com/>). You'll get a new JupyterLab server. JupyterLab is a lot like Jupyter Notebook, but has a spiffier interface.

If you are an analyst on a Data Library project please try it out and let me know how it works:

  1. Visit <https://jupyter.civicknowledge.com/>
  2. Enter your username and password for your Redmine project management site account.
  3. Try creating a new Notebook in your 'work' directory. (The 'shared' directory is for official business. )


Note that this environment lets you start up a terminal window, so you can use git to store and share notebooks. Only work you put in the `work` directory will be persisted, and anything that's really valuable should be managed with git.

## Run an Example Analysis

We've got an example analysis notebook that you can run in JupyterLab. Once you have logged in and the JupyterLab window open:

  1. In the "Launcher" window, click on the Terminal tile to open a new terminal, or, use the menus: "File > New > Terminal. " You should get a back screen with white text.
  2. Type "cd work" to change to the 'work' directory.
  3. Clone the example notebook repository by typing: "git clone https://github.com/san-diego-water-quality/example-analysis.git"
  4. Switch to the file browser by clicking on "File" in the tabs on the left side of the screen. Click into the "work" directory, then click into "example-analysis"
  5. Click on the file "TMDL.ipynb" to open the example notebook.
  6. In the 'Run' menu, click on "Run All Cells"


Here is an example of the process above.
