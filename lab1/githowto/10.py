#git log

#$ git log
#b7614c1 2023-11-28 | Added HTML header (HEAD -> main) [Alexander Shvets]
#46afaff 2023-11-28 | Added standard HTML page tags [Alexander Shvets]
#78433de 2023-11-28 | Added h1 tag [Alexander Shvets]
#5836970 2023-11-28 | Initial commit [Alexander Shvets]



#git checkout <hash>
#cat hello.html

#$ git checkout 5836970
#Note: switching to '5836970'.
#
#You are in 'detached HEAD' state. You can look around, make experimental
#changes and commit them, and you can discard any commits you make in this
#state without impacting any branches by switching back to a branch.
#
#If you want to create a new branch to retain commits you create, you may
#do so (now or later) by using -c with the switch command. Example:
#
#  git switch -c <new-branch-name>
#
#Or undo this operation with:
#
#  git switch -
#
#Turn off this advice by setting config variable advice.detachedHead to false
#
#HEAD is now at 5836970 Initial commit
#$ cat hello.html
#Hello, World!



#git switch main
#cat hello.html

#$ git switch main
#Previous HEAD position was 5836970 Initial commit
#Switched to branch 'main'
#$ cat hello.html
#<html>
#  <head>
#  </head>
#  <body>
#    <h1>Hello, World!</h1>
#  </body>
#</html>