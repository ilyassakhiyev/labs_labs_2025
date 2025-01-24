#git tag v1
#git log

#$ git tag v1
#$ git log
#b7614c1 2023-11-28 | Added HTML header (HEAD -> main, tag: v1) [Alexander Shvets]
#46afaff 2023-11-28 | Added standard HTML page tags [Alexander Shvets]
#78433de 2023-11-28 | Added h1 tag [Alexander Shvets]
#5836970 2023-11-28 | Initial commit [Alexander Shvets]



#git checkout v1^
#cat hello.html

#$ git checkout v1^
#Note: switching to 'v1^'.
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
#HEAD is now at 46afaff Added standard HTML page tags
#$ cat hello.html
#<html>
#  <body>
#    <h1>Hello, World!</h1>
#  </body>
#</html>



#git tag v1-beta
#git log

#$ git tag v1-beta
#$ git log
#46afaff 2023-11-28 | Added standard HTML page tags (HEAD, tag: v1-beta) [Alexander Shvets]
#78433de 2023-11-28 | Added h1 tag [Alexander Shvets]
#5836970 2023-11-28 | Initial commit [Alexander Shvets]



#git checkout v1
#git checkout v1-beta

#$ git checkout v1
#Previous HEAD position was 46afaff Added standard HTML page tags
#HEAD is now at b7614c1 Added HTML header
#$ git checkout v1-beta
#Previous HEAD position was b7614c1 Added HTML header
#HEAD is now at 46afaff Added standard HTML page tags



#git tag

#$ git tag
#v1
#v1-beta



#git log main --all

#$ git log main --all
#b7614c1 2023-11-28 | Added HTML header (tag: v1, main) [Alexander Shvets]
#46afaff 2023-11-28 | Added standard HTML page tags (HEAD, tag: v1-beta) [Alexander Shvets]
#78433de 2023-11-28 | Added h1 tag [Alexander Shvets]
#5836970 2023-11-28 | Initial commit [Alexander Shvets]