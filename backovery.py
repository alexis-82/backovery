#!/usr/bin/env pthon3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import time
from lib import Fore, Back, Style, init

sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=40, cols=90))

subprocess.call("clear && clear", shell=True)

# nodir = open("excludes","r")
# exc = nodir.read()
# nodir.close()

init(autoreset=True)

data = (time.strftime("%d_%m_%Y"))
directory = "$(pwd)"

id1 = os.system("grep -wom1 'sudo' $HOME/.bash_history > id")
file = open("id", "r")
root1 = file.read(4 - 0)

if os.stat("id").st_size == 0:
    id2 = os.system("grep -wom1 'su' $HOME/.bash_history > id")
    file = open("id", "r")
    root2 = file.read(4 - 0)


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
        if root1 == "sudo":
            time.sleep(2)
            print()
            print("Sistema riconosciuto: ", (Fore.GREEN + Style.BRIGHT + root1))
            print()
            os.system("rm id")
            time.sleep(1)
            #os.system("mkdir Backup/backup_%s.txt 2>backup.log" % (data))
            os.system("sudo apt-mark showmanual | grep -vE 'linux-(generic|headers|image|modules)' > tmp/packages_%s.txt" % (data))
            os.system("sort tmp/packages_%s.txt -o Backup/all_packages_%s.txt" % (data, data))
            os.system("rm tmp/packages_%s.txt" % (data))
            print()
            time.sleep(1)
            input("File generato, premere un tasto per tornare indietro!")
            os.system("clear && clear")
            os.system("python3 backovery.py")
            return
        if root2 == "su":
            time.sleep(2)
            print()
            print("Sistema riconosciuto: ", (Fore.GREEN + Style.BRIGHT + root2))
            print()
            print()
            os.system("rm id")
            time.sleep(1)
            os.system("su root -c 'aapt-mark showmanual | grep -vE 'linux-(generic|headers|image|modules)' > Backup/packages_%s.txt'") % (data)
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
        if root1 == "sudo":
            time.sleep(2)
            print()
            print("Sistema riconosciuto: ", (Fore.GREEN + Style.BRIGHT + root1))
            print()
            print()
            os.system("rm id")
            time.sleep(1)
            print("PULIZIA DEL SISTEMA")
            print()
            os.system("sudo apt-get autoremove 1>backup.log && sudo apt-get clean 1>backup.log && sudo apt-get autoclean 1>backup.log")
            os.system("sudo rm -rf /tmp/*")
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
                    lista = "sudo dpkg --get-selections | grep linux-image"
                    os.system(lista)
                    print()
                    print()
                    print((Fore.RED + "ATTENZIONE - NON DISINSTALLARE IL KERNEL ATTUALMENTE IN USO"))
                    uninstall = input("Specificare il kernel da rimuovere: ")
                    command = "sudo apt-get purge %s"
                    os.system(command % (uninstall))
                    print()
                    print("PULIZIA DEL SISTEMA")
                    print()
                    os.system("sudo apt-get autoremove 1>backup.log && sudo apt-get clean 1>backup.log && sudo apt-get autoclean 1>backup.log")
                if kernel == 'no' or kernel == 'n':
                    print()
                    print()
                    print("Processo avviato...")
                    print()
                    time.sleep(2)
                    print("Esportazione del file di configurazione desktop")
                    print()
                    conf = input("Nominare il file di configurazione: (consigliato il nome del DE) ")
                    config_command = "dconf dump / > Backup/%s_%s.conf" % (conf, data)
                    subprocess.call(config_command, shell=True)
                    print()
                    # Se si vuole una minor compressione sostituire il flag -cpzf con -cpf
                    command = "sudo tar --xattrs -cpzf - --exclude-from='excludes' --one-file-system / 2>backup.log | pv -p --timer --rate --bytes > Backup/backup_%s.tgz" % (data)
                    subprocess.call(command, shell=True)
                    print()
                    print()
                    input("Backup terminato, premere un tasto per uscire!")
                    os.system("clear && clear")
                    return
        if root2 == "su":
            time.sleep(2)
            print()
            print("Sistema riconosciuto: ", (Fore.GREEN + Style.BRIGHT + root2))
            print()
            print()
            os.system("rm id")
            time.sleep(1)
            print("PULIZIA DEL SISTEMA")
            print()
            os.system("su root -c 'apt-get autoremove 1>backup.log' && su root -c 'apt-get clean 1>backup.log' && su root -c 'apt-get autoclean 1>backup.log'")
            os.system("su root -c 'rm -rf /tmp/*'")
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
                    lista = "su root -c 'dpkg --get-selections | grep linux-image'"
                    os.system(lista)
                    print()
                    print()
                    print((Fore.RED + "ATTENZIONE - NON DISINSTALLARE IL KERNEL ATTUALMENTE IN USO"))
                    uninstall = input("Specificare il kernel da rimuovere: ")
                    command = "su root -c 'apt-get purge %s'"
                    os.system(command % (uninstall))
                    print()
                    print("PULIZIA DEL SISTEMA")
                    print()
                    os.system("su root -c 'apt-get autoremove 1>backup.log' && su root -c 'apt-get clean 1>backup.log' && su root -c 'apt-get autoclean 1>backup.log'")
                if kernel == 'no' or kernel == 'n':
                    print()
                    print()
                    print("Processo avviato...")
                    print()
                    print("Esportazione del file di configurazione desktop")
                    conf = input("Nominare il file di configurazione: ")
                    config_command = "dconf dump / > Backup/%s_%s.conf" % (conf, data)
                    subprocess.call(config_command, shell=True)
                    print()
                    # Se si vuole una minor compressione sostituire il flag -cpzf con -cpf
                    command = "su root -c 'tar --xattrs -cpzf - --exclude-from='excludes' --one-file-system / 2>backup.log | pv -p --timer --rate --bytes > Backup/backup_%s.tgz'"
                    os.system(command % (data))
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
        if root1 == "sudo":
            time.sleep(2)
            print()
            print(("Sistema riconosciuto: "), (Fore.GREEN + Style.BRIGHT + root1))
            print()
            print()
            time.sleep(1)
            os.system("rm id")
            kernel = input("Vuoi rimuovere delle vecchie versioni di kernel per ottimizzare il backup? [si/no] ")
            if kernel == 'si' or kernel == 's':
                print()
                print((Fore.RED + "Kernel attualmente utilizzato:"))
                os.system("uname -r")
                print()
                print("Lista di tutti i kernel presenti nel sistema:")
                lista = "sudo dpkg --get-selections | grep linux-image"
                os.system(lista)
                print()
                print()
                print((Fore.RED + "ATTENZIONE - NON DISINSTALLARE IL KERNEL ATTUALMENTE IN USO"))
                uninstall = input("Specificare il kernel da rimuovere: ")
                command = "sudo apt-get purge %s"
                os.system(command % (uninstall))
                print()
                print("PULIZIA DEL SISTEMA")
                print()
                os.system("sudo apt-get autoremove && sudo apt-get clean && sudo apt-get autoclean")
            if kernel == 'no' or kernel == 'n':
                print()
                address = input("Digitare l'indirizzo IP di destinazione: ")
                port = input("Digitare la porta: ")
                print()
                print()
                print("Processo avviato...")
                print()
                time.sleep(1)
                command = "sudo tar -cpz --xattrs Backup/backup_%s.tgz --exclude-from='excludes' --one-file-system / 1 2>net_backup.log | pv | nc -q 0 %s %s"
                os.system(command % (data, address, port))
                print()
                print()
                input("Backup remoto terminato, premere un tasto per uscire!")
                os.system("clear && clear")
                return
        if root2 == "su":
            time.sleep(2)
            print()
            print("Sistema riconosciuto: ", (Fore.GREEN + Style.BRIGHT + root2))
            print()
            print()            
            print()
            time.sleep(1)
            os.system("rm id")
            print("PULIZIA DEL SISTEMA")
            print()
            os.system("su root -c 'apt-get autoremove' && su root -c 'apt-get clean' && su root -c 'apt-get autoclean'")
            os.system("su root -c 'rm -rf /tmp/*'")
            print()
            # Riconoscimento sistema
            print()
            print()
            print()
            time.sleep(1)
            kernel = input("Vuoi rimuovere delle vecchie versioni di kernel per ottimizzare il backup? [si/no] ")
            if kernel == 'si' or kernel == 's':
                print()
                print((Fore.RED + "Kernel attualmente utilizzato:"))
                os.system("uname -r")
                print()
                print("Lista di tutti i kernel presenti nel sistema:")
                lista = "su root -c 'dpkg --get-selections | grep linux-image'"
                os.system(lista)
                print()
                print()
                print((Fore.RED + "ATTENZIONE - NON DISINSTALLARE IL KERNEL ATTUALMENTE IN USO"))
                uninstall = input("Specificare il kernel da rimuovere: ")
                command = "su root -c 'apt-get purge %s'"
                os.system(command % (uninstall))
                print()
                print("PULIZIA DEL SISTEMA")
                print()
                os.system("su root -c 'apt-get autoremove' && su root -c 'apt-get clean' && su root -c 'apt-get autoclean'")
            if kernel == 'no' or kernel == 'n':
                print()
                address = input("Digitare l'indirizzo IP di destinazione: ")
                port = input("Digitare la porta: ")
                print()
                print()
                print("Processo avviato...")
                print()
                command = "su root -c 'tar -cpz --xattrs Backup/backup_%s.tgz --exclude-from='excludes' --one-file-system / 1 2>net_backup.log' | pv | nc -q 0 %s %s"
                os.system(command % (data, address, port))
                print()
                print()
                eval(input("Backup remoto terminato, premere un tasto per uscire!"))
                os.system("clear && clear")
                return
remote()


def recovery():
    if select == 4:
        if root1 == "sudo":
            time.sleep(2)
            print()
            print(("Sistema riconosciuto: "), (Fore.GREEN + Style.BRIGHT + root1))
            time.sleep(1)
            os.system("rm id")
            print()
            print()
            input('Trasferire il file backup e file pacchetti nella cartella ' + Fore.RED + 'Backup' + Style.RESET_ALL + ' e premere il tasto INVIO')
            print()
            os.system("sudo apt-mark showmanual > tmp/new_packages.txt")
            os.system("sort tmp/new_packages.txt -o tmp/newsystem_packages.txt")
            os.system("mv tmp/newsystem_packages.txt Backup/")
            print()
            print((Fore.MAGENTA + "Lista Backup"))
            print((Fore.MAGENTA + "------------"))
            print()
            os.system("cd Backup && ls *.tgz")
            print()
            print()
            var_backup = input("Digitare un backup presente in lista: ")
            time.sleep(2)
            print()
            print("Processo avviato...")
            print()
            command2 = "sudo pv Backup/%s | sudo tar -xpzf - -C / 2> recovery.log"
            os.system(command2 % (var_backup))
            print()
            print()
            print((Fore.MAGENTA + "Lista file pacchetti da ripristinare"))
            print((Fore.MAGENTA + "------------------------------------"))
            print()
            # qui andrebbe il nuovo codice per confrontare i due file packages
            os.system("comm -23 Backup/all_packages_%s.txt Backup/newsystem_packages.txt > Backup/packages_%s.txt" % (data, data))
            os.system("rm Backup/all_packages_%s.txt && rm Backup/newsystem_packages.txt && rm tmp/*" % (data))
            # -------------------------------------------------------------------------- #
            os.system("cd Backup && ls *.txt")
            print()
            var_list = input("Digitare la lista dei pacchetti da installare presente in lista: ")
            print()
            time.sleep(2)
            os.system("sudo apt update && sudo apt upgrade -y")
            print()
            print()
            command = "xargs sudo apt-get install --reinstall -y < Backup/%s 2>recovery.log"
            os.system(command % (var_list))
            time.sleep(2)
            print()
            print()
            print((Fore.MAGENTA + "Lista file di configurazione"))
            print((Fore.MAGENTA + "----------------------------"))
            print()
            os.system("cd Backup && ls *.conf")
            print()
            conf = input("Digitare il file per la configurazione: ")
            config_command = "dconf load / < Backup/%s" % (conf)
            subprocess.call(config_command, shell=True)
            print()
            time.sleep(2)
            print()
            print((Fore.GREEN + "Processo terminato."))
            print((Fore.RESET))
            input("Premere un tasto per uscire, potete riavviare il computer!")
            os.system("clear && clear")
            return
        if root2 == "su":
            time.sleep(2)
            print()
            print("Sistema riconosciuto: ", (Fore.GREEN + Style.BRIGHT + root2))
            print()
            print()
            input('Trasferire il file backup e file pacchetti nella cartella ' + Fore.RED + 'backup' + Style.RESET_ALL + ' e premere il tasto INVIO')
            print()
            os.system("su root -c 'apt-mark showmanual > tmp/new_packages.txt'")
            os.system("sort tmp/new_packages.txt -o tmp/newsystem_packages.txt")
            os.system("mv tmp/newsystem_packages.txt Backup/")
            print()
            print((Fore.MAGENTA + "Lista Backup"))
            print((Fore.MAGENTA + "------------"))
            print()
            print()
            os.system("cd Backup && ls *.tgz")
            print()
            var_backup = input("Digitare un backup presente in lista: ")
            time.sleep(2)
            print()
            print("Processo avviato...")
            print()
            command2 = "su root -c 'pv backup/%s | sudo tar -xpzf - -C / 2> recovery.log'"
            os.system(command2 % (var_backup))
            print()
            print()
            print((Fore.MAGENTA + "Lista file pacchetti da ripristinare"))
            print((Fore.MAGENTA + "------------------------------------"))
            print()
            # qui andrebbe il nuovo codice per confrontare i due file packages
            os.system("comm -23 Backup/all_packages_%s.txt Backup/newsystem_packages.txt > Backup/packages_%s.txt" % (data, data))
            os.system("rm Backup/all_packages_%s.txt && rm Backup/newsystem_packages.txt && rm tmp/*" % (data))
            # -------------------------------------------------------------------------- #
            os.system("cd Backup && ls *.txt")
            print()
            var_list = input("Digitare la lista dei pacchetti da installare presente in lista: ")
            print()
            time.sleep(2)
            os.system("su root -c 'apt-get update && apt-get upgrade -y'")
            print()
            # qui andrebbe il nuovo codice per confrontare i due file packages
            print()
            command = "su -c 'xargs -I {} sh -c \"apt-get install --reinstall -y {} < Backup/%s 2> recovery.log\" < Backup/%s'"
            os.system(command % (var_list, var_list))
            time.sleep(2)
            print((Fore.MAGENTA + "Lista file di configurazione"))
            print((Fore.MAGENTA + "----------------------------"))
            print()
            os.system("cd Backup && ls *.conf")
            print()
            conf = input("Digitare il file per la configurazione: ")
            config_command = "dconf load / < Backup/%s" % (conf)
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
