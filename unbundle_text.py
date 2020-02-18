import enchant
global dict
dict=enchant.Dict("en_US")
class unbundle_text:
    def __init__(self,text):
        self.text=text
        self.cursor=0

        self.newtext=""
        self.cur=0

    def catch(self):
        if (self.cursor+16)<len(self.text):

            return self.text[self.cursor:self.cursor+16]
        else:
            #print(i)
            return self.text[self.cursor:len(self.text)]
    def findword(self):
        catchtext=self.catch()
        word=""
        l=len(catchtext)
        for i in range(l):
            word=catchtext[0:(l-i)]
            if word[0] in [" "]:
                return -1
            if word[0]=="<":

                for j in range(len(word)):
                    if word[j]==">":
                        #print("j",j)
                        return -j*3

            if not dict.check(word[0]):
            #word[0] in [",", ";", ".", "!", "?","-"]:
                return -2
            if dict.check(word):
                return l-i
    def unbundle(self):
        j=0
        length=len(self.text)-1
        while self.cursor<length:
            flag=self.findword()
            if flag==-1:
                j=j+1
                self.cursor=j
            elif flag==-2:
                j=1+j
                self.newtext=self.newtext[0:len(self.newtext)-1]
                self.newtext=self.newtext+self.text[self.cursor:j]+" "
                self.cursor=j
            elif flag<0:
                j=int(-flag/3+j)

                self.newtext=self.newtext+self.text[self.cursor+1:j]+" "

                j=j+1
                self.cursor=j
                #print(self.text[j])
            else:
                j=flag+self.cursor
                self.newtext=self.newtext+self.text[self.cursor:j]+" "
                self.cursor=j
        self.cursor=0
    def letter(self):
            return self.newtext[self.cur]
