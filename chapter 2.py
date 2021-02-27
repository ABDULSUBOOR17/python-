#!/usr/bin/env python
# coding: utf-8

# # CHAPTER 2 

# 2-1. Simple Message: Store a message in a variable, and then print that
# message.
# 

# In[2]:


message = "Welcome to python"
print(message)


# 2-2. Simple Messages: Store a message in a variable, and print that message. Then change the value of your variable to a new message, and print the new message.
# 

# In[5]:


message = "Welcome to python"
print(message)
message = "Happhy Learning"
print(message)


# 2-3. Personal Message: Store a person’s name in a variable, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

# In[7]:


name = "ABDUL"
print(f"Hello {name}, would you like to learn some Python today?")


# 2-4. Name Cases: Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase.

# In[9]:


name = "Abdul"
print(name.lower())
print(name.upper())
print(name.title())


# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks:
# Albert Einstein once said, “A person who never made a mistake never tried anything new.”

# In[10]:


qoute = "“A person who never made a mistake never tried anything new.”"
print(f"Albert Einstein once said, {qoute}")


# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time store the famous person’s name in a variable called famous_person. Then compose your message and store it in a new variable called message. Print your message.

# In[11]:


famous_person = "Albert Einstein"
message = f"{famous_person} once said “A person who never made a mistake never tried anything new.”"
print(message)


# 2-7. Stripping Names: Store a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once. Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

# In[13]:


name = "  \tsuboor  \n "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())


# 2-8. Number Eight: Write addition, subtraction, multiplication, and division operations that each result in the number 8. Be sure to enclose your operations in print statements to see the results. You should create four lines that look like this:
# print(5 + 3)
# 
# 

# In[14]:


print(4 + 4)
print(18 - 10)
print(2 * 4)
print(40 // 5)

2-9. Favorite Number: Store your favorite number in a variable. Then, using that variable, create a message that reveals your favorite number. Print that message.
# In[15]:


fav_num = 8
print(f"My favorite number is {fav_num}")

2-10. Adding Comments: Choose two of the programs you’ve written, and add at least one comment to each. If you don’t have anything specific to write because your programs are too simple at this point, just add your name and the current date at the top of each program file. Then write one sentence describing what the program does.
# In[17]:


print(4 + 4) # addition
print(18 - 10) # substraction
print(2 * 4) # multiplcation
print(40 // 5) # integer division

name = "  \tSuboor  \n "
print(name)
print(name.lstrip()) # remove spaces from left
print(name.rstrip()) # remove spaces from right
print(name.strip()) # remove spaces from lef tand right

2-11. Zen of Python: Enter import this into a Python terminal session and skim
through the additional principles.
# In[18]:


import this


# In[ ]:




