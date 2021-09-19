import random


# receives a dice roll in the following format: "3d6", or "3d6+5" which adds the modifier to the total
def roll(par):
    if par.find("+") == -1:  # if no plus sign, aka no modifier
        dice_amount = int(par[0:par.find("d")])
        dice_type = int(par[par.find("d")+1:len(par)])
        modifier = 0
    else:
        dice_amount = int(par[0:par.find("d")])
        dice_type = int(par[par.find("d") + 1:par.find("+")])
        modifier = int(par[par.find("+"):len(par)])

    total = 0
    for i in range(dice_amount):
        current_roll = random.randint(1, dice_type)
        print(current_roll)
        total += current_roll
    if modifier == 0:
        print("sum:", str(total))
    else:
        print("sum:", str(total) + "+" + str(modifier) + " = " + str(total + modifier))
    return total + modifier


def test(dice_type, amount):
    rem = [0] * (dice_type + 1)
    pres = []
    for x in range(0, amount):
        rem[roll("1d" + str(dice_type))] += 1
    print(rem[1:(dice_type + 1)])
    for i in range(len(rem)):
        pres.append(rem[i] / amount * 100)
    print(pres[1:(dice_type + 1)])


def main():
    run = True
    while run:
        inp = input("enter command:\n")
        inp = inp.lower()
        if inp == "help":
            print("COMMANDS:")
            print("- roll PARAMETER")
            print("- off")
        elif inp == "off":
            run = False
        elif inp[0:4] == "roll":
            roll(inp[5:len(inp)])
        else:
            print("SYNTAX ERROR")


if __name__ == '__main__':
    main()
