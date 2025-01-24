#git switch main



#<html>
#  <head>
#  </head>
#  <body>
#    <h1>Hello, World!</h1>
#    <!-- This is a bad comment. We want to revert it. -->
#  </body>
#</html>



#git status

#$ git status
#On branch main
#Changes not staged for commit:
#  (use "git add <file>..." to update what will be committed)
#  (use "git restore <file>..." to discard changes in working directory)
#	modified:   hello.html
#
#no changes added to commit (use "git add" and/or "git commit -a")



#git restore hello.html
#git status
#cat hello.html

#$ git restore hello.html
#$ git status
#On branch main
#nothing to commit, working tree clean
#$ cat hello.html
#<html>
#  <head>
#  </head>
#  <body>
#    <h1>Hello, World!</h1>
#  </body>
#</html>