/ Data
/input:" "\"00100 11110 10110 10111 10101 01111 00111 11100 10000 11001 00010 01010"
input:0:`input

/ Part 1
d:{`b$'x}'input
gamma:(0.5*#d)>+/d
epsilon:~gamma

(2/epsilon)*2/gamma

/ Part 2

f:{$[1<#x;x@&(x@\:y)=~(0.5*#x)>+/x@\:y;x]}
g:{$[1<#x;x@&(x@\:y)=(0.5*#x)>+/x@\:y;x]}

(2/*d f/!#*d)*2/*d g/!#*d
