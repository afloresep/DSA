def random_picker(theme=None):

    llist = ['split a circular linked list in two halves', 'create the append and prepend functions for a Circular Linked Lits', 'swap nodes in a linked list', 'reverse linked list', 'count ocurrences', 'get node index', 'remove duplicates', 'merge two sorted linked lists', 'sum two linked lists numbers and return them on a new linked list ']
    stack= ['ex', 'ex1']
    themes ={'linked lists':llist, 
             'stack': stack}
    all_exercises = llist+stack

    import random
     
    if theme:
        print(random.choice(themes[theme]))
    else:
        print(random.choice(all_exercises))


if __name__=='__main__':
    random_picker('linked lists')