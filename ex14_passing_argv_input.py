from sys import argv

script, user_name=argv
prompt='>'

print("Hi %s, I'm the %s script." %(user_name,script))

print("I'd like to ask to a few question.")

print("Do you like me %s?" %user_name)
likes=input(prompt)

print("Where do you live %s"%user_name)
lives=input(prompt)

print("what kind of ocomputer do you have")
computer=input(prompt)

print ("""Alright, so you said %r about linking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice. """ %(likes, lives,computer))
