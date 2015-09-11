// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

(WAITLOOP)
//initialisations
    //address = SCREEN
    @SCREEN
    D=A
    @address
    M=D
    //n=8192 ; 8192 because there are 8192 registers in the screen memory map
    @8192
    D=A
    @num
    M=D
    //listens the keyboard and jumps to CLEAR or FILL according to the content
    @KBD
    D=M
    @CLEAR  // if zero
    D;JEQ
    @FILL   // if nonzero
    D;JNE

    (FILL)
    @R0
    M=-1
    @FILLORCLEAR
    0;JMP

    (CLEAR)
    @R0
    M=0

//fill or clear loop ; fills or clears the screen at the end of the loop
    (FILLORCLEAR)
        //num=num-1 and jump to end after num(8192) iteration
        @num
        D=M-1
        M=M-1
        @WAITLOOP   //jump to wait loop after clearing or filling
        D;JLT

        //RAM[address] = RAM[0];fills or clear each register sequentially
        @R0
        D=M
        @address
        A=M
        M=D
        //address ++
        D=A+1
        @address
        M=D
        
        //loop unconditionally
        @FILLORCLEAR
        0;JMP
