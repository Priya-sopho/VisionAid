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

Following are the function alongwith keyboard keys to be pressed to execute:
 >1. Pause/Resume - Space
 >2. Change Speed - up key to increase speed, down key to decrease speed
 >3. Find a keyword in file - f
 >4. Jump on a specific page - j
 >5. Rewind (Move 10 lines back) - left key
 >6. Repeat - r
 >7. Skip current page - right key
 >8. Quit - Esc key or q 

**WORD READER**

WordReader to listen the content of word file
Following are the function alongwith keyboard keys to be pressed to execute:
> 1. Pause/Resume - Space
>2. Change Speed - up key to increase speed, down key to decrease speed
>3. Find a keyword in file - f
>4. Jump on a specific para - j
>5. Rewind (Move 10 lines back) - left key
>6. Repeat - r
>7. Skip current para - right key
>8. Quit - Esc key or q 


**MS WORD DOCUMENT HANDLING**

Following are the numerical keys to press after menu prompt
>1. Read the word doc
>2. Add a Heading
>3. Add new Para
>4. Add formatted text
>5. Change Font style of Doc
>6. Add Table
>7. Add Picture 
>8. Delete a paragraph containing a particular word 
>9. Delete the last paragraph


**NEWS READER**

Following are the function alongwith keyboard keys to be pressed to execute:
 >Pause/Resume - Space
 >Change Speed - up key to increase speed, down key to decrease speed
 >Repeat - r
 >Move to next category - right key
 >Quit - Esc key or q



**File exploration**

1. No installation required.

2. open_MyPc() will list/speak all drives on your system.

3. change directory name in get_directory_list(), and it will print/speak all files, audio,directory,pdf,doc within that directory .

4. change create_directory("F:","ok") , replace "F:" by the path where you want to create a new directory and replace "ok" by folder name. If folder name already exist it will print 0 else 1.

5. Similarly change path for copy_file() and copy_directory(). 

**Web Browser**
  	Following keys to be used for keyboard interrupts
	>1. Pause/play- Space
	>2. Exit - q
	>3. Reading bookmark/History - r
	>4. Add Bookmark - b
	>5. Google Search - f
  
