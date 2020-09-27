# Self Replicating Insanity
Script that replicates itself with unique filenames. Ability to run the replicated files, which usually ends up with the machine crashing.

[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/smcclennon/SRI.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/smcclennon/SRI/context:python)
[![Maintainability](https://api.codeclimate.com/v1/badges/a4e85e15988e4dab380f/maintainability)](https://codeclimate.com/github/smcclennon/SRI/maintainability)
[![License](https://img.shields.io/github/license/smcclennon/SRI)](LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/smcclennon/SRI)](https://github.com/smcclennon/SRI/commits)
[![HitCount](https://hits.dwyl.com/smcclennon/SRI.svg)](https://hits.dwyl.com/smcclennon/SRI)

## Features
- Write the current file contents into another file (duplicate/replicate itself)
- Compatible with linux (tested on Fedora 32)
- Generate unique filenames (doesn't exceed 120 characters)
- Create hundreds of files per second
- INSANE MODE: Run the replicated files (Windows only)
- INSANE MODE: Fill up ram incredibly quickly and crash the machine (Windows only)
- Window titles state what replication generation the file is (Windows only)

## Installation
1. Visit the raw page for [`Self Replicating Insanity.py`](https://raw.githubusercontent.com/smcclennon/SRI/master/Self%20Replicating%20Insanity.py)
2. Press `CTRL+S` and save the page (alternatively, right click the page and press "Save page as")

#### Requirements:
- Python 3.6+
- Windows 10 for all features, Linux for limited features

## Insane Mode
Normally, SRI would replicate itself over and over, creating lots of files.
With Insane Mode enabled, SRI can now run the replicated files, which can then help it replicate and run even more files. This gets out of hand very quickly.
##### Generation 0: The original script has just been run (1 running)
![Console window (Gen 0)](https://smcclennon.github.io/assets/images/screenshots/SRI/console-g0.png)
##### Generation 1: The original script (S1) has generated and ran S2 (2 running)
![Console window (Gen 1)](https://smcclennon.github.io/assets/images/screenshots/SRI/console-g1.png)
##### Generation 2: S1 and S2 have replicated themselves and ran the new scripts (4 running)
![Console window (Gen 2)](https://smcclennon.github.io/assets/images/screenshots/SRI/console-g2.png)
##### Generation 3: S1, S2, S3, and S4 have replicated themselves and ran the new scripts (8 running)
![Console window (Gen 3)](https://smcclennon.github.io/assets/images/screenshots/SRI/console-g3.png)
##### Generation 4: S1, S2, S3, S4, S5, S6, S7, S8 have replicates themselves and ran the new scripts (16 running)
![Console window (Gen 4)](https://smcclennon.github.io/assets/images/screenshots/SRI/console-g4.png)
##### Hypothetical Generation calculations
|Generation|What's happened|Scripts Running
|:-:|-|:-:|
|10|S1-20 replicated and ran the new scripts|1,024|
|20|S1-40 replicated and ran the new scripts|1,048,576|
|50|S1-100 replicated and ran the new scripts|1,125,899,906,842,624|

## File explorer screenshot
![File output (file explorer)](https://smcclennon.github.io/assets/images/screenshots/SRI/file-explorer.png)

*Written in Python 3.8 on Windows 10*