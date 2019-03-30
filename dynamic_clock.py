#-----------------------------------Program innformation-----------------------------------------------
#Program name: dynamic_clock.py
#last modifyied: 3/24/19
#
#
#


#-------------------------program resources--------------------------------------------------------------------


def access(x,y):
      return x[y] 


def assign(x,y,val):
    
        x[y] = val
       


#used to access and assign specific items found in nested list. to indicate access, pass the string "-o-" in the arguement val. if val is equal to anything other than "-o-"
# the value occupying the position refered to by x and y will be assigned to val.


#used to access and assign specific items found in nested list. to indicate access, pass the string "-o-" in the arguement val. if val is equal to anything other than "-o-"
# the value occupying the position refered to by x and y will be assigned to val.
#x = raw_input( " which function would you like to test? " )
x = raw_input("enter the function you would like to test")
options = input("please enter a desired animation speed( in terms of seconds per frame for this instance of dynamic_clock.py - if unsure enter the number five.")    




#Allows for dubugging of individual program sections --
#Syntax:
# if( x ==  "string" ):
#    function()





def nest(func):
    
    para_amount = input("how many parameters would you like to test?")
    values = [None]*para_amount
    for zero in range (para_amount):
        print "please enter a value for parameter" + str(zero) 
        values[zero] = raw_input() 
        print values[zero] 
    if para_amount == 1:
       if(raw_input("would you like input to be looped? - y/n") == "y"):
          for zero in range (int(raw_input("How many times?"))):
              func(values[0])
    if para_amount == 2:
       if(raw_input("would you like input to be looped? - y/n") == "y"):
         for zero in range (int(raw_input("How many times?"))):
             func(values[0], values[1])
    
    if para_amount == 3:
       if(raw_input("would you like input to be looped? - y/n") == "y"):
         for zero in range (int(raw_input("How many times?"))):
             func(values[0], values[1],values[2])
    
    if para_amount == 4:
       if(raw_input("would you like input to be looped? - y/n") == "y"):
         for zero in range (int(raw_input("How many times?"))):
             func(values[0], values[1],values[2],values[3])




#-------------------------------Animation textures//other resources--------------------------------------------------------------
import datetime
import random
import random
import time 
# syntax ==  time = datetime.datetime.now()
# prints time in YYYY-MM-DD HH:MM:SS:MD
# additional syntax = print(str(time))

zero = 0
p = [0]
#instaid of tracking down the position of each and individual character, compare with counted heirarchy. -- at least with palm trees and maybe houses that is.
animated = []

#animation definitions, tree #1            

animated.append(" ")
animated.append(" ")
animated.append(" ")
animated.append(" ")
animated.append(" ")
animated.append(" ")
animated.append("                           -")
animated.append("                              _  -")
animated.append("                               \|")
animated.append("                             -   - -")
animated.append("                               /  \ ")
animated.append("                                 |")  
animated.append("                                /")
animated.append("                               /")
animated.append("______________________________|____________________________________________")
# tree #2 
animated.append(" ")
animated.append(" ")
animated.append(" ")
animated.append(" ")        
animated.append(" ")
animated.append(" ")
animated.append(" ")         
animated.append(" ")        
animated.append("                              \| ")
animated.append("                             -   -")
animated.append("                             /  \ ")
animated.append("                              /")
animated.append("                             /")
animated.append("                             \\")
animated.append("______________________________|________________________________________________")
#tree # 3

animated.append(" ")         
animated.append(" ") 
animated.append(" ")         
animated.append(" ")
animated.append(" ")
animated.append(" ")
animated.append(" ")
animated.append("                        _  ")
animated.append("                          \| ")
animated.append("                         -   -  ")
animated.append("                          /  \ ")
animated.append("                            {")
animated.append("                            | ")
animated.append("                             \\")
animated.append("______________________________|________________________________________________")
#tree #4
 
animated.append(" ")
animated.append(" ") 
animated.append(" ")
animated.append(" ")
animated.append(" ")
animated.append(" ")
animated.append("                      -  ")                        
animated.append("                       -")
animated.append("                        \ | ")
animated.append("                      - _   -")
animated.append("                         /  \ ")
animated.append("                           \\")
animated.append("                            \ ")
animated.append("                             \\")
animated.append("______________________________|_______________________________________________")

# Bottom walkway
        
animated.append(" ")
animated.append(" ")
animated.append("  ")
animated.append(" ")
animated.append("  ")
animated.append("                                                        ^      ^ ")
animated.append("                                                       / \    / \   ")           
animated.append("                                                           ^ ")
animated.append("                                                          / \  ")
animated.append("  ")
animated.append("  ")
animated.append("  ")



 
                                              
#animated.append("                                                          - -- -")
#animated.append("                                                        --      --")
#animated.append("                                                       --        --")
#animated.append("                                                       --        --")
#animated.append("                                                       --        --")     
#animated.append("                                                        --      --")   
#animated.append("                                                          - -- -") 




#---------------------------fwrite------------------------------------------------
def write(calculations,top_down_line):    # final output , random movement calculations , line number   -- here top_down_line refers to pos as it would apppear in a list, and that is starting with a zero.
     #print str(calculations[0]) + "calculations" 
     #part = (14*(calculations[0]-1)) + 1 
     #print "part" + str(part)
     #print "top_down_line" + str(top_down_line)     
     
     

  
        
        
    
     animated_top_down_position = ((15*(calculations[0]-1))+ top_down_line)
     #print animated_top_down_position
     #print "end of test output"

     if top_down_line == 0:                  # provide the time if first line detected.
        x = str(datetime.datetime.now())
        return "It is currently " + x[0:len(x)-10]


     if(top_down_line < 15):
         pixel = ""
         for zero in range (len(animated[animated_top_down_position])):   #prints to each left right          #---------- trees -- -- - --
                 pixel += access(animated[animated_top_down_position], zero)
         return pixel 


                                                        #---------- sun animation --   
     #if len(pixel) != 70:              #makes sure that there is always a line to write
      #   while len(pixel) != 70:
                # pixel += " "
     #if top_down_line > calculations[2] and top_down_line < calculations[3]:

     
     #for zero in range (len(sun animation ___ )  :   #prints to each left right          
      #   pixel += access(animated[animated_top_down_position], zero)
     #return pixel


    

    
     else:
         select = 45 + top_down_line
         pixel = ""
         
         for zero in range (len(animated[select])):   #    Base --- walk -- way-- animation
             pixel += access(animated[select], zero)
         
         
         return pixel
                           

     


if x == "write":
   write(0,3,4)


#----------------------Check()-----------------------------------------------------2
#for length of animated[item], to insure flexibility      
def check(mult):
     list = [0]
     
     #here, each line is written. This function is called in a loop to write every line value.
    
     #> trees, filters through the four possible animations of the trees depending on a randomized value. 
     ran = random.randrange(0, 100)
     
     if (ran % 2 == 0) :
         if mult == 1:
            mult += 1
            list[0] = mult
         else:
             mult -= 1
             list[0] = mult
     else:
        if mult == 4:
           mult -= 1
           list[0] = mult
        else:
          mult += 1    
          list[0] = mult                 

     
 
     return list
     
if x == "check":
        check()

#--------------------------fmain(), start here-------------------------------------------------1

def get_time(yyy):
     
     frame = [" "]*27  # defines the screen
     uptime = 0
     calculations = [random.randrange(1,5)]
     clear = ["                                                                  "] * 100
     


     while(uptime == 0):  
          
          calculations = check(calculations[0])
          #calculations = [1]   
          
          
          for zero in range (26):     #assemble/collect print animations
             frame[zero] = write(calculations,zero)


    
                


         
                     
          time.sleep(yyy)   #Refresh rate timer 
          
              

          for zero in range (len(clear)):   #clear the screen
               print clear[zero]           
 
          
          for zero in range (26):    #print
                print frame[zero]
          
          
          

          
          



            
              
                      





if x == "main":
    nest(get_time(options))

#------------------------------------------------------------    works -  



import a


def command(x):
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
    #syntax
    #import command
    #command.order()
#converts text into command and runs it via python modules
# however, input must be in list form
#-------------------------------------------------------------    works -
if x == "meme":
      up = ["print 'eat ass'", "print 'say my name'"]
      command(up)
      a.a() 
      
