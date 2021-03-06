import wget
import os

def scaricaurl(url,name):
    try: os.remove(name)
    except: pass
    wget.download(url,name)
    print(" ",name,"Downloaded")
    
def listahosts(filename):
    l=[]
    with open(filename,'r') as f:
        temp=f.readlines()
    l=[i for i in temp if not i.startswith('#')]
    try: os.remove(filename)
    except: pass
    return l

def logo():
    print('''
*************************************///////***********///////////((((((((((((((((((((((((#########%
*****************************************************************//(((((((((((((((((((((###########%
*********************************************************************///((((((((((((((#############%
******************************************************************//////////(((((((################%
*************      ,*****************************************  *////////////////.    ##############%
*************   ********************************************  /////////////////////  ##############%
************* **************************************.     ,* /////,    ,/////////////(##########%%%&
******************************************************////*  ,/,          *//////////(((#####%%%%%%&
***************************************************/////*..*///           ./////(/((((((((#%%%%%%%%&
************************************************/////         //         ./////((((((((((((#%%%%%%%&
****************************.   .************//////*           //           /((((((((((((((((%%%%%%&
*************************,         ********////////*            ,/,           /(((((((((((((((%%%%%&
***********************              ***/////////////,           ,///         (((((((((((((####%%%%&
/*******************       ...,        */////////////////.       ///((((((((((((((((((((########%%&&
//***************.                       .///////////////       /((((((((((((((((((((############%&&
/**************,         ******    ,        /////////////*    *(((((((((((((((((((################&&
/*************     *.   .***///    *//        /////////////(((((((((((((((((((((################%%%&
*************.    ,,    ,*/////    /////        ,///////(((((((((((((((((((((################%%%%%%&
*************                                     .//(((((((((((((((((((((################%%%%%%%%%&
*************    ***    */****,    ...               ((((((((((((((((((#################%%%%%%%%%%%&
*************    ,/*    //////,    //////    */        /((((((((((((#################%%%%%%%%%%%%%%&
**************    /*    //////.   .//////    /           *(((((((#################%%%%%%%%%%%%%%%&&&
************//,                                  /(*        ((#################%%%%%%%%%%%%%%%%&&&&@
/********///////                              *((((((/        ##############%%%%%%%%%%%%%%%%&&&&&&&@
(****/////////////       .*///    /*.      .((((((((((((        (########%%%%%%%%%%%%%%%%&&&&&&&&&&@
(/*//////////////////.                  ,(((((((((((((####,       *###%%%%%%%%%%%%%%%%&&&&&&&&&&&&@@
((/////////////////////////*,....,*((((((((((((((((#########*        %%%%%%%%%%%%%%&&&&&&&&&&&&&&@@@
(((/////////////////////////((((((((((((((((((((###############        %%%%%%%%%%&&&&&&&&&&&&&&&@@@@
((((/////////////////////((((((((((((((((((((#################%%%        #%%%%&&&&&&&&&&&&&&&&&@@@@@
(((((/////////////////(((((((((((((((((((((################%%%%%%%%,       *&&&&&&&&&&&&&&&&@@@@@@@@
(((((((/////////////((((((((((((((((((((################%%%%%%%%%%%%%(        &&&&&&&&&&&@@@@@@@@@@@
(((#####////////(((((((((((((((((((((################%%%%%%%%%%%%%%%%&&%        %&&&&&@@@@@@@@@@@@@@
##########//(/((((((((((((((((((((################%%%%%%%%%%%%%%%%&&&&&&&&.       #@@@@@@@@@@@@@@@@@
############(((((((((((((((((((#################%%%%%%%%%%%%%%%&&&&&&&&&&&&&*       #@@@@@@@@@@@@@@@
############# ((((((((((((((#################%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&#     (@@@@@@@@@@@@@@@
#############%%%#(((((((((################%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@
##########%%%%%%%%%#((#################%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@
########%%%%%%%%%%%%%%%#############%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#####%%%%%%%%%%%%%%%%%%%%%%%#####%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
##%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
%%%%%%%%%%%%% Powered by piopy thanks to adaway, x0uid, StevenBlack , cttynul @@@@@@@@@@@@@@@@@@@@@@
%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&%%%%%%%%%%%%&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
          ''')

# if __name__ == '__main__':
logo()  
hosts=[]
passa=False
while passa == False:
    print("Cosa vuoi bloccare? Inserisci (anche pi?? di una lettera)\n\ns per bloccare gli ads di spotify\na per pubblicit?? varie (adaway)\nb per pubblicit?? varie (steven black's list)\nn per bloccare che i dati personali vadano all'nsa\n")
    scelta=input("> ")
    if 'a' in scelta:
        scaricaurl('https://adaway.org/hosts.txt','adaway')
        hosts+=listahosts('adaway')
    if 's' in scelta:
        scaricaurl('https://raw.githubusercontent.com/x0uid/SpotifyAdBlock/master/SpotifyBlocklist.txt','spotify')
        hosts+=['127.0.0.1 '+l for l in listahosts('spotify')]
    if 'b' in scelta:
        scaricaurl('https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts','sb')
        hosts+=listahosts('sb')
    if 'n' in scelta:
        scaricaurl('https://raw.githubusercontent.com/cttynul/NSABlocklist/master/HOSTS','nsa')
        hosts+=listahosts('nsa')
    passa=True
    if not 'a' in scelta and not 's' in scelta and not 'b' in scelta and not 'n' in scelta: 
        print("Trovata lettera non supportata.")
        passa=False
temp='## PIOPY HOSTS FILE ##\n'
for h in hosts:
    temp+=h
try: os.remove('hosts')
except: pass
with open('hosts','w') as f:
    f.write(temp)
print("\nScrivi il tuo sistema operativo (w = windows, l=linux, m=mac)\n")
t=input("> ")
print("\nMetti il file hosts generato in: ")
if 'w' in t: print(r"C:\Windows\System32\drivers\etc")
elif 'l' in t: print("/etc/hosts")
elif 'm' in t: print("/private/etc/hosts")
else: print("Scelta non valida")
print("")
input("Press enter to end program.")