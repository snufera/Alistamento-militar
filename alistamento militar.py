print("""\nOlá! Caro usuário!
Digite sua idade ou o da pessoa a qual deseja descobrir se 
já está na hora de fazer o alistamento militar.
\033[33mDIGITE APENAS NÚMEROS\033[m""")

from time import sleep
sleep(0.5)

import datetime
today = datetime.date.today()
year = today.year
nascimento = int(input("\nDigite o ano de nascimento: "))
alistamento = nascimento + 18
prazo_falta = alistamento - year
prazo_passou = year - alistamento

print("\n\033[35m(Analisando...)\033[m")
sleep(1)

if alistamento < year:  # passou o prazo
    print(f"\n\033[31mO prazo para se alistar já passou. Você tem {prazo_passou} ano(s) sem a reservista.\033[m\n")
elif alistamento > year:  # falta tempo
    print(f"\033[36m\nVocê deverá se alistar em {alistamento}. Aguarde mais {prazo_falta} ano(s).\033[m\n")
else:  # ano de se alistar
    print(f"\n\033[32mChegou a hora de se alistar! Você já tem 18 anos!\033[m\n")
