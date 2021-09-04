inp = input('Qual a chance de drop do item? (drops/kills) :').split('/')
chance = int(inp[0])/(int(inp[1])-int(input('Quantos inimigos voce matou?')))*100
for aim in [30,40,50,60,70,80,90,95,97]:
    print(f'Para você ter {aim}% de chances de conseguir o item você deverá matar {int(aim/chance)} inimigos no jogo.')