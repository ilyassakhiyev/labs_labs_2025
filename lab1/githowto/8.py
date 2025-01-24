#<html>
#  <body>
#    <h1>Hello, World!</h1>
#  </body>
#</html>



#git add hello.html



#<html>
#  <head>
#  </head>
#  <body>
#    <h1>Hello, World!</h1>
#  </body>
#</html>



#git status

#$ git status
#On branch main
#Changes to be committed:
#  (use "git restore --staged <file>..." to unstage)
#	modified:   hello.html
#
#Changes not staged for commit:
#  (use "git add <file>..." to update what will be committed)
#  (use "git restore <file>..." to discard changes in working directory)
#	modified:   hello.html



#git commit -m "Added standard HTML page tags"
#git status

#$ git commit -m "Added standard HTML page tags"
#[main 46afaff] Added standard HTML page tags
# 1 file changed, 5 insertions(+), 1 deletion(-)
#$ git status
#On branch main
#Changes not staged for commit:
#  (use "git add <file>..." to update what will be committed)
#  (use "git restore <file>..." to discard changes in working directory)
#	modified:   hello.html
#
#no changes added to commit (use "git add" and/or "git commit -a")



#git add .
#git status

#$ git add .
#$ git status
#On branch main
#Changes to be committed:
#  (use "git restore --staged <file>..." to unstage)
#	modified:   hello.html



#git commit -m "Added HTML header"

#$ git commit -m "Added HTML header"
#[main b7614c1] Added HTML header
# 1 file changed, 2 insertions(+)