stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    # your code goes here
    ttl = 0
    print('Inventory:')
    lst = list(inventory.keys())
    lst.sort()
    for key in lst:
        print(inventory[key], key)
        ttl += inventory[key]

    print('Total number of items:',str(ttl))

if __name__ == "__main__":
    displayInventory(stuff)
