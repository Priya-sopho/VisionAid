# VisionAid
Smart India Hackathon'18

Problem Statement:
Create an app that can run on a Windows/Linux based desktop to aid the disabled persons to perform day to day tasks

General Problem Statement : 
The disabled (blind) persons currently need support to start the PC , login their user id and passwords and then the access to certain browsers to do browsing. We must try to resolve this problem. 
Users: Disabled (Blind) persons for reading / browsing / performing word documentation. 
Technical Solution : Create the service in windows that listens to the finger print sensors and if the sensors match to the PC owner, allow the person to login and immediately start listening to commands as the blind person will not be able to see the next window / or won’t be able to open something. 
Desired Solution : i. The app must begin as a service that shall run in the background. Allow to register the disabled person with one time help from non-disabled person.
ii. The service must be integrated with figerprint sensors and must be able to validate the fingerprint of the disabled person and allow the access of this person to the app.
iii. The service upon successful logon immediately allows you to start sending the commands that allow the blind person to perform web browsing
iv. The service must allow to start accepting the commands to perform ms-word document.
v. The service must be generic to accept new interfaces like using read out loud feature in pdf to open and read a pdf and integrate / operate the other windows applications.


Link to app features description: https://docs.google.com/document/d/1ubM8JUVAbIcTJrNVtJKH_70syNb7xKPaqf9o3gHDKA4/edit?usp=sharing 

Link to log file:
https://docs.google.com/spreadsheets/d/1d9-0a-qe7w713yk49RsQJP3Sp2EWHebwGLGIMBaVspU/edit#gid=0

**Installation**

Run following commands :

> python setup.py install

> pip install -r requirements.txt

*Incase of installation errors try using **sudo** with pip command*

**Pdf Reader**

1.Change file name in pdfReader_keyboardinput.py script

2.Run 'python pdfReader_keyboardinput.py '

3.Press Ctrl+C to pause the script

Press any key except (1 - 10) to hear menu.

1-10 input follows certain task to perform as follows:

>1:Start - Begin with 1st line of pdf

>2:Pause

>3:Resume

>4:Exit

>5:Rewind 

>6:Repeat

>7:Skip current page

>8:Jump to a specific page

>9:Search

>10:Change speed of voice (-10 to 10)



**Music Player**

1.Change file name in music.py script

2.Run 'python music.py '

3.Press Ctrl+C to pause the script


**File exploration**

1. No installation required.

2. open_MyPc() will list/speak all drives on your system.

3. change directory name in get_directory_list(), and it will print/speak all files, audio,directory,pdf,doc within that directory .

4. change create_directory("F:","ok") , replace "F:" by the path where you want to create a new directory and replace "ok" by folder name. If folder name already exist it will print 0 else 1.

5. Similarly change path for copy_file() and copy_directory(). 

**Web Browser**
  
  1.Run **web_browser.py** using command: *python web_browser.py*

   >**googleSearch():** will perform a google search for spoken keyword and then return top 10 results.

   >**accessBookmarks():** will export the browser's boookmarks to a file called *bookmarks*.

   >**accessHistory():** will export the browser's history to a file called *history*.

   >**createBookmark():** will create a bookmark for the current webpage.
  
