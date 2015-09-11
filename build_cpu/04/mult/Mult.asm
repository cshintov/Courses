// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

//num1=RAM[0]
    @R0
    D=M
    @num1
    M=D

//num2=RAM[1]
    @R1
    D=M
    @num2
    M=D

//i=num2+1
    @i
    M=D+1

//prod = 0 and R2 = 0
    @R2
    M=0
    @prod
    M=0

//product loop ; adds num1 to prod num2 times
    (PRODUCT)
        //i=i-1 and jump to end after num2 iteration
        @i
        D=M-1
        M=M-1
        @END
        D;JEQ

        //prod = prod + num1
        @num1
        D=M
        @prod
        M=M+D

        //store prod in R2
        @prod
        D=M
        @R2
        M=D
        
        //loop unconditionally
        @PRODUCT
        0;JMP

//end of the program        
    (END)
        @END
        0;JMP
