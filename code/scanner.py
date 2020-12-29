import re

def ident_detect(identifer):
    if(identifer == '+'):
        return "addation"
    elif(identifer == '-'):
        return "subtracion"
    elif(identifer == '='):
        return "conditional equal"
    elif(identifer == '*'):
        return "multiplication"
    elif(identifer == '/'):
        return "division"
    elif(identifer == '<'):
        return "smaller than"
    elif(identifer == '('):
        return "opening bracket"
    elif(identifer == ')'):
        return "closing bracket"
    elif(identifer == ':='):
        return "assign"
    elif(identifer == ';'):
        return "semi column"
    else:
        return("identifer")

def run_scanner(code_lines):
    #file = open("example.txt", "r")
    f = open("output.txt", "w")
    file_lines=''
    for l in code_lines:
        file_lines += l

    comments = re.findall("\{(.*?)\}",file_lines)
    for comment in comments:
        file_lines=file_lines.replace('{'+comment+'}' ," ")



    lines = file_lines.splitlines( )
    flag = 0
    for line in lines :
        for words in line.split():
            reserved_words=re.search("read|if|then|else|end|repeat|until|write",words)
            if reserved_words:
                f.write(str(reserved_words.group()) + " , reserved words \n")
                words=words.replace(reserved_words.group(),"",1)
                words=words.strip()

            while(len(words)!=0):
                neg_numbers = re.search("^(-)([0-9])+", words)
                if (neg_numbers) and (neg_numbers.start() == 0) and (flag == 1):
                    f.write(str(neg_numbers.group()) + " , NUM  \n")
                    words = words.replace(neg_numbers.group(), "", 1)
                    flag = 0
                else :
                    flag = 0
                numbers =  re.search("[0-9]+",words)
                if (numbers)and (numbers.start()==0):
                    f.write(str(numbers.group()) + " , NUM  \n")
                    words=words.replace(numbers.group(),"",1)

                identifers = re.search("^[a-zA-Z]([a-zA-Z]|[0-9]|_)*",words)
                if (identifers )and (identifers.start()==0):
                    f.write(str(identifers.group()) + " , ID  \n")
                    words=words.replace(identifers.group(),"",1)



                special_char = re.search("\+|-|\*|/|=|<|\(|\)|;|:=",words)
                if special_char and (special_char.start()==0) and (flag == 0):
                    f.write(str(special_char.group()) + " , "+  ident_detect(special_char.group())  +"\n")
                    words=words.replace(special_char.group(),"",1)
                    flag = 1









#print(identifers)
