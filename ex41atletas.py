from time import sleep
print('=-'*30)
print('MIRIM, INFANTIL, JÚNIOR, SÊNIOR E MASTER')
print('=-'*30)
idade = int(input('Digite sua idade: '))
print('PROCESSANDO...')
sleep(2)
if idade <= 9:
    print('Sua idade é de {} ano(s). Sua categoria é \033[7:40mMIRIM!\033[m'.format(idade))
elif idade <= 14:
    print('Sua idade é de {} ano(s). Sua categoria é \033[7:40mINFANTIL!\033[m'.format(idade))
elif idade <= 19:
    print('Sua idade é de {} ano(s). Sua categoria é \033[7:40mJÚNIOR!\033[m'.format(idade))
elif idade <= 25:
    print('Sua idade é de {} ano(s). Sua categoria é \033[7:40mSÊNIOR!\033[m'.format(idade))
else:
    print('Sua idade é de {} ano(s). Sua categoria é \033[7:40mMASTER!\033[m'.format(idade))