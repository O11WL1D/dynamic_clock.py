#-------------------------program resources--------------------------------------------------------------------


x = "main"
options = input("please enter a desired animation speed( in terms of seconds per frame for this instance of dynamic_clock.py - if unsure enter the number five.") 


def access(x,y):
      return x[y] 


def assign(x,y,val):
    
        x[y] = val


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
animated.append("                           ")
animated.append("                                ")
animated.append("                               \|")
animated.append("                               -  -")
animated.append("                               /  \ ")
animated.append("                                 |")  
animated.append("                                /")
animated.append("                               /")
animated.append("______________________________|________________________________________________")
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
animated.append("                          ")
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
animated.append("                        ")                        
animated.append("                       ")
animated.append("                        \ | ")
animated.append("                        _   -")
animated.append("                         /  \ ")
animated.append("                           \\")
animated.append("                            \ ")
animated.append("                             \\")
animated.append("______________________________|________________________________________________")

# Bottom walkway
        
animated.append(" ")
animated.append(" ")
animated.append("                              . ")
animated.append(" ")
animated.append("      . ")      
animated.append("       _          .                                                ")
animated.append("                         .             -                       ")           
animated.append("               .                      -              .    - ")
animated.append("                         .                                   ")
animated.append("  .        .                  -")
animated.append("  .")
animated.append("                  -                            -- -  .")



 
                                              
#animated.append("                                                          - -- -")
#animated.append("                                                        --      --")
#animated.append("                                                       --        --")
#animated.append("                                                       --        --")
#animated.append("                                                       --        --")     
#animated.append("                                                        --      --")   
#animated.append("                                                          - -- -") 


# features for later edition 

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
def child_1(multi):
      list = [0]
      if multi == 1:
            multi += 1
            list[0] = multi
      else:
             multi -= 1
             list[0] = multi
      

      return list 

def child_2(multi):
      list = [0]
      if multi == 4:
           multi -= 1
           list[0] = multi
      else:
          multi += 1    
          list[0] = multi
       

      return list
      
def check(mult):
     
     ran = random.randrange(0, 100)
     
     if (ran % 2 == 0) :
         bud = child_1(mult)  
     else:
        bud  = child_2(mult)             

     return bud
     
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
    get_time(options)

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
