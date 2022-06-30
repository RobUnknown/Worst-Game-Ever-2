#choosing username
print('')
print ('???: "Greetings traveler,"')
print ('???: "What is your name?" ')
user_name = input('> ')
print('')
if 'my name is' in user_name:
    user_name = user_name.replace('my name is ','')
if 'My name is' in user_name:
    user_name = user_name.replace('My name is ', '')
if "My name's" in user_name:
    user_name = user_name.replace("My name's ", '')
if "my name's " in user_name:
    user_name = user_name.replace("my name's ",'')
if len(user_name) >= 30:
    print("???: 'You seem to be very confused.'")
    print("???: 'I'll call you Rob for now.")
    user_name = 'The default Rob'
else:
    for i in ['remember',' forgot','forgotten','memory','not sure',' know','no clue',' idea',' forget',' have one']:
        if i in user_name:
            print("???: 'You seem to be very confused.'")
            print("???: 'I'll call you Rob for now.")
            user_name = 'The default Rob'
if user_name != "The default Rob":
    print('???: "Ah,',user_name,'it is then."')
    print('???: "You seem to be confused,',user_name,'."')
print('???: "I am Henrick, and this is the land of Pythonia."')
if user_name == 'The default Rob':
    user_name = "Rob"

#defining stuff
global user_input
thin = True
inventory_open = False
def print_inventory():
    print (' _________')
    print ('|    o/   |')
    if thin == True: print ('|   /|    |')
    else: print ('|   /#    |')
    print ('|   / \   |')
    print ('|Items:   |')
    print ('|         |')
    print ('|_________|')
def is_user_trying_to_open_inv():
    if inventory_open == True:
        return False
    for i in ['inv','Inventory','inventory','open ','Inv','Open ','Backpack','backpack','backpack','show me my stuff','Show me the inventory screen. Now.','Dear computer that I hope can read this, could you please show me my inventory?','If you can read this sentence, open the inventory.','PLEASE FOR THE LOVE OF GOD JUST OPEN THE INVENTORY ALREADY PLEASE','open up sesame','open up, inventory coming through']:
        if i in user_input: return True
    for i in ['i','I']:
        if i == user_input: return True
def is_user_trying_to_close_inv():
    if inventory_open == False:
        return False
    for i in ['inv','Inv','inventory','Inventory','close','Close','stop','Stop','quit','Quit','exit','Exit',' backpack',' Backpack','stop showing me my stuff','Get this out of my face','Close the inventory screen please','Close the Inventory please','Dear Diary, today I tried to close the inventory.','close it, close it now']:
        if i in user_input: return True
    for i in ['i','I']:
        if i == user_input: return True

#explaining inventory
print("Henrick: 'Say, you don't happen to have some food on you by any chance?'")
print("-- [Open your inventory by typing 'Open Inventory' or 'Open Backpack'] --")
while True:
    user_input = input('> ')
    if is_user_trying_to_open_inv() == True:
        print_inventory()
        inventory_open = True
        print ("-- [Exit your inventory by typing 'close inventory' or 'close backpack'] --")
        while True:
            user_input = input('> ')
            if is_user_trying_to_close_inv() == True:
                inventory_open = False
                break
            print('-- [If you want to continue the story you need to do as it says] --')
        break
    print('-- [You can open your inventory by entering I, Inv, Inventory, Open Inv, Open Inventory or Open Backpack] --')

#showing character changes
print('')
print('Henrick: "Nothing, huh?"')
print('Henrick: "Well you look famished, so have some of my bread."')
print('')
print('Henrick: "There, you look better already!"')
thin = False
print('-- [Open your inventory again to see if you look less thin] --')
while True:
    user_input = input('> ')
    if is_user_trying_to_open_inv() == True:
        print_inventory()
        inventory_open = True
        break
    else: print ('- [Look just do what it says] -')
inventory_open = False
print('')
print("Henrick: 'See? you'll be back in shape for adventuring in no time!'")
print('Henrick: "Make sure to always keep a supply of food with you, eh?"')

#figure out where the user is from
print("Henrick: 'Where have you traveled from, by the way?'")
user_input = input('> ')
print('')
for i in ['remember',' forgot','forgotten','memory','not sure',' know','no clue',' idea',' forget']:
    if i in user_input:
        homeland = 'memory loss'
        break
    else: homeland = user_input
if homeland == 'memory loss':
    print('Henrick: "Memory loss? Oh dear."')
    print("Henrick: 'I've got to enlighten you then on the surrounding areas!'")
elif len(homeland) >= 25:
    print("Henrick: 'Yeesh that's a long name.")
    print("Henrick: 'Anyway, let me enlighten you on the surrounding areas.'")
else: 
    print("Henrick: '"+user_name,"of",homeland+", excellent.'")
    print("Henrick: 'Let me enlighten you on the surrounding areas,",user_name)

#talk about surroundings and begin chapter 2
print("Henrick: 'Down there to the West is Tumble Creek, a bussling village with a small river running through it.'")
print("Henrick: 'To the South the hills get a bit calmer, but I don't recommend going there, it's prime snake territory'")
print("Henrick: 'The hills keep going for a while to the East, before they eventually form into a valley.'")
print("Henrick: 'And to the North are a lot of fertile plains and forests that stretch all the way back to Tumble Creek.'")
print("Henrick: 'Come, I'll bring you down to the village.'")
print("-- [Press enter to continue] --")
input('> ')
print('')
print('')
print('')
print('')
print('')
print(" ________  ___  ___  ________  ________  __________  ________  ________         ________")
print("|\   ____\|\  \|\  \|\   __  \|\   __  \|\___   ___\|\   ____\|\   __  \       /   __   \   ")
print("\ \  \___|\ \  \ \  \ \  \|\  \ \  \|\  \|__ \  \__|\ \  \___|\ \  \|\  \     |\__\__|\  \  ")
print(" \ \  \    \ \   __  \ \   __  \ \   ____\  \ \  \   \ \   ____\ \   _  _\    \|__|  \/  /   ")
print("  \ \  \____\ \  \ \  \ \  \ \  \ \  \___|   \ \  \   \ \  \___|\ \  \\\  \|          /  /____ ")
print("   \ \_______\ \__\ \__\ \__\ \__\ \__\       \ \__\   \ \_______\ \__\\\ _\         |\_______\\")
print("    \|_______|\|__|\|__|\|__|\|__|\|__|        \|__|    \|_______|\|__|\|__|        \|_______| ")
print('')
print('')
print('-- [Press enter to continue] --')
input('> ')
                                                                                             


