---
title: "Sharing Jupyter Notebooks with Google Colab"
date: 2019-04-19T10:06:31+00:00
draft: false
categories: ["News"]
author: "eric"
---

Google Colab offers hosted Jupyter notebooks that are integrated with Google Drive and Github. The customized Jupyter Notebook application has some nice features, and a few quirks, but has one feature that I've wanted for years: comments. This version of Jupyter Notebook seems perfect for collaborating on notebooks, which is otherwise very difficult. Here is a notebook that [demonstrates using the Data Library's Planning Database. ](<https://colab.research.google.com/drive/1TAdeN0TQmZotKfysh3Esd5OgiltnIVrQ>)You can also [link directly to cells.](<https://colab.research.google.com/drive/1TAdeN0TQmZotKfysh3Esd5OgiltnIVrQ?authuser=2#scrollTo=xBfNqgoxXZ6y>) This version of Jupyter Notebook is different enough that it takes getting used to; the keystrokes are a bit different, and the lifecycle of the kernel is a bit surprising, because you can both restart the backend IPython kernel and the container the kernel runs on. So, if you install Python modules or Debian packages, those installations will persist when you restart the kernel, but not if you restart the container. But, despite the differences, the commenting and collaboration features make any additional learning worth the effort.
