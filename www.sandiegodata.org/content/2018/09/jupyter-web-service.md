---
title: "Jupyter Web Service"
date: 2018-09-28T11:52:51+00:00
draft: false
categories: ["News"]
author: "eric"
description: "JupyterLab online for easier Data analysis."
---

![](http://jupyter.org/assets/hublogo.svg)

The Data Library now offers a new Jupyter web service, where you can get an (almost) fully configured Jupyter installation, without fighting the installation on your own machine. It's probably best to install it yourself, if you can, but for everyone else, this service is a great option. The Url is: <http://jupyter.sandiegodata.org> You log into the service with Github, but before you can log, your github account must be a member of the [SDRDL Data Projects](<https://github.com/sandiegodata-projects>) Github organization. Email your github user id to eric@sandiegodata.org to request access. 

## Using The Service

If you have a repo named 'sandiegodata' in your personal account ( not in an organization you are part of ) the server will clone that repo when it creates a new server. You can use this repo to pull in other repos by [adding the other repos as submodules](<https://chrisjean.com/git-submodules-adding-using-removing-and-updating/>) to your sandiegodata repo. The repo will be cloned into the work directory of the servers user account, **jovyan**.
