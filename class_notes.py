
print ("BYU-I WebDevelopment")
#Installing VSC. 
#Windows      https://www.youtube.com/watch?v=Epiixq4F1E0
#Mac          Won't OPEN...
##
#VSC set interface preferences.      https://www.youtube.com/watch?v=YPPeNcbZy1o&t=1s
##
#Keyboard Shortcuts   #Windows https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf  #Mac https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf   #Linux https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf
##
#FILE MANAGEMENT   and how we can start a web project's file structure using VSC.
#Create a folder (class is wdd130) with the structure of your about me project inside of it.  # https://www.youtube.com/watch?v=kuKCW6wxVoc&t=3s
#Image folder (images)     #Scripts (Javascript)     #Styles (CSS)       #index.html (for...html)
## TIP ## 
#When naming folders and files: all lowercase, no caps, no spaces

#Creating HTML page and installing VSCode extentions.
#  https://www.youtube.com/watch?v=Ae7npVLX938

#go to the index.html folder. type in "!" Then hit tab or Enter. It will give you the starting of a web page. (on index.html)
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
"""

#Note the Source control tab on the left of VSC... use that to get github pages where we will be hosting our web files
#Go to the extentions and install "live server" by Ritwick Dey and "beautify"
#rightclick on index.html file and choose "open with live server". That'll open up a window where you can see your changes being made live.

"""
Become familiar with VSCode
If you'd like to explore the VSCode environment in more detail, visit the Microsoft documentation on VSCode at docs.microsoft.com
https://docs.microsoft.com/en-us/visualstudio/get-started/visual-studio-ide?view=vs-2022
# One nice feature is to turn on the word-wrap feature by selecting the View menu option and checking the Word Wrap' checkbox.
# Other Software
Here is a list of other software we will use this semester. These are all web-based and require no installation. Your instructor will give you more details when it is time to use them:
Wireframe.cc Lightweight online tool for creating wireframes, or
Coolors.co    A color theme chooser
"""
# https://wireframe.cc/ 
# https://coolors.co/

print ("Week 01   HTML") #Getting Started
 #Class name WDD-130
 #This class serves as an introduction to web design and development.
 #The course is designed to introduce students to the basics of web technology and web design and development principles.
 #The course uses hands-on activities with students actually participating in simple web design projects and programming.
 #It is anticipated that students who complete this course will understand the fields of web design and development and will have a good idea of whether or not they want to pursue web design and development as a career.
##Over the course of this class, you will create two websites as you learn HTML and CSS.
 #The first website is for a  fictional whitewater rafting company.
 #The second website is your personal site.
 #Most of the homework activities and assignments are actually smaller parts of the creation of these two websites. 
 #The flow of the creation of the sites will be planning, layout, and build.  
##Seek help early and often in this course. Later, activities build on earlier ones so don't let yourself get stuck!
"""Overview
Tasks: Install a coding editor where we will code our HTML and CSS and create a simple HTML file
Purpose: This week we will be introduced to HTML and learn about the elements and a brief introduction to CSS.
Objectives
Become familiar with the code editor we will be using this semester.
Introduce yourself by creating a basic HTML document.
Become familiar with the basic vocabulary of the web and HTML."""
 #[Notes]
 #You will be reading or watching videos to prepare for each week. 
 # Usually, you will watch or read the preparation materials and take the preparation quiz before the first class of the week.
 # Then you will have assignments to compete during the week inside and outside of class. 
 # Remember, because this is a two-credit course, you will spend approximately 4-6 hours per week on homework. 
 # Do not plan for any less. The most important thing to remember is to pace yourself. 
 # Set aside time throughout the week to complete your assignments.

 #Seek help early and often in this course. Later activities build on earlier ones...don't let yourself get stuck!
print ("preparation materials")
#  https://www.youtube.com/watch?v=HTsJbDw13tI&t=2s     The internet and web development basics/vocab
#  https://www.youtube.com/watch?v=jxYtjiuPfLQ&t=1s      "What is HTML?"
#  https://www.youtube.com/watch?v=GpZmiD8WlFo           "More HTML elements"
#  https://www.youtube.com/watch?v=CDQobxknrlE&t=1s      "What is CSS?"

# HTML and CSS are "front end languages."
#php and python are "back-end languages."

#opening and closing tags. closing tabs usually have / in them
#html tag has all the other tags between its opening and closing tag.
#body tag contains all the tags that will display in the page of the browser.
#text between the h1 tags or heading level 1 tag is the MAIN heading.
#h2 tags are one level down from the main heading. used often as subheadings. 
#text between the p tags is the paragraph text.
##HTML = Hyper Text Markup Language
"simple HTML framework= "
#!DOCTYPE html>
#<html>
# <head>
#    <title>Page Title</title>
# </head>
# <body>
#       
# </body>
#</html>
"Page Title" #where the tab at top of browser...
#between body will be what's displayed.

##MORE HTML elements.
#between the body segment.
#header = Logo, menu are things that would belong in the header.
  #nav = navigation. used to hold the menu. defines a set of navigation links.
    #<a href=""></a>      "<a> elements"
    #<a> elements defines a hyperlink
    #if a user clicks on text/content between the a tags, it will take them somewhere else.
    ###"Additional information is needed inside the opening tag to specify where to send the user once they click the content of the <a> element. 
      #Additional information inside an opening tag is called an attribute. Attributes usually come in name/value pairs, with the name followed 
      #by an equal sign and then the value in quotes. This is an attribute with the name of href and the value in quotes of the URL or web address
      #of where the link will take the user. Href stands for hypertext reference. Notice that tags and attribute names are lowercase. 
      # HTML is not case sensitive but it’s good practice to leave them lowercase. These <a> elements are nested inside the <nav> 
      # element and so they are the children of the <nav>"
    #
#main = hold webpage content that is unique to each page of the website.
  #img = image element...
  ###one, of only a few elements, that doesn’t have an open and closing tag. That’s because there is no content that is needed between tags. 
  # All the information to show the image is handled by the attributes. This image element has two attributes the src or source attribute and 
  # the alt or alternative text attribute. The src attribute has the value of the path of where the image is located along with the name of the 
  # image. The alt attribute shows alternative text that will be used by screen readers or if the image is not available. 
  # The name part of the name value pairs are src and alt. The values are in the quotes following the equal sign.
  #EG.
  #<img src="voyager.jpg" alt="docking station">
#footer = hold elements that will show up at the bottom of a website. eg. copyright or content info. "follow, contact, help"

#meta tags we'll learn later.
#lang=language.
"Semantic" #semantic tags describe the content added to the page.
#<h1> main heading
#<a> links
#<img> display images. 
#HTML handles the structure of the page, and CSS handles how it looks/how it is presented.
"""What is CSS"""
#all about presentation. 
#  csszengarden.com
#see examples...
#
#Cascading
#Style
#Sheets
#done in the styles file.

print ("Understanding HTML")
#HTML stands for hypertext markup language. 
# Hypertext refers to the way we can place hypertext links in our document that allows our users to move from one page to another.
# Markup is a set of symbols or codes for displaying content on the Internet. 
# HTML tells web browsers the structure of a web page's words and images.
#This markup language allows you to code around the content, the browser will use this code to display or render our page correctly. 
# The code or tags we use are the markup.
#Let's copy the following code into an html file.
"""
<!DOCTYPE html>
<html>
  <head>
    <title>BYUI</title>
  </head>
  <body>
    <header></header>
    <main></main>
    <footer></footer>
  </body>
</html>"""
# This is the framework of a beginning HTML page. 
# Notice inside the body tag we have 3 general areas. 
# The body tag has 3 children tags of header, main and footer. 
# Let's start with the header. 
# Let's type in a common element you'd find in the header a nav element.
"""
<header>
  <nav></nav>
</header>"""
#The nav element will contain menu links. 
# These links are created with an a tag.
"""
<nav>
  <a>Church of Jesus Christ</a>
  <a>Temples</a>
  <a>Scriptures</a>
</nav>"""
# If we look at our rendered page now in a browser window, the content of the a tag shows but they are not links. 
# When we click on the content text, nothing happens. 
# We have to add an attribute to the opening a tag that shows where to take the user when they click on the content. 
# Let's also add a Home page link and then add attributes to each opening tag as follows.
"""
<a href="byui.html">Home</a>
<a href="https://www.churchofjesuschrist.org">Church of Jesus Christ</a>
<a href="https://www.churchofjesuschrist.org/temples">Temples</a>
<a href="https://www.churchofjesuschrist.org/study/scriptures">Scriptures</a>
"""
# Now when you look at the rendered page in the browser you can click the text content and it will take you to the right place 
# because we added the href or hypertext reference value for each a link.
##NOTE: Note that the links here are not going to internal website pages but to external website pages. 
# Your navigation link would usually be going to other pages in your website not to outside web pages like this.

#Eg. Cont.
#Let's move on to the main part of our web page with a header level one title for our page using an h1 tag. 
# Then let's add an img tag. There are two attributes needed for an image. 
# First where is the image located or what is the source (src) and, second what is some alternative text (alt) that can be used if 
# the image can't be seen. Then add a paragraph beneath the title using a p tag.
"""
<main>
  <h1>Brigham Young University Idaho</h1>
  <img
    src="https://www.byui.edu/images/service-sites/map-banner.jpg"
    alt="BYUI Campus"
  />
  <p>BYU-Idaho is a comfortable place to learn and grow as a disciple of Jesus Christ because students, faculty, and employees share a commitment to live the gospel.</p>
  </main>"""
#Again, we are using an attribute value for the src property that is taking us to an image that is located externally to our site. Normally you would want to use an internal path to your own images folder where your website images are located. Something like src="images/map-banner.jpg" This would assume that you have a folder called images with a jpg image called 'map-banner.jpg' located in that images folder of your site. But for ease of this prepare practice we will use the external image.

#Lastly, let's add a p tag to our footer with a bit of information for the bottom of our page.
"""
<footer>
  <p>My Web Page 20XX ©</p>
</footer>"""
#The &copy; will create an HTML symbol copyright entity for us. See HTML Symbols for more examples.
##      https://www.w3schools.com/html/html_symbols.asp    
#There we have our first simple HTML page. 
# If we had multiple page that we created for the same website, the header and footer section would remain the same for every page 
#of our website and the main section would change from page to page of our website.
#We've practiced with some of the elements that make up the structure of a simple web page.
# And we see that some elements need attributes within their opening tags to display and function properly.



print ("Week 02   CSS & Siteplan")
#We could create webpages with any simple text code editor.
#eg. notepad     open with command+o Crl+o

#get web pages on internet.
#Through "hosting"
#pay hosing company
#purchase hardware
#domain name.  eg. amazon. google. etc.
#DNS domain name system
#GostGeter, Google cloud, amazon web services
#glitch or github are hosting companies for free.

#comments on HTML and CSS.
#  <!-- comment text here -->     (HTML)
#and
#  /*  comment text here   */     (CSS)   * is called "asterix"

#CSS syntax & inheritance. 
#eg. values. 

#fonts.
#web safe fonts. fonts recognized by any brower. 
#eg. sanserif, serif, monospace, cursive, fancy
#Some like Comic Sans are way overused and should be AVOIDED.
#googlefonts or font squirrel.
#@import url('')
#TTF    true type font.
#@font-face   css rule
#add import from gFonts and @font-face rules shouold ALWAYS be at the top of CSSfile B4other styles
#try to not go over 2 different font types.

#COLORs
#color names
#Hexadecimal codes
"""
  #000000 Black
  #FFFFFF White
  #FF0000 Red
  #00FF00 Green
  #0000FF Blue
  #FFFF00 Yellow """
  # included.
#RGB values.
  #black 0,0,0
  #white 255,255,255
  #red 255,0,0
  #green 0,255,0
  #blue 0,0,255
  #yellow 255,255,0
#you can add alpha values to rgb which specifies opacity
#example red = rgba(255,0,0,0.2)
#values 0.0 invisible
#1.0 complete opacity.
print ("Understanding CSS")
#CSS stands for cascading style sheets. used to layout and style web pages.
"""
<!DOCTYPE html>
<html>
  <head>
    <title>BYUI</title>
  </head>
  <body>
    <header>
      <nav>
        <a href="byui.html">Home</a>
        <a href="https://www.churchofjesuschrist.org">Church of Jesus Christ</a>
        <a href="https://www.churchofjesuschrist.org/temples">Temples</a>
        <a href="https://www.churchofjesuschrist.org/study/scriptures">Scriptures</a>
      </nav>
    </header>
    <main>
      <h1>Brigham Young University Idaho</h1>
      <img src="https://www.byui.edu/images/service-sites/map-banner.jpg" alt="BYUI Campus" />
      <p>
        BYU-Idaho is a comfortable place to learn and grow as a disciple of
        Jesus Christ because students, faculty, and employees share a commitment
        to live the gospel.
      </p>
    </main>
    <footer>
      <p>My First Web Page 20XX &copy</p>
    </footer>
  </body>
</html>   
"""
#Right now, any styling on this page is from browser default CSS styles.
#For example the h1 element is styled as bigger and bolder.
#If we want to add our own styles to this page we will use an external CSS file that will link up to the HTML page.
#We use the link tag inside the HTML to tell which CSS file will be used with that HTML page.
"Inside the head element, let's add the link tag to the HTML page, which will link this HTML page to the CSS file."
"""<head>
  <title>BYUI</title>
  <link rel="stylesheet" href="styles/styles.css" />
</head>
"""
#The link tag has two attributes. The rel specifies the relationship between the current document and the linked document.
#The href or hypertext reference shows where the document is located. It is inside a styles folder and is called styles.css.
## Let's create the folder called styles with a CSS file called styles.css inside that folder.
#The styles folder will be at the same level as our HTML file.
#Open the styles.css and let's add our first rule-set to the CSS file:
"""
body {
  text-align: center;
}
"""
#The selector is body and inside the curly braces are all the declarations, or property value pairs, that will affect that selector.
#If we look at our rendered HTML page now in a browser window, all the body and all the children of the body inherited the alignment of center.
#Let's add another CSS declarations.
"""
nav {
  background-color: steelblue;
  padding: 10px;
}
"""
#Now when you look at the rendered page in the browser, you will see the background of the nav changed colors and a little bit of space, or padding, is added all around the links in the nav.
#ut the links are still really close together and they are hard to read because there is not a good contrast between the text color and the background color.
#Let's fix that by adding another declaration.
"""
a {
  color: white;
  margin: 40px;
}
"""
#The color refers to the font color and the margin gives some space between the a elements.
#Let's add the rest of the CSS declarations.
"""
h1 {
  color: steelblue;
}
img {
  width: 800px;
  border: 4px solid steelblue;
}
p {
  padding: 10px;
}
footer {
  background-color: steelblue;
  color: white;
}
"""
#Don't worry if you don't understand some of the units of measurement like px or the % sign.
#We will learn more about units of measurement in a different learning module.
#What we see from this activity is the proper syntax for creating rule sets in our CSS file and how a little CSS styling can make a difference in how our page looks.
"""
<!DOCTYPE html>
<html>
  <head>
    <title>BYUI</title>
    <!-- what the tab will be named. -->
  </head>
  <body>
    <header>
      <nav>
        <a href="byui.html">Home</a>
        <a href="https://www.churchofjesuschrist.org">Church of Jesus Christ</a>
        <a href="https://www.churchofjesuschrist.org/temples">Temples</a>
        <a href="https://www.churchofjesuschrist.org/study/scriptures">Scriptures</a>
        <!-- the above are links and what they will be called on the website -->
      </nav>
    </header>
    <main>
      <h1>TITLE BIG AND BOLDED</h1>
      <!-- self explanatory... -->
      <img src="https://www.byui.edu/images/service-sites/map-banner.jpg" alt="BYUI Campus" />
      <!-- image -->
      <p>
        paragraph eilsjilfsjelsefjsjsfilsdkf.
      </p>
    </main>
    <footer>
      <p>footer text</p>
      <!-- the text at the bottom will go here. -->
    </footer>
  </body>
</html>
"""
print ("Setting up GitHub")
print ("W02: GitHub Pages Hosting Setup " " Background")
#We will continue setting up a way to get our web pages live on the web.
#Last week we learned how to create pages using the Microsoft Visual Studio Code editor.
#Now we will continue by learning how to upload our files to GitHub.
#Then from there they can be seen on GitHub Pages.
#We can then share the website with an instructor or fellow students for collaboration.

#Again, like last week, there are a number steps we will need to go through to get everything set up.
#ou will be installing and setting up Git, GitHub, and GitHub Pages.

#If you aren’t familiar with Git, there is a 'What is Git?’ video you can watch, but basically Git keeps track of your project folder as you make changes to any of the files.
###    https://www.youtube.com/watch?v=FsgEtgmh268
#You can commit to these changes, or decide you want to keep them, and then transfer or push our files to our project that is stored on GitHub servers.
#We will refer to the folder with all our project files as a repository or repo.
#That is a huge simplification of Git and Repositories, but we really aren’t going to go super in depth with versioning control in this beginning level course.
#We are mainly using GitHub Pages because it’s a nice, free way to publish our website so it can be live on the Internet without having to pay for hosting or a domain.
print("Instructions")
#Each list of steps is followed by a video demonstrating the same steps. Carefully follow each step in the order they are presented here.
#01 Sign up for a GitHub Account
#Visit the Github.com website.
###  https://github.com/
#Select the Sign Up button.
#You'll enter an email. Then select Continue.
#Create a password that has to be at least 15 characters or 8 characters with a number and lowercase letter. Then select Continue.
#Enter a username all in lowercase.
 #Use a professional name since this username will show up in the domain of your web projects.
 #You might show these links to future prospective employers.
 #If you get a red 'X' to the left of your username, then someone else has already used that username and you need to choose a different one.
 #Don't forget the email, password, and username you used for this new GitHub account.
 #We will need them later.
#Enter 'n' for the next step unless you want email from them.
#At this point it wants to make sure you are human, so it has you solve a few simple puzzles.
 # Select Start puzzle and follow the directions. Select Create account.
#It will send a launch code to the email you listed. Use that launch code and enter it.
#You can skip any personalization questions by selecting the Skip Personalization link near the bottom.

#The following video demonstrates the steps above.
#The last bit of the video should just show the launch code getting entered.
#You can just keep the account open on your browser while you go on to the next steps in the setup process.
#https://www.youtube.com/watch?v=eMbF5kYqPt0&t=1s

print ("install Git on your computer.")
#Select and follow only the Windows, Mac, or Linux Instructions.
#Windows
##  https://www.youtube.com/watch?v=3KpzB3ZZCZ4&t=1s
""" 
Before downloading, check to make sure you don't already have Git installed on your computer.
Select the Start window icon on your computer in the bottom left of your screen.
Type 'cmd' to open the Command Prompt app. You should get the Command Prompt terminal to open. It doesn't matter what your prompt path is.
Type in
git --version
and select Enter.
###    'git' is not recognized as an internal or external command, operable program or batch file.
    OR YOU MIGHT GET     git version 2.37.3.windows.1
You should now either see a git version number come up or a message that says something about how 'git' is not recognized. If you have a version number come up, you already have Git installed and you don't need to install it. If you get the message that git is not recognized, then you need to install it.

To install Git for Windows. Go to git-scm.com/downloads and select Windows under Downloads. An .exe file should be downloaded.
Select that .exe file to open it and it will begin the process of installing Git.
Allow it to make changes to your device.
Select Next through all of the setup windows leaving all the defaults as they are. There will be quite a few windows.
The last window will let you select Install and select Finish.
Open up a new Command Prompt window by closing the first Command Prompt window and start a new one by typing 'cmd' at the Windows start button in the bottom left of your screen again. At the prompt, type the following:
git --version
again to see that it installed. You should now see the version number. (If you don't use a new Command Prompt window, you could get the same message you had before you installed Git.)
While we are still in the Command Prompt, we will type in two more commands to set up our username and email that are associated with our GitHub account. Again, it doesn't matter what the path prompt is. These are global settings so you can type them from any path prompt.

The command is listed below, but make sure you use your own username and email between the "" quotes. Use the username and your email you used for the GitHub account. It will be different for everyone. Type the following:
git config --global user.name "yourusername"
and then select Enter. Nothing will happen if you did it right. And then type the following:
git config --global user.email "youremail@byui.edu"
and then select Enter again.
If you want to check the global configurations, you can always type
git config --list
and you can see the user.name and user.email should have your new username and email values. Don't worry about all the other configurations.
Now you have configured your Git to recognize your GitHub later."""

#Mac
## https://www.youtube.com/watch?v=kJLYtoj4VpA
""" Before downloading, check to make sure you don't already have Git installed on your computer.
Select the Search icon (it looks like an magnifying glass) on your screen near the top right of your screen.
Type in 'Terminal' and open the Terminal app. It doesn't matter what path our Command Prompt is showing. All the commands we type will work anywhere.
Type in
git --version
at the prompt and select Enter.
You should now either see a git version number come up or a pop up window that says something about 'The git command requires the command line developer tools...'. If you have a version number come up, you already have git installed and you don't need to install it. (But you will want to set your config setting as shown below.) If you get the pop-up message, select Install and Agree.
The installation may take quite a few minutes. You will get a set of development tools, which includes Git.
Type in
git --version
at the prompt and select Enter. You should now see the version number.
While we are still in the Command Prompt, we will type in two more commands (or configuration settings) to set up our username and email that are associated with our GitHub account. Again it doesn't matter what the path prompt is. These are global settings so you can type them from any path prompt.

The command is listed below, but make sure you use your own username and email between the "" quotes. Use the username and your email you used for the GitHub account. It will be different for everyone. Type the following:
git config --global user.name "yourusername"
and then select enter. Nothing will happen if you did it right. And then type the following:
git config --global user.email "youremail@byui.edu"
and then select Enter again.
If you want to check the global configurations, you can always type
git config --list
and you can see the user.name and user.email should have your new username and email values. Don't worry about all the other configurations.
Now you have configured your Git to recognize your GitHub later."""

#For Linux Users
#Linux Git Install
#https://github.com/git-guides/install-git#install-git-on-linux 
#Install Git with the link above and then follow the last few steps from the Windows or Mac instructions to set up your global config username and email settings to match your GitHub account.

#Set up Visual Studio Code with Git and GitHub
#Our wdd130 folder will hold all our files and resources for all our projects and keep track of any changes we make.
#When we are ready, we want to then transfer the local files to our remote GitHub account.

#Before you start, make sure you have the previous step completed with Git installed and your Git config username and email settings done.

#Let's use the folder we set up last week called 'wdd130' to become a repository in GitHub so we can eventually see our website online.

#Remember we already had the 'aboutme' folder within wdd130 that contained our aboutme project.
#We had an index.html file and folder(s). The images folder had an image file in it.

#1. Make sure the wdd130 folder is open in VSCode if it's not already open.
#If you have other folders open in VSCode that use Git make sure you close them.
#You only want the one wdd130 folder open, otherwise you won't see the button you need to see in the next few steps.
#(It may ask if you trust the file source. It's your folder and files so you can trust it.)

#2.Select the Source Control icon in VSCode. (It's the 3rd one from the top on the left.)

#3. Select the blue button that says Publish to GitHub.
#If you don't see this button, make sure you have all other Git repo folders closed.

#4. Select Allow if you get a message saying 'The extension 'GitHub' wants to sign in using GitHub.'
#5. If you are prompted for an authorization for Visual Studio Code to Access GitHub, select Continue.
#6.If you are asked to allow the page to open 'Visual Studio Code', select Allow.
#7.You may also be asked to allow an extension to open this URI, select Open.

#8. VSCode will choose the folder you have open, the wdd130 folder as the the repository and give you the option to 'Publish to GitHub public repository'.
#Choose the one that says 'public', not 'private'.
#This will make a new public repository in our GitHub account.

#9.It will show a list of all the files in the wdd130 folder.
#They will all be selected by default so just click 'OK' to include all files in the new respository.
#10.You may get a prompt to 'Authorize Git Credential Manager' here. Select Authorize.
#11.If you get a message asking if you'd like to periodically run fetch you can say 'Yes', but it's not necessary.
#You can see in your GitHub account (at Github.com) the new repository there and the files there that now mirror the files in the wdd130 folder you have on your computer
#Now we will only have to 'push' any changes or additions to GitHub.
#The following video demonstrates the steps above. I used a Mac computer with this video. Windows computers won't have the .DS_Store file.
#https://www.youtube.com/watch?v=mrGMxZkkIzg
print ("Starting our Home Page")
#Let's start a new index.html page (Home Page) inside our repository. Remember to use all lowercase letters and no spaces in file names.
#1. In VSCode, open the Explorer panel and add a file to the wdd130 folder called index.html.
#This index.html is different from the index.html inside of aboutme.
#It will be the home page of our entire repository (wdd130) folder.
#2. Open the file and start a new HTML document with an exclamation mark '!' and select Enter. This will start a new file for you.
#3. Change the default title text of 'Document' to 'WDD130 Home Page'
#4. Add the following code inside the body:
"""
<h1>Welcome to WDD130 Web Projects</h1>
<nav>
  <a href="aboutme/index.html">About Me Page</a>             
  <a href="wwr/index.html">White Water Rafting Website</a>
  <a href="wwr/site-plan-rafting.html">White Water Rafting Siteplan</a>
  <a href="positioning.html">Positioning Activity</a>
  <a href="#">Personal Website</a>
  <a href="#">Personal Siteplan</a>
</nav>
"""
#5. As you save this file, you will notice another blue circle number show up on our Source Control icon. Our local Git noticed a new file in our repository.
#6. Select the Source Control Icon.
#7. Select the + sign next to Changes.
#8. Now commit the change to our local repository by adding a message to the 'Message' input box that describes what changes we've made. Something like 'Added the home page for wdd130'.
#9. Select the check mark to the right of your repository name.
#10.Now send those changes to the remote repository by selecting the 'More actions' ...
#(3 dots) and choose Push from the pop up menu. This will send the index.html to GitHub.
#11. When you go to your GitHub account, you should now see the index.html file in the repository there.
print("setting up GitHub pages")
#Let's set it up so we can see our GitHub files as live web pages on the Internet. We're almost there. Hang in there.
#1.Let's see this page live on the Internet by setting up GitHub pages. Go back to the GitHub.com account. 
#Click 'Settings' with the gear icon. In the submenu that appears to the left choose 'Pages'
#2. In the Source section, select the button that says None and change it to the 'main' branch, leave the next one at 'root' and select Save.
#Your branch could be named 'master' instead of 'main' and that's fine. You will only have one branch to choose from there.
#3. Above that section, you will get a colored area that says 'Your site is ready to be published at ...'
#with the name of your URL that can be used by anyone to see your website. Woo Hoo! We did it!
#4. Give it a few minutes for your home page to show up. You might need to refresh the page after a few minutes.
###  The following video demonstrates the steps of GitHub Pages:
#     https://www.youtube.com/watch?v=_jzY3dryS5A&t=1s
#NOTE:  You might want to bookmark that new github.io website address so you can easily see your home page each week.
print ("Practice with Pushing all our additions and edits for our project to GitHub")
#Let's add another HTML element to our page to see how we will push our edits and additions of our project to GitHub
#This step is all you will need to do from this point on as you edit and make additions to your projects. All previous steps were just setup.
#1. In VSCode, open the Explorer panel and add a paragraph to the index.html. You can add it below the navigation.
"""
<h1>Welcome to WDD130 Web Projects</h1>
<nav>
  <a href="wwr/index.html">White Water Rafting Website</a>
  <a href="wwr/site-plan-rafting.html">White Water Rafting Siteplan</a>
  <a href="positioning.html">Positioning Activity</a>
  <a href="#">Personal Website</a>
  <a href="#">Personal Siteplan</a>
</nav>  
<p>Your Name Here - WDD130</p>   """
#2. As you save this file, you will notice another blue circle number show up on our Source Control icon. Our local Git noticed the change in our file in our repository.
#3.Select the + sign next to the index.html file.
#4.Now commit the change to our local repository by adding a message to the 'Message' input box that describes what changes we've made. Something like 'Added a paragraph to the home page'.
#5.Select the check mark to the right of your repository name.
#6.Now send those changes to the remote repository by selecting the More actions ... (3 dots) and choose Push from the pop up menu. This will send the index.html to GitHub.
#7.Give it a few minutes to update on GitHub, but when you go to your GitHub Pages URL (web address) you should see the changes to the index.html.
#The following video demonstrates pushing to our GitHub repository from Visual Studio Code:
#    https://www.youtube.com/watch?v=QMBidV_Qo3A&t=1s
#When editing or adding to your files:
#Do NOT make edits or addition to your repository files inside of the GitHub online editor. 
# Always just edit your local files on your computer through the Visual Studio Editor and then 'push' 
# the changes to the online repository.
#See your instructor if you have any trouble.
#We did it! That was a lot of set up but worth it to have free hosting. And from here on out, you just have to commit and push any changes you make in your wdd130 repo from VSCode.
















#Color Theory
#Basics
#Primary
#secondary
#
#Color wheel!
#
#hue
#Another word for "color"
#
#Saturation
#word for intensity
#subtle vs vibrant
#
#Value
#dark or light.
#
#Formula for COLOR HARMONY
#Color schemes...
#Monochromatic: the easiest.
#only uses 1 hue, or color. 
#Guarenteed to match!
#
#Analogous :
#uses colors next to eachother on the color wheel
#reds and oranges. and red orange.
#
#Complementary colors: opposite on the color wheel
#Eg. red and green
#add variety by introducing lighter/darker or desaturated tones.
#
#Split Complementary: 
#Colors on either side of complement.
#eg. red, green-blue, green-yellow
#gives more colors to work with.
#
#Triadic
#3 colors evenly spaced on color wheel.
#tend to be STRIKING! 
#especially with primary/secondary colors.
#BE MINDFUL WHEN USING THESE COLORS!!! 
#
#Tetradic
#Forms a rectangle on the color wheel.
#uses not 1 but 2 complementary color pairs on the color wheel.
#Works best if you let 1 color dominate,while others serve as an accent color
#
#DOs and DONTs when it comes to color.
#colors that seem to VIBRATE when placed next to eachother. 
#Solution, tone it down! 
#
#bright colors have fun/modern vibe
#desaturated appear professional/business-like
#context. 
#
#See advertizing and branding for ideas.
#or you can look at famous art works.
#web resources. 










print ("Week 03   Wireframe to HTML")




#Class and ID Selectors.
#Class attributes are used to give a class name to an HTML element
#Many differ elements can use the same class.
#Id attributes are used to GIVE A UNIQUE ID to an HTML element
#You CANNOT have more than 1 element with the samme ID value in 1 HTML page.
"""
<!DOCTYPE html>
<html>
<head>
    <title>BYUI</title>
    <link rel="stylesheet" href="styles/styles.css">
</head>
<body>
    <header>
        <nav>
            <a href="byui.html">Home</a>
            <a href="https://www.churchofjesuschrist.org">Church of Jesus Christ</a>
            <a href="https://www.churchofjesuschrist.org/temples">Temples</a>
            <a href="https://www.churchofjesuschrist.org/study/scriptures">Scriptures</a>
        </nav>
    </header>
    <main>
        <h1>Brigham Young University Idaho</h1>
        <img src="https://www.byui.edu/images/service-sites/map-banner.jpg">
        <p>BYU-Idaho is a comfortable place to learn and grow as a disciple of Jesus Christ because students, faculty, and employees share a commitment to live the gospel.</p>
    </main>
    <footer>
        <p>My Web Page 20XX &copy</p>
    </footer>
</body>
</html>
  """
#Create a folder at the same level as our HTML file and call it styles.
#Within that folder, let's create a styles.css file. Open that styles.css in the editor.

#Let's change the font size and line-height of the paragraph in the main section of our page, but we don't want it to effect the footer paragraph.
#So we can give our paragraph a class or ID attribute to differentiate it from all other paragraphs on the page.

#<p class='main-para'>BYU-Idaho is a comfortable place to learn and grow as a disciple of Jesus Christ because students, faculty, and employees share a commitment to live the gospel.</p>
##Then in CSS we can target just that class by using a dot selector. Classes are specified with a dot or period before the class name in CSS.
"""
.main-para {
    font-size: 1.5em;
    line-height: 1.5em;
}"""

#Notice that just the paragraph in the main section is bigger and has more line-height. The paragraph in the footer has not changed because only the paragraph in the main section has that class name.
#If we added more paragraphs to our main section of the page, we could give them the exact same class name and they would also have the same larger text and line-height.
print ("Example 2")
#Perhaps we want to show our users which page is the active page in the navigation, or in other words, which is the current page that they are on. 
#We will only ever have one active page at a time. Let's use an ID this time for our home page link.
"""
<nav>
    <a id="active" href="http://index.html">Home</a>
    <a href="https://www.churchofjesuschrist.org">Church of Jesus Christ</a>
    <a href="https://www.churchofjesuschrist.org/temples">Temples</a>
    <a href="https://www.churchofjesuschrist.org/study/scriptures">Scriptures</a>
</nav>"""
#Now we can target that ID in CSS using a hashtag preceding the id value.
#Remember we can't use the id of 'active' anywhere else on the page, but we can use another id with a different value if we needed to.
"""
#active {
    background-color: white;
    color: steelblue;
}"""
#Now our home page link has a different background color and text color to show what page they are on.
#We should not use the same id of 'active' on any other element on this web page.
# 
# 
# ##

print ("Week 04   More CSS")

print ("Week 05   Fonts & Spacing  /  Elevator pitch")

print ("Week 06   Leam Layout")

print ("Week 07   Finish Home Page  /  Start Siteplan")

print ("Week 08   Wire-frames  /  Pages Content")

print ("Week 09   Rafting Complete  /  Complete Siteplan")

print ("Week 10   Forms")

print ("Week 11   Homepage")

print ("Week 12   Subpage 1")

print ("Week 13   Subpage 2")

print ("Week 14   Site & Report Complete")
