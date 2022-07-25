INCLUDE 'EMU8086.INC'
.MODEL SMALL
.STACK 100H
.DATA
ID DB ?    
B DW "CSE_56$"
N DW "SHAKIL$"
S DW "PC_A$"
.CODE  

MAIN PROC
    
    MOV AX,@DATA
    MOV DS,AX 
    
    MOV AH,1
    INT 21H
    MOV ID,AL
    SUB ID,48
    PRINTN
    
    

    MOV AH,2
    MOV DL,ID
    ADD DL,48
    INT 21H 
    PRINTN 
    
    MOV AH,9
    LEA DX,B
    INT 21H
    PRINTN     
         
    MOV AH,9
    LEA DX,N
    INT 21H
    PRINTN  
    
    MOV AH,9
    LEA DX,S
    INT 21H
    PRINTN

     EXIT:
     MOV AH,4CH
     INT 21H
     MAIN ENDP
END MAIN