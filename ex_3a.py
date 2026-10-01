def fat(val):
    totalfat=1
    while val > 1:
        totalfat=val*totalfat
        val-=1
    return totalfat

def main():
    val=int(input('Insira um valor: '))
    res=fat(val)
    print('O valor do fatorial de', val, 'é de', str(res)+'.')
if(__name__=='__main__'):
     main()