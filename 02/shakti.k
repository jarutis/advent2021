d:+" "\'0:`input
commands:`n$d[0]
val:`h$d[1]

/ Part 1
horizontal:+/val@&commands=`forward
up:+/val@&commands=`up
down:+/val@&commands=`down

horizontal*down-up

/ Part 2
down:+\@[val;&~commands=`down;0]
up:+\@[val;&~commands=`up;0]
aim:down-up

hi:&commands=`forward
depth:+/aim[hi]*val[hi]
depth*+/val[hi]
