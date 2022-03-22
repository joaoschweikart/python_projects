from time import sleep


def ajuda(com):
    titulo(f'\033[30:45mAcessando o manual do comando {com}\033[m')
    help(com)


def titulo(msg):
    tam = len(msg) + 4
    print('')
    print('=' * tam)
    print(f'  {msg}')
    print('=' * tam)


#programa principal
comando = ''
while True:
    sleep(1)
    titulo('\033[30:46mSISTEMA DE AJUDA PyHelp\033[m')
    sleep(1)
    comando = str(input('\033[30;43mDigite a função ou biblioteca que você deseja acessar (FIM para finalizar o programa): \033[m'))
    if comando.upper().strip() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('\033[30:42mATÉ LOGO\033[m')
