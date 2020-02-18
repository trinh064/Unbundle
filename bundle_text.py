class bundle_text:
    def __init__ (self,text):
        self.text=text
        self.cur=0
        self.newtext=""
    def firstpress(self):
        for x in self.text:
            if x!=" ":
                self.newtext=self.newtext+x
    def letter(self):
        return self.newtext[self.cur]
    def insert(self,specialsign):
        self.newtext=self.newtext[0:self.cur]+specialsign+self.newtext[self.cur:len(self.newtext)]
    def delete(self):
        self.newtext=self.newtext[0:self.cur]+self.newtext[self.cur+1:len(self.newtext)]
