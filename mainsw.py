import unbundle_text as un
import bundle_text as bun


def compress(og):
    print("Start")
    totallength=len(og)-1

    #print("Original text:",og)
    bund=bun.bundle_text(og)
    bund.firstpress()
    #print (bund.newtext)
    unbun=un.unbundle_text(bund.newtext)
    unbun.unbundle()
    #print("First attempt:",unbun.newtext)

    print("Tracking:")
    bund.cur=0
    i=0
    while i <=len(og)-1:
        if i%20==0:
            print ("...................",round(i*100/totallength,1),"%")
        if(i==totallength) :
            print("................... 100% DONE!")
        unbun.cur=i
        #print (og[i]," 1")
        #print (unbun.letter()," 2")
        #print (bund.letter())
        if og[i]!=" ":
            bund.cur=bund.cur+1
            #print("bundcur:",bund.cur,bund.letter())
            #print(unbun.newtext)
        if unbun.letter() != og[i]:
            if og[i]==' ':
                #print("HELLLLOOOO")
                bund.insert(' ')
                bund.cur=bund.cur+1
                #print(bund.newtext)
            else:
                while og[i]!=' ' and i>=0:
                    i=i-1
                    bund.cur=bund.cur-1

                bund.insert('<')
                #print("START <<<<")
                #print(bund.newtext)
                i=i+1
                while og[i]!=' ' and i!=len(og)-1:
                    i=i+1
                    bund.cur=bund.cur+1
                    #print(len(og),i)

                bund.cur=bund.cur+1
                bund.insert(' ')
                #print(">>>> END")
                #print(bund.newtext)
                bund.cur=bund.cur+1
                #print("New bundletext:",bund.newtext)
                #print("New unbundletext:",unbun.newtext)

            unbun.text=bund.newtext
            unbun.newtext=""
            #print(unbun.text," test")
            unbun.unbundle()
        i=i+1

    #print("New bundletext:",unbun.text)
    #print("New unbundletext:",unbun.newtext)
    return bund.newtext
def decompress(bdle):
    unbun=un.unbundle_text(bdle)
    unbun.unbundle()
    return unbun.newtext
