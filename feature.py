#Additional feature module
# -------------------------
# instructions::
# copy and paste the first section of the module at the top of your program.
# when pasting has commmenced, remove comments pre. 

# !!-- Make sure to import all files found in repository,

#------------------------first section -----------------------------------------



#x = input( " which function would you like to test? " )


#--------------------------------------------------------------------------------
# MODULAR DEBUGGING FUNCTION 
# allows the individualized testing of a program's different componets.

# After each function in a program, insert the following syntax with "calling string" 
# customized accordingly


#Modular debugging syntax:
# if( x ==  "calling_string" ):
#    function()


 
# additional portion of code seen in the first section of this module 



#--------------------------------------------------------------------------------



def access(x,y):
      return x[y] 


def assign(x,y,val):
    
        x[y] = val
       

# Allows access and assignment to items belonging in a nested list



#---------------------------------------------------------------------------------------------




def command(x):
    import a
    #if y = erase : erase command file- 
    open("a.py", "w").close()
    #erases file for new command.
    object = open("a.py", "w")
    object.write("def a():")
    if type(x) == list:
       for zero in range (len(x)):
         object.write( '\n' + "    " + x[zero])
    else:
         object.write( '\n' + "    " + x)
    object.close()
    reload(a)



  #Description:

# Interprets a command given as a string and runs it via an additional python module.
# The command function may be used to execute a single command or a list containing multiple commands
# within the python interpreter.

# example SYNTAX
#up = ["print 'testing'", "print 'more testing'"]
#command(up)
#a.a()
#

# or 
# command("print ' bonjour, parmi nous? '")
#
