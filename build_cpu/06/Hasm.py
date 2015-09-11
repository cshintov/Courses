'''The Hack assembler'''
import sys,os


class Parser(object):
    '''The parser module which parses the input file'''
    currentcommand = None
    def __init__(self,sourcefile):
        self.sourcefile = sourcefile
        self.current = 0

    def hasMoreCommands(self):
        if self.rest > 0:
            return True
        else:
            return False

    def remove_wh_space(self):
        copy = self.sourcefile[:]
        for currentcommand in self.sourcefile:
            if currentcommand.startswith('//') or currentcommand == '\r\n':
                copy.remove(currentcommand)
            elif '//' in currentcommand:
                pos = copy.index(currentcommand)
                index = currentcommand.index('//')
                currentcommand =  currentcommand[:index]
                del copy[pos]
                copy.insert(pos,currentcommand)
        self.sourcefile = copy[:]
        self.rest = len(self.sourcefile)
        for pos,item in enumerate(self.sourcefile):
            self.sourcefile[pos] = item.strip()


    def advance(self):
        '''gets the next instruction'''
        if self.hasMoreCommands():
            self.currentcommand = self.sourcefile[self.current]
            self.rest -= 1
            self.current += 1
        if '=' in self.currentcommand:
            self.eqindex = self.currentcommand.index('=')
        else :
            self.eqindex = None

        if ';' in self.currentcommand:
            self.colindex = self.currentcommand.index(';')
        else :
            self.colindex = None


    def commandType(self):
        '''returns the type of the current instruction'''
        if self.currentcommand.startswith('@'):
            return 'A_COMMAND'
        if self.currentcommand.startswith('('):
            return 'L_COMMAND'
        return 'C_COMMAND'


    def symbol(self):
        '''returns the symbol of the a-instruction and label declaration'''
        if self.commandType() is 'A_COMMAND':
            return self.currentcommand[1:]

        if self.commandType() is 'L_COMMAND':
            return self.currentcommand[1:-1]


    def dest(self):
        '''returns the destination mnemonic(filed of the instruction)'''
        if self.eqindex:
            dest = self.currentcommand[:self.eqindex].strip()
            return dest

        return 'null'


    def comp(self):
        '''returns the computation mnemonic(field of the instruction)'''
        if '=' in self.currentcommand:
            index = self.currentcommand.index('=')
            rest = self.currentcommand[index+1:].strip()
            if self.colindex:
                comput = rest[:colindex].strip()
            else:
                comput = rest.strip()
        else:
            comput = self.currentcommand[:self.colindex]

        return comput


    def jump(self):
        '''returns the jump field of the instruction'''
        if self.colindex:
            jmp = self.currentcommand[self.colindex+1:].strip()
            return jmp
        return 'null'


class Code(object):
    '''returns the binary code of the different fields in the instruction'''
    
    ctable = {
              '0':'0101010', '1':'0111111', '-1' : '0111010', 'D' :  '0001100','D-1' :'0001110','!D' :  '0001101','-D' : '0001111','D+1'  :'0011111', 'A' :'0110000',               'M':'1110000' ,'!A':'0110001'  ,'!M':'1110001','-A': '0110011' ,'-M':'1110011','A+1' : '0110111' ,'M+1':'1110111', 'A-1' : '0110010' , 'M-1':'1110010',               'D+A' : '0000010', 'D+M' : '1000010', 'D-A' : '0010011', 'D-M' : '1010011','A-D' : '0000111','M-D' : '1000111','D&A' : '0000000','D&M' : '1000000',                   'D|A' :'0010101' ,  'D|M':'1010101'
             }   
    dtable = {'null':'000','M':'001','D':'010','MD':'011','A':'100','AM':'101','AD':'110','AMD':'111'}
    jtable = {'null':'000','JGT':'001','JEQ0':'010','JGE':'011','JLT':'100','JNE':'101','JLE':'110','JMP':'111'}
    def dest(self,mnem):
        return self.dtable[mnem] 

    def comp(self,mnem):
        return self.ctable[mnem] 

    def jump(self,mnem):
        return self.jtable[mnem]


class SymbolTable(object):
    '''creates the symbol table and provides access to its elements'''
    def __init__(self):
        self.symtab = {'SP':0, 'LCL':1,'ARG':2,'THIS':3,'THAT':4,'SCREEN':16384,'KBD':24576}
        for i in range(16):
            self.symtab['R'+str(i)] = i
    
    def addEntry(self,symbol,address):
        self.symtab[symbol] = address

    def contains(self,symbol):
        return symbol in self.symtab

    def getAddress(self,symbol):
        return self.symtab[symbol]


def main(sourcefile):
    '''The main function which translates the assembly code to machine code'''
    fh = open(sourcefile,r'r')
    source= fh.readlines()

    targ,ext = os.path.splitext(sourcefile)
    targfile = targ + '.hack'
    tfh = open(targfile,'w')
    
    parser = Parser(source)
    code = Code()
    symtab = SymbolTable()
    parser.remove_wh_space()

    '''The first pass: adds labels to the symbol table'''
    labelnum = 0
    while parser.hasMoreCommands():
        parser.advance()
        if parser.commandType() is 'L_COMMAND':
            labelnum += 1
            print 'current command ',parser.current,' ',parser.currentcommand
            if not symtab.contains(parser.symbol):
                symtab.addEntry(parser.symbol(),parser.current-labelnum)

    '''The second pass: adds variables to the symbol table and translates all the instuctions'''
    parser.current = 0
    parser.rest = len(parser.sourcefile)
    varnum = 0
    while parser.hasMoreCommands():
        parser.advance()
        if parser.commandType() is 'A_COMMAND':
            if parser.symbol().isdigit():
                machcode = '{0:016b}'.format(int(parser.symbol()))+'\n'
            else:
                if not symtab.contains(parser.symbol()):
                    symtab.addEntry(parser.symbol(),16+varnum)
                    varnum += 1
                address = symtab.getAddress(parser.symbol())
                machcode = '{0:016b}'.format(address)+'\n'
        elif parser.commandType() is 'C_COMMAND':
            machcode = '111' + code.comp(parser.comp()) +  code.dest(parser.dest()) + code.jump(parser.jump())+'\n'
        else:
            continue
        tfh.write(machcode)
    
    tfh.close()

if __name__=='__main__':
    if len(sys.argv) != 2:
        print 'usage: Hasm.py sourcefile'
        sys.exit(1)
    main(sys.argv[1])
