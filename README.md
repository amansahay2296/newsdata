# newsdata
Udacity Full Stack Nanodegree-Log Analysis

This is the third project for the Udacity Full Stack Nanodegree. 
In this project, a large database with over a million rows is explored by building complex SQL queries to draw business conclusions for the data. 
The project mimics building an internal reporting tool for a newpaper site to discover what kind of articles the  readers like. 
The database contains newspaper articles, as well as the web server log for the site.



**Requirements**

Python3
Vagrant
VirtualBox


**Usage**

Install Vagrant And VirtualBox.
 
 
Download or Clone <a href ="https://github.com/udacity/fullstack-nanodegree-vm">fullstack-nanodegree-vm</a> repository.

Launch Vagrant VM by running **vagrant up**, you can the log in with **vagrant ssh**

Download the <a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip">data</a> from here.

To load the data, use the command **psql -d news -f newsdata.sql** to connect a database and run the necessary SQL statements.


To execute the program, run **python3 get-news-data.py** from the command line.
