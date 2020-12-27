# run-turing-machine
Script to return the result of running a TM, given the transition function and the input.

# Implementation
`runTM( tf , s , t , p ) -> ( tf , halt_state , halt_tape , halt_pos )`                     
                                                                                         
where "tf" is the transition function, "s" is a string represeting current state, "t" is a list (of strings) representing current tape symbols, "p" is an integer index of the current position of the TM head on the tape.                                                                            
                                                                                        
Conventions: Symbol for a blank cell is "∆"; assume start and halt states are "S0" and "SH" respectively.                                                  
                                                                                        
The TM transition function "tf" is a python dictionary (associative array) of the form:                                                        
                                                                                        
`tf = { ...                                                                              
      ( current_state , input_symbol ) : ( new_state , write_symbol , dir ) ,           
      ... }`                                                                             
                                                                                        
where current_state, new_state, input_symbol, write_symbol are strings; dir is integer 0 or 1 representing a move of the TM head left or right respectively.                                                             
                                                                                        
# Example transition function and input for a parity-bit TM:                              

`tf_parity = { ( 'S0' , '0' ) : ( 'S0' , '0' , 1 ) ,
              ( 'S0' , '1' ) : ( 'S1' , '1' , 1 ) ,
              ( 'S0' , '∆' ) : ( 'SH' , '0' , 1 ) ,
              ( 'S1' , '0' ) : ( 'S1' , '0' , 1 ) ,
              ( 'S1' , '1' ) : ( 'S0' , '1' , 1 ) ,
              ( 'S1' , '∆' ) : ( 'SH' , '1' , 1 ) }

input_parity = [ "0" , "1" , "1" , "0" , "1" , "0" , "0" ]

>>> run_TM( tf_switch , "S0" , input_switch , 0 )[2]`

# Known issues:
- Only the computational kernal is provided; should add an interaction shell (I/O)
- Only "SH" is a halt state; should be extended to allow set of halt states in halt condition (I/O also?)
