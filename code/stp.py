from scanner import run_scanner
class token:
    tokenvalue=""
    tokentype=""
    def __init__(self, tokenvalue, tokentype):
        self.tokentype = tokentype
        self.tokenvalue = tokenvalue
    def is_ID(self):
        if(self.tokentype=="ID"):
            return True
        else:
            return False
    def is_NUM(self):
        if(self.tokentype=="NUM"):
            return True
        else:
            return False
    def is_reservedword(self):
        if(self.tokentype=="reserved words"):
            return True
        else:
            return False
    def is_terminator(self):
        if(self.tokenvalue==";"):
            return True
        else:
            return False
    def iscomparison(self):
        if((self.tokenvalue=='<')or(self.tokenvalue=='=')):
            return True
        else:
            return False
    def isaddop(self):
        if((self.tokenvalue=='+')or(self.tokenvalue=='-')):
            return True
        else:
            return False
    def ismulop(self):
        if((self.tokenvalue=='*')or(self.tokenvalue=='/')):
            return True
        else:
            return False

def return_tokens(code_lines):
    run_scanner(code_lines)
    f = open("output.txt", "r")
    lines =f.readlines()
    outputs=[]

    specialsymbols = [':=','+','-','*','/','=','<', '(',')',';']
    for line in lines:
        t = line.split(',')
        t[1]=t[1].strip()
        t[0]=t[0].strip()
        if(t[0] in specialsymbols):
            t[1] ="special symbols"


        mytoken = token(t[0],t[1])

        outputs.append(mytoken)

    mytoken=token("END","END")
    outputs.append(mytoken)
    return(outputs)



