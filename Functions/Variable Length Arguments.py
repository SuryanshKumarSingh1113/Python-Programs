                                                    # Variable Length Arguments

# *args
# Used to pass multiple positional arguments.

def total(*args):
    print(args)
 
total(1, 2, 3, 4)

# **kwargs
# Used to pass multiple keyword arguments.

def user_details(**kwargs):
    print(kwargs)
 
user_details(name="Harry", age=25)

