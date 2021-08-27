from os import system

TITULO = ('*' * 20 + ' Calculadora de inimigos mortos para dropar items ' + '*' * 20)
QUANTITIES = [30,40,50,60,70,80,90,95,97]

# STRING IN CASE USER INPUT INVALID CHANCE
CHANCESR = 'Por favor digite uma chance valida :' 

# STRING IN CASE USER INPUT INVALID KILL COUNT
KILLCR = 'Por favor digite um numero de kills valido :'


def hasNum(str): # CHECK IF STRING HAS A NUMBER

    for i in str:
        if i.isnumeric():
            return True
    return False



def numbersFS(string): # RETURN ALL OF THE NUMBERS IN A STRING OR -1 IF NO NUMBERS ARE PRESENT
    output = ''

    for i in string:
        if i.isnumeric():
            output += i
            
    if output == '':
        return -1
    return int(output)


# GET USER INPUTS, VALIDADATE THEM AND TRANSFORM INTO PERCENTAGE IF NEEDED
def getInputs(chS='Qual a chance de drop do item? (porcentagem ou drops/inimigos mortos):',
            kcS='Quantas vezes voce derrotou esse inimigo? :'):

    system('cls')
    print(TITULO)
    chance = input(chS)
    killsInp = input(kcS)
    percent = ['',''] # LIST WITH Y ITEM DROPS EVERY X ENEMY KILLS
    kills = numbersFS(killsInp) # CONVERT ENEMY KILL COUNT INTO NUMBERS

    #IF KILLS IS NOT A NUMBER
    if kills == -1:
        return getInputs(CHANCESR,KILLCR)

    # IF USER GIVES DROP CHANCE IN PERCENTAGE 
    if chance.isdigit() or '%' in chance:
        output = numbersFS(chance) # NUMBERS FROM USER INPUT

        # IF CHANCE INPUT IS INVALID CALL RECURSION
        if output != -1:
            return output, kills
        else:
            return getInputs(CHANCESR,KILLCR)
    
    # IF USER GIVES THE AMOUNT OF ENEMIES KILLED FOR THE ITEM DROP
    else:

        for i in chance:

            # IF i IS NaN IN CHANCE STRING 
            if not i.isnumeric():

                # SPLIT THE CHANCE IN THE FOUND CHARACTER
                chanceS = [chance[:chance.index(i)],chance[chance.index(i):]]

                # CHECK IF BOTH SUBSTRINGS HAVE NUMBERS
                if hasNum(chanceS[0]) and hasNum(chanceS[1]):

                    # CONVERTING BOTH STRINGS INTO NUMBERS
                    percent[0] = numbersFS(chanceS[0])
                    percent[1] = numbersFS(chanceS[1])

                    # CALCULATING OUTPUT PERCENTAGE
                    output = (percent[0] / percent[1])*100
                    return output, kills

                # IF NO NUMBER IS FOUND IN EITHER SUBSTRING REDO FUNCTION
                else:

                    return getInputs(CHANCESR,KILLCR)
        return getInputs(CHANCESR,KILLCR)


 
def printQuantity(aim, chance, kills):
    prt = (aim/chance) # HOW MANY ENEMIES SHOULD BE KILLED FOR THE DESIRED DROP CHANCE

    # CHECK IF CURRENT DROP CHANCE SURPRASSED DESIRED DROP CHANCE
    if int(prt) > 0:
        print(f'Para você ter {aim}% de chances de conseguir o item você',
            f' deverá matar {int(prt)} inimigos no jogo.')
    
    # IF ITEM SHOULD HAVE BEEN DROPED ALREADY
    elif aim == 97:
        print('Este item provavelmente sera dropado em alguns inimigos mortos!')



def main():
    chance, kills = getInputs()
    system('cls')
    print(TITULO)
    for i in QUANTITIES:
        printQuantity(i,chance,kills)



if __name__ == '__main__':
    main()