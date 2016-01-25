# -*- coding: utf-8 -*-
import Queue
from threading import Thread

# stworzenie przykłądu
b = Queue.LifoQueue()
#LIFO- Last in first out; czyli liczby pokazują się od największej
#FIFO- First in first out



# Dodanie pozycji w kolejce
for i in range(0,30,5):
    #Range przyjmuje 3 argumenty z czego 2 są opcjonalne.
    #Argumentami są start, stop i step. Start rozpoczyna działanie, stop zatrzymuje a
    #Step mówi co ile będzie skakać inkrementacja lub dekrementacja for i in range (2,20,2) Wynik:2;4;6;8;10
    b.put(i) #Elementy są dodawane na koniec kolejki (get() usuwa z kolejki)
 
    
def dane_z_kolejki():
    while not b.empty(): #Sprawdzenie, czy kolejka nie jest pusta
        print b.get() #Wypisanie elementu z kolejki
        b.task_done() #Określa czy element się wykonał
        
for i in range(1): # Zasięg ilości liczb w jednej linii
    t1 = Thread(target = dane_z_kolejki)
    t1.start() # Start wątku

    
b.join() # Działa z b.task_done
         # Utrzymanie rozmiaru kolejki


