fname = input("first: ")
lname = input("last:  ")

fname = fname.strip().capitalize()
lname =lname.strip().capitalize()
print(f"hello {fname:.1s}       {lname}")
print(f"hello {fname.strip()}  {lname}")

# Practical - Email Slice
fname = input("whats your name? ")
email = input("whats your email? ")

the_username = email.index("@")
the_website = email.index("@")+1

username = email[0:the_username]
website = email[the_website:]

print(f"your name is {fname.strip().capitalize()} and the username is {username} and the website is {website}")
#email = "Example22@gmail.com"
#mail = email.index("@")
#print(email[0:mail])