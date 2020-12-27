# Script to emulate a TM given a transition function and an input tape
#
# runTM( tf , s , t , p ) -> ( tf, halt_state, halt_tape , halt_pos )
#
# where "tf" is the transition function, "s" is a string represeting
# current state, "t" is a list of symbols representing the current
# tape, "p" is an integer index of the current position of the TM head
# on the tape.
#
# Conventions: Symbol for a blank cell is "∆"; assume start and halt
# states are "S0" and "SH" respectively.
#
# The TM transition function "tf" is a python dictionary
# (associative array) of the form:
#
# tf = { ...
#       ( current_state , input_symbol ) : ( new_state , write_symbol , dir ) ,
#       ... }
#
# where current_state, new_state, input_symbol, write_symbol are
# strings; dir is integer 0 or 1 representing a move of the TM head
# left or right respectively.
#
# Written by Nela Brockington, 23rd December 2020, London U.K.

# Example transition function and input for a parity-bit TM:

tf_parity = { ( 'S0' , '0' ) : ( 'S0' , '0' , 1 ) , 
              ( 'S0' , '1' ) : ( 'S1' , '1' , 1 ) , 
              ( 'S0' , '∆' ) : ( 'SH' , '0' , 1 ) , 
              ( 'S1' , '0' ) : ( 'S1' , '0' , 1 ) , 
              ( 'S1' , '1' ) : ( 'S0' , '1' , 1 ) , 
              ( 'S1' , '∆' ) : ( 'SH' , '1' , 1 ) }

input_parity = [ "0" , "1" , "1" , "0" , "1" , "0" , "0" ]

# Example transition function and input for a/b switching TM:

tf_switch = { ( "S0" , "b" ) : ( "S0" , "a" , 1 ) ,
              ( "S0" , "a" ) : ( "S0" , "b" , 1 ) ,
              ( "S0" , "∆" ) : ( "SH" , "∆" , 0 ) } 

input_switch = [ "a" , "a" , "a" , "b" , "b" , "b" , "a" ]
              

# Procedure to return the result of running a TM (defined by its
# transition function) on a given input tape. 

def run_TM( tf , s , t , p ): 
    
    if tf[( s , t[p] )][ 0 ] == 'SH':

        return ( tf , 
                 "SH" , 
                 next_tape( tf , s , t , p ) , 
                 next_pos( tf , s, t , p ) )

    else: 
        
        return run_TM( tf , 
                       tf[( s , t[p] )][ 0 ] ,
                       next_tape( tf , s , t , p ) ,
                       next_pos( tf , s , t , p ) )                 

                


# Procedure to return the next iteration of the tape given transition
# function, current state, current tape and current position:

def next_tape( tf , s , t , p ):

    # Check whether moving right will take index outside of range:
    if p + tf[(s , t[p] )][2] >= len(t):

        # If so, write symbol and add new blank cell on the right of
        # the tape:
        return t[:p] + [ tf[( s , t[p] )][ 1 ] ] + ["∆"]

    # Check whether moving left will take index outside of range:
    elif p + tf[(s , t[p] )][2] == 0:
        
        # If so, write symbol and add new blank cell on the left of
        # the tape:
        return ["∆"] + [ tf[( s , t[p] )][ 1 ] ] + t[1:]
             
    # Otherwise write symbol:
    else: 
        return t[:p] + [ tf[( s , t[p] )][ 1 ] ] + t[p+1:]



# Procedure to return the next position given the transition function,
# current state, current tape and curretn position:

def next_pos( tf , s , t , p):

    # Check whether TM head will move left:
    if tf[(s , t[p] )][ 2 ] == 0:

        # Check whether doing so will take index out of range: 
        if p == 0:

            # Keep position at zero, as additional blank cell will be
            # added to the left of the tape by the next_tape function:
            return 0

        # Otherwise subtract 1 from the position:
        else:
            return p - 1

    # If TM head will move right, add 1 to the position:
    else: 
        return p + 1


        
             
     

    
