def main():
    global media
    nota=['0','0','0','0']
    for i in range(0, 4):
        nota[i]=float(input('Digite a nota '+ str(i+1) +'.'))

    media=(nota[0]+nota[1]+nota[2]+nota[3])/4
    switch()
def switch():
    global media
    if media>=6:
        print('Aprovado')
    elif media>=3:
        print('Exame')
    else:
        print('Retido')
if(__name__=='__main__'):
     main()