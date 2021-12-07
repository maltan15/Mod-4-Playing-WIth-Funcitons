#!/usr/bin/env python
# coding: utf-8

# # Assignment: Playing with Functions
# 
# ## Instructions
# 
# This is the template file for the assignment of Module 4 called "Playing with Functions." Please carefully follow the instructions below.
# 
# 1. Rename this file by filling out your surname and first name in the file name. For example, if your surname is Ilagan and if your first name is Joben, then rename the file to ILAGAN-JOBEN-playingWithFunctions.ipynb.
# 2. Fill out the markdown cell just above `Problem 1` with your student details as indicated.  
# 3. To submit this file, first, upload your file to your GitHub repository and, second, submit your repository link to the assignment on Canvas.
# 

# ## Student Details
# 
# ID Number: 204957
# Surname: Tan
# Year and Course: 2 BS ITE

# ## Problem 1
# ## Factorial (1 point)
# 
# The **factorial** of a number is the product of that number and all the numbers below it. For example, 5 factorial (denoted 5! in math) is 5 * 4 * 3 * 2 * 1, which is 120.  
# 
# **Write a function called `problem_1` that takes one positional argument `number`. The function should return  the factorial of `number` as an integer.**
# 
# Example input/output:  
# `problem_1(5)` => `120`  
# `problem_1(10)` => `3628800`  

# In[2]:


def problem_1(number):
    if number < 0:
        return 0
    elif number == 0 or number == 1:
        return 1
    else:
        factorial = 1
        while(number > 1):
            factorial *= number
            number -= 1
        return factorial


# In[4]:


problem_1 (10)


# ## Problem 2
# ## Guessing Game (2 points) 
# 
# Recall that we use `input()` to ask for user input.  
# 
# **Write a function called `problem_2` that takes one positional argument `passphrase`. The function should ask the user to enter the passphrase with `input()`. If the user enters the correct passphrase, the function should return the integer `1`. If the user enters the wrong passphrase, the function should keep asking them for the passphrase. If the user gets the passphrase wrong 3 times, the function should return the integer `0`.**  
# 
# Example input/output:  
# 
# Function input:  
# `problem_2("chums")`  
# Simulated user input:  
# `joben`  
# `chums`  
# Output:  
# `1`  
# 
# Function input:  
# `problem_2("annika")`  
# Simulated user input:  
# `joe`  
# `earl`  
# `niks`  
# Output:  
# `0`

# In[12]:


def problem_2(passphrase):

    for x in range(3):
      guess = input("passphrase: ")
      if(guess == passphrase):
        return(1)

      elif(guess != passphrase):
            None

    return(0)


# In[14]:


problem_2("annika")


# ## Problem 3
# ## Temperature Converter (3 points)
# 
# A common beginner's exercise is to write a function that can convert a temperature value from one format, such as Fahrenheit, to another, such as Celsius.  
# 
# In this problem, extend this idea to convert temperatures freely to and from any of the following formats: Celsius, Fahrenheit, and Kelvin.  
# 
# **Write a function called `problem_3` that takes three positional arguments: (float) `temp`, (string) `original_format`, (string) `new_format`. The function should convert `temp`, which is represented in `original_format`, to its equivalent value in the `new_format.`**  
# 
# Example input/output:  
# `problem_3(0.0, "Celsius", "Fahrenheit")` => `32.0`  
# `problem_3(500.0, "Kelvin", "Fahrenheit")` => `440.33`  
# `problem_3(273.0, "Kelvin", "Celsius")` => `0.0`  
# 
# For your convenience:  
# 1. The accuracy of your float outputs will only be evaluated to within 4 decimal places. 

# In[7]:


def problem_3(temp, original_format, new_format):

    if original_format == "Celsius" and new_format == "Fahrenheit":
        new_temp = (temp * 1.8) + 32 

    elif original_format == "Celsius" and new_format == "Kelvin":
        new_temp = (temp + 273.15)

    elif original_format == "Fahrenheit" and new_format == "Celsius":
        new_temp = (temp - 32) * 5/9

    elif original_format == "Fahrenheit" and new_format == "Kelvin":
        new_temp = ((temp - 32) * 5/9) + 273.15

    elif original_format == "Kelvin" and new_format == "Celsius":
        new_temp = (temp - 273.15)

    else:
        new_temp = ((temp - 273.15) * 9/5) + 32

    new_temp = "{:.4f}".format(new_temp)

    return new_temp


# In[11]:


problem_3 (0, "Celsius", "Fahrenheit")


# ## Problem 4
# ## Exact Change (4 points)
# 
# Part of a cashier's job is to give exact change to customers. It can be difficult to mentally tally how many coins of each type (i.e., 1 peso, 25 centavos, 10 centavos, etc.) to give to a customer.  
# 
# **Write a function called `problem_4` that takes 1 positional argument `amount` in centavos. The function should return a string that describes the appropriate amounts of each type of coin to give to the customer. The string should be formatted as follows:**  
# 
# `"1P:{num}/25C:{num}/10C:{num}/5C:{num}/1C:{num}"`  
# 
# **Use the fewest number of total coins possible.**  
# 
# Example input/output:  
# `problem_4(105)` => `"1P:1/25C:0/10C:0/5C:1/1C:0"`  
# `problem_4(69)` => `"1P:0/25C:2/10C:1/5C:1/1C:4"`  

# In[15]:


def problem_4(amount):

  num_p = 0
  num_25 = 0
  num_10 = 0
  num_5 = 0
  num_1 = 0

  if amount <= 0:

    print('no change')

  else:

    num_p = amount // 100

    amount %= 100

    num_25 = amount // 25

    amount %= 25

    num_10 = amount // 10

    amount %= 10

    num_5 = amount // 5

    amount %= 5

    num_1 = amount

    print ("1P:{0}/25C:{1}/10C:{2}/5C:{3}/1C:{4}".format(num_p, num_25, num_10, num_5, num_1))


# In[16]:


problem_4(105)


# ## Problem 5
# ## Invert Capitalization (3 points)  
# 
# **Write a function called `problem_5` that takes 1 positional argument (string) `message`. The function should return a string whose uppercase letters are now lowercase and whose lowercase letters are now uppercase. Spaces should be left alone.**  
# 
# Example input/output:  
# `problem_5("Test Me")` => `"tEST mE"`  
# `problem_5("asSiGnmENt")` => `"ASsIgNMenT"`  
# 
# For your convenience:  
# 1. The message will only ever consist of spaces, lowercase letters, and uppercase letters.  
# 
# Hint: Research on `ord()` and `chr()`.  

# In[17]:


def problem_5(message):
    new_message = ''
    for i in message:
        if ord(i) >= 65 and ord(i) <= 90:
            i = chr(ord(i)+32)
        elif ord(i) == 32:
            None
        else:
            i = chr(ord(i)-32)
        new_message = new_message + i

    return(new_message)


# In[18]:


problem_5("Test Me")

