#Definizione della classe counter
class Counter:
    '''
    Ogni volta che viene chiamato un metodo il primo parametro implicito e' self
    '''
    def __init__(self, name):
        #variabili
        self.name = name
        self.x=0
        self.y=1
        # x e y sono attributi
        self.__z=2 #variabile privata
        self.num=0

    def print_attr(self):
        '''
        Funzione che stampa attributi della classe
        '''
        print("x: {}, y: {}".format(self.x, self.y))
    def increment(self):
        self.num+=1
    def decrement(self):
        self.num-=1
    def print_counter(self):
        print(self.num)

#########   Ereditarieta
class CounterExtended(Counter): #Metto tra parentesi il nome della classe padre
    def print_something_else(self):
        print(self.num)


#Esegue il codice solo se il modulo e' stato invocato esplicitamente per l'esecuzione
if __name__=="__main__":
    print("Ciao sono il modulo counter")
    c=Counter("Me")
    for _ in range(10):
        c.increment()
    for _ in range(15):
        c.decrement()
    c=CounterExtended("Always me")

    c.print_something_else()

    try:
        c=Counter("Me")
        c.print_something_else()
    except Exception as e:
        print(e)