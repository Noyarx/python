import os
import time
# os.system('clear') serve a ripulire il prompt
# time.sleep(n) serve ad attendere alcuni secondi prima di proseguire 

def menu():       # MENU DI SCELTA OPERAZIONE
	print("BENVENUTO NEL BEST PROGRAMMA EVER!\n1. Apri il generatore di wordlist\n2. Unisci due wordlist\n3. cattivo\n4. Esci dal programma.")
	choice= input("Scegli cosa fare:  ")
	if choice== '1':
		os.system('clear')
		generatore()
		input("Premi Invio per tornare al menu..\n")
		print("Ritorno al menu ...\n")
		time.sleep(1)
		os.system('clear')
		menu()
	elif choice== '2':
		os.system('clear')
		unisciWordlist()
		input("Premi Invio per tornare al menu..\n")
		print("Ritorno al menu ...\n")
		time.sleep(1)
		os.system('clear')
		menu()
	elif choice== '3':
		os.system('clear')
		cattivo()
		time.sleep(0.5)
		print("Ritorno al menu ...\n")
		time.sleep(0.5)
		os.system('clear')
		menu()
	elif choice== '4':
		os.system('clear')
		print("Grazie per aver usato il nostro programma!\n")
		time.sleep(0.5)
		print("Chiudo il programma...\n")
		time.sleep(0.6)
		os.system('clear')
		exit()
	else:
		os.system('clear')
		print("\nInserisci una risposta valida!\n")
		time.sleep(0.5)
		print("Ritorno al menu ...\n")
		time.sleep(0.5)
		os.system('clear')
		menu()

def generatore(): #GENERATORE WORDLIST
	print("\nGenera una wordlist che combini le parole della prima con quelle della seconda wordlist.\n")
	f1 = open(input("Inserisci la prima wordlist:  ").strip()+".txt", "r+")                                 #inserimento 1 wordlist
	f2 = open(input("Inserisci la seconda wordlist:  ").strip()+".txt", "r+")                               #inserimento 2 wordlist
	f3 = open(input("Inserisci il nome del nuovo file:  ").strip()+".txt", "a")                             #inserimento wordlist risultato
	a= ""
	count= 0

	for line1 in f1:                                                                                        #legge la prima wordlist
		for line2 in f2:                                                                                #legge la seconda wordlist
			a= (line1.replace('\n','')+line2)                                                       #elimina lo \n dalla prima parola
			print(a)                                                                                #stampa la parola appena generata
			f3.write(a.replace(a[0],a[0].upper()))                                                  #scrivi parola in upperCase
			f3.write(a.replace(a[0],a[0].lower()))                                                  #scrivi parola in lowerCase
			count= count+2                                                                          #contatore delle parole generate
		
		f2.seek(0,0)                                                                                    #riporta il puntatore all'inizio del file2
		os.system('clear')
		print ("\n---- LA TUA WORDLIST E' STATA GENERATA ----\nParole generate: "+str(count)+'\n')	#stampa il contatore


	f1.close()                                                                                              #chiusura dei file
	f2.close()                                                                                              #chiusura dei file
	f3.close()                                                                                              #chiusura dei file

		
def unisciWordlist():
	print("Genera una nuova wordlist che contenga le parole della prima e della seconda wordlist.\n")
	f1 = open(input("Inserisci la prima wordlist:  ").strip()+".txt", "r+")                                 #inserimento 1 wordlist
	f2 = open(input("Inserisci la seconda wordlist:  ").strip()+".txt", "r+")                               #inserimento 2 wordlist
	f3 = open(input("Inserisci il nome del nuovo file:  ").strip()+".txt", "a")                             #inserimento wordlist risultato
	
	for line in f1:
		f3.write(line)
	for line2 in f2:
		f3.write(line2)
	
	print("\n ---- LA NUOVA WORDLIST E' STATA GENERATA UNENDO LE PRIME DUE ----\n")
	f1.close()                                                                                              #chiusura dei file
	f2.close()                                                                                              #chiusura dei file
	f3.close()                                                                                              #chiusura dei file

def cattivo():
	print("\nSei cattivo.\n")

#main:
os.system('clear')
menu()