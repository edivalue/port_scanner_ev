import socket, sys, threading

if len(sys.argv) > 1:
	target=socket.gethostbyname(sys.argv[1])
else:
	target= socket.gethostbyname(input('Enter host\'s name: '))

woo=[]

#type = string
print('\nHost\'s IP_Address: ',target,'\n')
print('Searching for weak ports\nLOADING....',end=' ')	
icounter=0


def scanport(target, port):
        global icounter, woo
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if s == 0:
                print(' {target} ~~~Port {port} is [open]')
                print('before close')
                s.close()
                icounter=2
                woo.append('if')

        else:
                icounter=1
                woo.append('else')
		
	
		
f=[]		
for i in range(1, 8001):
    scan=threading.Thread(target=scanport, args=(target, i))
    scan.start()
    f.append(scan)
    if isinstance(ri, str):
        with open('scan.txt', 'a') as sf:
            sf.write(ri)
    else:
        ri=f.pop()
        R=str(ri)
        with open('scan1.txt', 'a') as sf1:
            sf1.writelines(R)
			
    		sf1.close()
	
		
print('End ')

if 'if' in woo:
	roo=woo.count('if')
	print(f'{roo} WEAK PORT(S) FOUND')
else:
	print('NO WEAK PORTS')
print()
#with open('scaner.txt','w') as sy:
#	sy.write(f)
