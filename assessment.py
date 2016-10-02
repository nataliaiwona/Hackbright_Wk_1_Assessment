# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 

def calculate_cost(state_abbr, cost, tax = .05):
    """This function will calculate an item cost by adding tax. It takes three 
    parameters: tax (default to 5%), state abbreviation and cost. The function 
    will return the cost of the item including tax. If the state is CA, 
    the function will apply a 7% tax rate."""
    
    upper_state_abbr = state_abbr.upper()
    ca_tax = .07

    total_cost = cost + cost * tax
    ca_total_cost = cost + cost * ca_tax
   
    if upper_state_abbr == "CA":
        return ca_total_cost
    else:
        return total_cost

#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

def is_berry(fruit_name):
    """This function takes a fruit name as a string and returns a boolean if 
    the fruit is a 'strawberry', 'cherry' , or 'blackberry'""" 
    
    lower_fruit_name = fruit_name.lower()
    return lower_fruit_name == "strawberry" or lower_fruit_name == "cherry" or lower_fruit_name == "blackberry" 

def shipping_cost(fruit_name_string):
    """This function calculates the shipping cost by taking a fruit name 
    as a string and calling the 'is_berry()' function within itself. 
    It returns '0' if 'is_berry' is True and '5' if 'is_berry' is False."""

    if is_berry(fruit_name_string) == True:
        return '0'
    else:
        return '5'


# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#
def is_hometown(town_name):
    """This function takes a name of a town as a string and evaluates to True 
    if it is my hometown, and False otherwise."""

    grammatical_town_name = town_name[0].upper() + town_name[1:]
    return grammatical_town_name == "Chicago"


#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.

def full_name(first_name, last_name):
    """This function takes a first and last name as arguments as strings and 
    returns the concatenation fo the two names in one string."""

    return first_name + " " + last_name


#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.

def hometown_greeting(home_town_name, frst_name, lst_name):
    """This function takes the string arguments hometown, first name, 
    and last name. Calling both 'is_hometown()' and 'full_name()' functions, this
    function will print 'Hi, 'full name here', we're from the same place!', or 
    'Hi, 'full name here', where are you from?', depending on what 
    'is_hometown()' evaluates to."""

    full_name_here = full_name(frst_name, lst_name)

    if is_hometown(home_town_name):
        print "Hi, {}, we're from the same place!".format(full_name_here)
    else:
        print "Hi, {}, where are you from?".format(full_name_here)


#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

def increment(x = 1):
    """This function has a nested function. The outer function takes 'x', an 
    integer that defaults to 1. The inner function takes in 'y' and 
    adds 'x' and 'y' together.""" 

    def add(y):
        return x + y
    return add


# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20.

addfive = increment(x = 5) #This is called a closure?
addfive(5)
addfive(20)



# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

def append_num_list(num, num_list):
    """This function takes in a number and a list of numbers. It will append 
    the number to the list of numbers and return the list. """

    num_list.append(num)
    return num_list

# I spent 30 minutes on this, and I figured it out, but...
# Originally, I had:
#
# def append_num_list(num, num_list):
#     
#     return num_list.append(num)
#
# Why doesn't .append() return anything? (It returns "NoneType" in the console and
# "None" when I tried to print). 
#
# I see now that returning the original num_list is what returns the 
# appended list, but I'm not sure I understand why. The ID of num_list is 
# the same after appending, and I recall dicussing the memory involved in this.
# 
# So, two questions: 1) Why doesn't .append() return the new list aka why is it a None Type.
# 2) What are the mechanics of new_list returning the new, appended list?? Is it
# just Python saying, "Oh, I knew you needed more than this many bits of and it 
# wasn't an issue for me to add that number to the same spot in memory associated with 
# the new_list variable."



#####################################################################