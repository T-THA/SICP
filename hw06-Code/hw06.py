""" Homework 6: OOP and Inheritance"""

#####################
# Required Problems #
#####################

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.add_funds(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self, food, price):
        self.balance=0
        self.number=0
        self.food=food
        self.price=price
    def vend(self):
        if self.number==0:
            return 'Machine is out of stock.'
        else:
            if self.balance<self.price:
                return 'You must add $'+str(self.price-self.balance)+' more funds.'
            elif self.balance==self.price:
                self.balance=0
                self.number-=1
                return 'Here is your '+self.food+'.'
            else:
                self.number-=1
                tmp=self.balance
                self.balance=0
                return 'Here is your '+self.food+' and $'+str(tmp-self.price)+' change.'
    def restock(self,add_number):
        self.number+=add_number
        return 'Current '+self.food+' stock: '+str(self.number)
    def add_funds(self,add_balance):
        if self.number==0:
            return 'Machine is out of stock. Here is your $'+str(add_balance)+'.'
        else:
            self.balance+=add_balance
            return 'Current balance: $'+str(self.balance)


class Pet:
    """A pet.

    >>> kyubey = Pet('Kyubey', 'Incubator')
    >>> kyubey.talk()
    Kyubey
    >>> kyubey.eat('Grief Seed')
    Kyubey ate a Grief Seed!
    """
    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner
    
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    
    def talk(self):
        print(self.name)


class Cat(Pet):
    """A cat.

    >>> vanilla = Cat('Vanilla', 'Minazuki Kashou')
    >>> isinstance(vanilla, Pet) # check if vanilla is an instance of Pet.
    True
    >>> vanilla.talk()
    Vanilla says meow!
    >>> vanilla.eat('fish')
    Vanilla ate a fish!
    >>> vanilla.lose_life()
    >>> vanilla.lives
    8
    >>> vanilla.is_alive
    True
    >>> for i in range(8):
    ...     vanilla.lose_life()
    >>> vanilla.lives
    0
    >>> vanilla.is_alive
    False
    >>> vanilla.lose_life()
    Vanilla has no more lives to lose.
    """
    def __init__(self, name, owner, lives=9):
        self.lives=lives
        Pet.__init__(self,name,owner)

    def talk(self):
        """ Print out a cat's greeting.
        """
        if self.lives>0:
            print(self.name+' says meow!')
            

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero, 'is_alive'
        becomes False. If this is called after lives has reached zero, print out
        that the cat has no more lives to lose.
        """
        if self.lives>=0:
            self.lives-=1
        if self.lives==0:
            self.is_alive = False
        if self.lives<0:
            print('{0} has no more lives to lose.'.format(self.name))


class NoisyCat(Cat): # Dose this line need to change?
    """A Cat that repeats things twice.

    >>> chocola = NoisyCat('Chocola', 'Minazuki Kashou')
    >>> isinstance(chocola, Cat) # check if chocola is an instance of Cat.
    True
    >>> chocola.talk()
    Chocola says meow!
    Chocola says meow!
    """
    def __init__(self, name, owner, lives=9):
        # Is this method necessary? If not, feel free to remove it.
        Cat.__init__(self, name, owner, lives)
    
    def talk(self):
        """Talks twice as much as a regular cat.
        """
        Cat.talk(self)
        Cat.talk(self)


##########################
# Just for fun Questions #
##########################

class Fib:
    """A Fibonacci number.

    >>> start = Fib()
    >>> start.value
    0
    >>> start.next().value
    1
    >>> start.next().next().value
    1
    >>> start.next().next().next().value
    2
    >>> start.next().next().next().next().value
    3
    >>> start.next().next().next().next().next().value
    5
    >>> start.next().next().next().next().next().next().value
    8
    >>> start.value # Ensure start isn't changed
    0
    """

    def __init__(self, value=0):
        self.value = value

    def next(self):
        "*** YOUR CODE HERE ***"
