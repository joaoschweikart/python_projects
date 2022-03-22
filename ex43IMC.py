print('CÁLCULO DE Indíce de Massa Corpórea (IMC)')

peso = float(input('Digite seu peso em kilos: '))
altura = float(input('Digite sua altura em metros: '))

IMC = peso / altura**2

if IMC < 18.5:
    print('Seu IMC é de {:.2f}. Você está abaixo do peso ideal!'.format(IMC))
elif IMC < 25:
    print('Seu IMC é de {:.2f}. Você está no peso ideal!'.format(IMC))
elif IMC < 30:
    print('Seu IMC é de {:.2f}. Você está com sobrepeso!'.format(IMC))
elif IMC <= 40:
    print('Seu IMC é de {:.2f}. Você está com obesidade!'.format(IMC))
else:
    print('Seu IMC é de {:.2f}. Você está com obesidade mórbida!'.format(IMC))
