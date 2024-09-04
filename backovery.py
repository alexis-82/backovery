#!/usr/bin/env pthon3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import time
from lib import Fore, Back, Style, init

if os.geteuid() != 0:
    print("Questo script deve essere eseguito come root.")
    sys.exit(1)

sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=40, cols=90))

subprocess.call("clear && clear", shell=True)

# nodir = open("excludes","r")
# exc = nodir.read()
# nodir.close()

init(autoreset=True)

data = (time.strftime("%d_%m_%Y"))
directory = "$(pwd)"

print()
print((Fore.GREEN + "   ______    ____     ____  __   ___  ____   __    __   _____ ______ __      __ "))
print((Fore.GREEN + "  (_   _ \  (    )   / ___)() ) / __)/ __ \  ) )  ( (  / ___/(   __ \) \    / ( "))
print((Fore.GREEN + "    ) (_) ) / /\ \  / /    ( (_/ /  / /  \ \( (    ) )( (__   ) (__) )\ \  / /  "))
print((Fore.GREEN + "    \   _/ ( (__) )( (     ()   (  ( ()  () )\ \  / /  ) __) (    __/  \ \/ /   "))
print((Fore.GREEN + "    /  _ \  )    ( ( (     () /\ \ ( ()  () ) \ \/ /  ( (     ) \ \  _  \  /    "))
print((Fore.GREEN + "   _) (_) )/  /\  \ \ \___ ( (  \ \ \ \__/ /   \  /    \ \___( ( \ \_))  )(     "))
print((Fore.GREEN + "  (______//__(  )__\ \____)()_)  \_\ \____/     \/      \____\)_) \__/  /__\    "))
print()
print((Fore.RED + "                                  Coded by Alexis                                 "))
print((Fore.RED + "                                https://alexis82.it/                              "))
print()
print()

print()
print("Seleziona un numero")
print()
print("[1] Esporta pacchetti")
print()
print("[2] Backup")
print("[3] Backup Remoto")
print()
print("[4] Recovery")
print()
print("[5] Gestore")
print()
print()
print("[0] Esci")
print()

try:
    select = eval(input(": "))
    if select >= 6:
        print()
        print("Opzione non trovata!")
        input("Premere un tasto per contiuare")
        os.system("python3 backovery.py")
except NameError:
    print()
    print("Comando non valido!")
    input("Premere un tasto per continuare")
    os.system("python3 backovery.py")
except SyntaxError:
    print()
    print("Comando non valido!")
    input("Premere un tasto per continuare")
    os.system("python3 backovery.py")
except UnboundLocalError:
    print("Sistema terminato")


def esporta():
    if select == 1:
        time.sleep(2)
        print()
        print("INIZIO PROCEDURA, NON INTERROMPERE...")
        print()
        time.sleep(2)
        # Scelta della destinazione del file di esportazione
        print("Scegli la destinazione del file di esportazione:")
        print()
        print("1. Cartella predefinita (Backup)")
        print("2. Altra cartella")
        print()
        scelta = input("Inserisci il numero della scelta: ")
        if scelta == "1":
            destinazione = "Backup"
        elif scelta == "2":
            destinazione = input("Inserisci il percorso della cartella di destinazione: ")
        else:
            print("Scelta non valida. Utilizzo cartella predefinita.")
            destinazione = "Backup"
        os.system("apt-mark showmanual | grep -vE 'linux-(generic|headers|image|modules)' > %s/packages_%s.txt" % (destinazione, data))
        os.system("sort %s/packages_%s.txt -o %s/all_packages_%s.txt" % (destinazione, data, destinazione, data))
        os.system("rm %s/packages_%s.txt" % (destinazione, data))
        print()
        time.sleep(1)
        input("File generato, premere un tasto per tornare indietro!")
        os.system("clear && clear")
        os.system("python3 backovery.py")
        return
esporta()

def stampa_avanzamento(passi):
    contatore = 0
    while contatore < passi:
        print(f"\r[{'#' * contatore}{'.' * (passi - contatore)}] {contatore}/{passi}", end="", flush=True)
        contatore += 1
        time.sleep(0.3)
    print("\r[" + "#" * passi + "] Operazione completata!")

def backup():
    if select == 2:
        time.sleep(2)
        print()
        print("INIZIO PROCEDURA, NON INTERROMPERE...")
        print()
        time.sleep(1)
        print("PULIZIA DEL SISTEMA")
        print()
        os.system("apt-get autoremove 1>backup.log && apt-get clean 1>backup.log && apt-get autoclean 1>backup.log")
        os.system("rm -rf /tmp/*")
        os.system("rm -rf ~/.local/share/Trash/files/*")
        print()
        # Stampa della barra di avanzamento per la pulizia del sistema
        passi = 10
        stampa_avanzamento(passi)
        print()
        time.sleep(1)
        while select:
            # Riconoscimento sistema
            print()
            print()
            print()
            kernel = input("Vuoi rimuovere delle vecchie versioni di kernel per ottimizzare il backup? [si/no] ")
            if kernel == 'si' or kernel == 's':
                print()
                print((Fore.RED + "Kernel attualmente utilizzato:"))
                os.system("uname -r")
                print()
                print("Lista di tutti i kernel presenti nel sistema:")
                lista = "dpkg --get-selections | grep linux-image"
                os.system(lista)
                print()
                print()
                print((Fore.RED + "ATTENZIONE - NON DISINSTALLARE IL KERNEL ATTUALMENTE IN USO"))
                uninstall = input("Specificare il kernel da rimuovere: ")
                command = "apt-get purge %s"
                os.system(command % (uninstall))
                print()
                print("PULIZIA DEL SISTEMA")
                print()
                os.system("apt-get autoremove 1>backup.log && apt-get clean 1>backup.log && apt-get autoclean 1>backup.log")
            if kernel == 'no' or kernel == 'n':
                print()
                print()
                print("Processo avviato...")
                print()
                time.sleep(2)
                print("Esportazione del file di configurazione desktop")
                print()
                conf = input("Nominare il file di configurazione: (consigliato il nome del DE) ")
                print()
                time.sleep(1)
                # Scelta della destinazione del file di configurazione
                print("Scegli la destinazione del file di configurazione:")
                print()
                print("1. Cartella predefinita (Backup)")
                print("2. Altra cartella")
                print()
                scelta = input("Inserisci il numero della scelta: ")
                if scelta == "1":
                    destinazione = "Backup"
                elif scelta == "2":
                    destinazione = input("Inserisci il percorso della cartella di destinazione: ")
                else:
                    print("Scelta non valida. Utilizzo cartella predefinita.")
                    destinazione = "Backup"
                config_command = "dconf dump / > %s/%s_%s.conf" % (destinazione, conf, data)
                subprocess.call(config_command, shell=True)
                print()
                time.sleep(2)
                # Scelta della destinazione del file di backup
                print("Scegli la destinazione del file di backup:")
                print()
                print("1. Cartella predefinita (Backup)")
                print("2. Altra cartella")
                print()
                scelta = input("Inserisci il numero della scelta: ")
                if scelta == "1":
                    destinazione = "Backup"
                elif scelta == "2":
                    destinazione = input("Inserisci il percorso della cartella di destinazione: ")
                else:
                    print("Scelta non valida. Utilizzo cartella predefinita.")
                    destinazione = "Backup"
                print()
                time.sleep(1)
                # Se si vuole una minor compressione sostituire il flag -cpzf con -cpf
                command = "tar --xattrs -cpzf - --exclude-from='excludes' --one-file-system / 2>backup.log | pv -p --timer --rate --bytes > %s/backup_%s.tgz" % (destinazione, data)
                subprocess.call(command, shell=True)
                print()
                print()
                input("Backup terminato, premere un tasto per uscire!")
                os.system("clear && clear")
                return
backup()


def remote():
    if select == 3:
        print()
        print((Fore.RED + "                                    - !ATTENZIONE! -                                   "))
        print((Fore.RED + "Con questo sistema potete inviare il file di backup direttamente su un altro computer o server"))
        print((Fore.RED + "senza salvare alcun dato sul sistema locale!"))
        print((Fore.RED + "Scompattare il file remote.tar nel server e avviatelo"))
        print()
        time.sleep(2)
        print()
        kernel = input("Vuoi rimuovere delle vecchie versioni di kernel per ottimizzare il backup? [si/no] ")
        if kernel == 'si' or kernel == 's':
            print()
            print((Fore.RED + "Kernel attualmente utilizzato:"))
            os.system("uname -r")
            print()
            print("Lista di tutti i kernel presenti nel sistema:")
            lista = "dpkg --get-selections | grep linux-image"
            os.system(lista)
            print()
            print()
            print((Fore.RED + "ATTENZIONE - NON DISINSTALLARE IL KERNEL ATTUALMENTE IN USO"))
            uninstall = input("Specificare il kernel da rimuovere: ")
            command = "apt-get purge %s"
            os.system(command % (uninstall))
            print()
            print("PULIZIA DEL SISTEMA")
            print()
            os.system("apt-get autoremove && apt-get clean && apt-get autoclean")
        if kernel == 'no' or kernel == 'n':
            print()
            address = input("Digitare l'indirizzo IP di destinazione: ")
            port = input("Digitare la porta: ")
            print()
            print()
            print("Processo avviato...")
            print()
            time.sleep(1)
            command = "tar -cpz --xattrs Backup/backup_%s.tgz --exclude-from='excludes' --one-file-system / 1 2>net_backup.log | pv | nc -q 0 %s %s"
            os.system(command % (data, address, port))
            print()
            print()
            input("Backup remoto terminato, premere un tasto per uscire!")
            os.system("clear && clear")
            return
remote()


def recovery():
    if select == 4:
        time.sleep(2)
        print()
        # Scelta della destinazione dei file di backup e pacchetti
        print("Scegli la destinazione dei file di backup e pacchetti:")
        print()
        print("1. Cartella predefinita (Backup)")
        print("2. Altra cartella")
        print()
        scelta = input("Inserisci il numero della scelta: ")
        if scelta == "1":
            destinazione = "Backup"
        elif scelta == "2":
            destinazione = input("Inserisci il percorso della cartella di destinazione: ")
        else:
            print("Scelta non valida. Utilizzo cartella predefinita.")
            destinazione = "Backup"
        print()
        input('Trasferire il file backup e file pacchetti nella cartella '+ Fore.RED + destinazione + Style.RESET_ALL +' e premere il tasto INVIO')
        print()
        os.system("apt-mark showmanual > tmp/new_packages.txt")
        os.system("sort tmp/new_packages.txt -o tmp/newsystem_packages.txt")
        os.system("mv tmp/newsystem_packages.txt %s/" % (destinazione))
        os.system("rm tmp/new_packages.txt")
        print()
        print((Fore.MAGENTA + "Lista Backup"))
        print((Fore.MAGENTA + "------------"))
        print()
        os.system("cd %s && ls *.tgz" % destinazione)
        print()
        print()
        var_backup = input("Digitare un backup presente in lista: ")
        time.sleep(2)
        print()
        print("Processo avviato...")
        print()
        command2 = "pv %s/%s | tar -xpzf - -C / 2> recovery.log" % (destinazione, var_backup)
        os.system(command2)
        print()
        print()
        print((Fore.MAGENTA + "Lista file pacchetti da ripristinare"))
        print((Fore.MAGENTA + "------------------------------------"))
        print()
        # qui andrebbe il nuovo codice per confrontare i due file packages
        os.system("comm -23 %s/all_packages_%s.txt %s/newsystem_packages.txt > %s/packages_%s.txt" % (destinazione, data, destinazione, destinazione, data))
        os.system("rm %s/all_packages_%s.txt && rm %s/newsystem_packages.txt && rm tmp/*" % (destinazione, data, destinazione))
        # -------------------------------------------------------------------------- #
        # Scelta della destinazione del file di pacchetti
        print("Scegli la destinazione del file di pacchetti:")
        print()
        print("1. Cartella predefinita (Backup)")
        print("2. Altra cartella")
        print()
        scelta_pacchetti = input("Inserisci il numero della scelta: ")
        if scelta_pacchetti == "1":
            destinazione_pacchetti = "Backup"
        elif scelta_pacchetti == "2":
            destinazione_pacchetti = input("Inserisci il percorso della cartella di destinazione: ")
        else:
            print("Scelta non valida. Utilizzo cartella predefinita.")
            destinazione_pacchetti = "Backup"
        os.system("cd %s && ls *.txt" % destinazione)
        print()
        var_list = input("Digitare la lista dei pacchetti da installare presente in lista: ")
        print()
        time.sleep(2)
        os.system("apt update && apt upgrade -y")
        print()
        print()
        command = "xargs apt-get install --reinstall -y < %s/%s 2>recovery.log" % (destinazione_pacchetti, var_list)
        os.system(command)
        time.sleep(2)
        print()
        print()
        # Scelta della destinazione del file di configurazione
        print("Scegli la destinazione del file di configurazione:")
        print()
        print("1. Cartella predefinita (Backup)")
        print("2. Altra cartella")
        print()
        scelta_config = input("Inserisci il numero della scelta: ")
        if scelta_config == "1":
            destinazione_config = "Backup"
        elif scelta_config == "2":
            destinazione_config = input("Inserisci il percorso della cartella di destinazione: ")
        else:
            print("Scelta non valida. Utilizzo cartella predefinita.")
            destinazione_config = "Backup"
        print((Fore.MAGENTA + "Lista file di configurazione"))
        print((Fore.MAGENTA + "----------------------------"))
        print()
        os.system("cd %s && ls *.conf" % destinazione_config)
        print()
        conf = input("Digitare il file per la configurazione: ")
        config_command = "dconf load / < %s/%s" % (destinazione_config, conf)
        subprocess.call(config_command, shell=True)
        print()
        time.sleep(2)
        print()
        print((Fore.GREEN + "Processo terminato."))
        print((Fore.RESET))
        input("Premere un tasto per uscire, potete riavviare il computer!")
        os.system("clear && clear")
        return
recovery()

def manager():
    os.system("clear && clear")
    if select == 5:
        print()
        print((Fore.GREEN + "   ______    ____     ____  __   ___  ____   __    __   _____ ______ __      __ "))
        print((Fore.GREEN + "  (_   _ \  (    )   / ___)() ) / __)/ __ \  ) )  ( (  / ___/(   __ \) \    / ( "))
        print((Fore.GREEN + "    ) (_) ) / /\ \  / /    ( (_/ /  / /  \ \( (    ) )( (__   ) (__) )\ \  / /  "))
        print((Fore.GREEN + "    \   _/ ( (__) )( (     ()   (  ( ()  () )\ \  / /  ) __) (    __/  \ \/ /   "))
        print((Fore.GREEN + "    /  _ \  )    ( ( (     () /\ \ ( ()  () ) \ \/ /  ( (     ) \ \  _  \  /    "))
        print((Fore.GREEN + "   _) (_) )/  /\  \ \ \___ ( (  \ \ \ \__/ /   \  /    \ \___( ( \ \_))  )(     "))
        print((Fore.GREEN + "  (______//__(  )__\ \____)()_)  \_\ \____/     \/      \____\)_) \__/  /__\    "))
        print()
        print((Fore.RED + "                                  Coded by Alexis                                 "))
        print((Fore.RED + "                                https://alexis82.it/                              "))
        print()
        print()
        print()
        print("[1] Dividere")
        print("[2] Unire")
        print()
        print()
        print("[0] Indietro")
        print()
        
        try:
            select2 = eval(input("Scegliere un opzione: "))
            if select2 >= 3:
                print("Opzione non trovata")
                input("Premere un tasto per continuare")
                os.system("python3 backovery.py")
        except NameError:
            print("Comando non valido")
            input("Premere un tasto per continuare")
            os.system("python3 backovery.py")
        except SyntaxError:
            print("Comando non valido")
            input("Premere un tasto per continuare")
            os.system("python3 backovery.py")
        except UnboundLocalError:
            print("Sistema terminato")
        
        if select2 == 1:
            print()
            print()
            print("Lista Backup")
            print("------------")
            os.system("cd backup && ls *.tgz")
            print()
            file_tgz = input("Digitare il backup da splittare: ")
            split = input("Dimensioni? [DvD - CD] ")
            if split == 'dvd':
                os.chdir('backup')
                size = os.path.getsize(file_tgz)
                # Impostato per DvD a 4Gb
                byte = 4294967296
                check_dir = os.path.exists("split")
                if check_dir is False:
                    os.system("mkdir split")
                if size > byte:
                    command = "split -b %s -d --suffix-length=2 %s %s."
                    os.system(command % (byte, file_tgz, file_tgz))
                    command_2 = "mv %s.*  split/"
                    os.system(command_2 % (file_tgz))
                    print()
                    print("Operazione terminata")
                    input("Premere un tasto per uscire")
                    os.system("clear && clear")
                    return
            if split == 'cd':
                os.chdir('backup')
                size = os.path.getsize(file_tgz)
                # Impostato per CD a 650Mb
                byte = 681574400
                check_dir = os.path.exists("split")
                if check_dir is False:
                    os.system("mkdir split")
                if size > byte:
                    command = "split -b %s -d --suffix-length=2 %s %s."
                    os.system(command % (byte, file_tgz, file_tgz))
                    command_2 = "mv %s.*  split/"
                    os.system(command_2 % (file_tgz))
                    print()
                    print("Operazione terminata")
                    input("Premere un tasto per uscire")
                    os.system("clear && clear")
                    return
            else:
                print("Opzione non trovata!")
                input("Premere un tasto per continuare")
                os.system("python3 backovery.py")
        if select2 == 2:
            print()
            print()
            print("Lista Backup da unificare")
            print("-------------------------")
            print()
            os.chdir('backup/split')
            command = "ls -1 | sed -e 's/\..*$//' | sed -n 1p"
            os.system(command)
            print()
            select_file = input("Digitare il backup da unire: ")
            command = "cat %s.* > %s.tgz"
            os.system(command % (select_file, select_file))
            command_2 = "mv %s.tgz ../"
            os.system(command_2 % (select_file))
            print()
            print("Completato")
            print()
            os.system("python3 ../../backovery.py")
        if select2 == 0:
            os.system("python3 backovery.py")
manager()

def close():
    if select == 0:
        os.system("rm id")
        subprocess.call("clear", shell=True)
        return
close()
