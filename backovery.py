#!/usr/bin/env pthon2
# -*- coding: utf-8 -*-
# Version Python 2.7.*

import os, sys, subprocess, time
from lib import Fore, Back, Style, init

subprocess.call("clear && clear", shell=True)

nodir = open("exclude","r")
exc = nodir.read()
nodir.close()

init(autoreset=True)

data = (time.strftime("%d_%m_%Y"))
directory = "$(pwd)"
log = os.system("grep -om1 sudo $HOME/.bash_history > id")
check = open("id", "r")
root = check.read(4 - 0)


print
print (Fore.GREEN + "   ______    ____     ____  __   ___  ____   __    __   _____ ______ __      __ ")
print (Fore.GREEN + "  (_   _ \  (    )   / ___)() ) / __)/ __ \  ) )  ( (  / ___/(   __ \) \    / ( ")
print (Fore.GREEN + "    ) (_) ) / /\ \  / /    ( (_/ /  / /  \ \( (    ) )( (__   ) (__) )\ \  / /  ")
print (Fore.GREEN + "    \   _/ ( (__) )( (     ()   (  ( ()  () )\ \  / /  ) __) (    __/  \ \/ /   ")
print (Fore.GREEN + "    /  _ \  )    ( ( (     () /\ \ ( ()  () ) \ \/ /  ( (     ) \ \  _  \  /    ")
print (Fore.GREEN + "   _) (_) )/  /\  \ \ \___ ( (  \ \ \ \__/ /   \  /    \ \___( ( \ \_))  )(     ")
print (Fore.GREEN + "  (______//__(  )__\ \____)()_)  \_\ \____/     \/      \____\)_) \__/  /__\    ")
print
print (Fore.RED + "                                  Coded by Alexis                                 ")
print (Fore.RED + "                                http://alexis82.it/                               ")
print
print

print
print "Seleziona un numero"
print
print "[1] Backup"
print "[2] Backup Remoto"
print
print "[3] Recovery"
print
print "[4] Gestore"
print
print
print "[0] Esci"
print

try:
    select = input(": ")
    if select >= 5:
        print
        print "Opzione non trovata!"
        raw_input("Premere un tasto per contiuare")
        os.system("python backovery.py")
except NameError:
    print
    print "Comando non valido!"
    raw_input("Premere un tasto per continuare")
    os.system("python backovery.py")
except SyntaxError:
    print
    print "Comando non valido!"
    raw_input("Premere un tasto per continuare")
    os.system("python backovery.py")
except UnboundLocalError:
    print "Sistema terminato"

def backup():
    if select == 1:
        print
        print "INIZIO PROCEDURA, NON INTERROMPERE..."
        print
        if root == "sudo":
            print
            print "Sistema riconosciuto: ", (Fore.GREEN + Style.BRIGHT + root)
            print
            print
            print "PULIZIA DEL SISTEMA"
            print
            os.system("sudo apt-get autoremove && sudo apt-get clean && sudo apt-get autoclean")
            os.system("sudo rm -rf /tmp/*")
            print
            while select:
                # Riconoscimento sistema
                print
                print
                print
                kernel = raw_input("Vuoi rimuovere delle vecchie versioni di kernel per ottimizzare il backup? [si/no] ")
                if kernel == 'si' or kernel == 's':
                    print
                    print (Fore.RED + "Kernel attualmente utilizzato:")
                    os.system("uname -r")
                    print
                    print "Lista di tutti i kernel presenti nel sistema:"
                    lista = "sudo dpkg --get-selections | grep linux-image"
                    os.system(lista)
                    print
                    print
                    print (Fore.RED + "ATTENZIONE - NON DISINSTALLARE IL KERNEL ATTUALMENTE IN USO")
                    uninstall = raw_input("Specificare il kernel da rimuovere: ")
                    command = "sudo apt-get purge %s"
                    os.system(command % (uninstall))
                    print
                    print "PULIZIA DEL SISTEMA"
                    print
                    os.system("sudo apt-get autoremove && sudo apt-get clean && sudo apt-get autoclean")
                if kernel == 'no' or kernel == 'n':
                    print
                    print
                    print "Processo avviato..."
                    print
                    command = "sudo tar --xattrs -cpzf - %s --one-file-system / 2>backup.log | pv -p --timer --rate --bytes > backup/backup_%s.tgz"
                    os.system(command % (exc, data))
                    print
                    print
                    raw_input("Backup terminato, premere un tasto per uscire!")
                    return
                    os.system("clear && clear")
        if root == "su":
            print
            print "Sistema riconosciuto: ", (Fore.GREEN + Style.BRIGHT + root)
            print
            print
            print "PULIZIA DEL SISTEMA"
            print
            os.system("su root -c 'apt-get autoremove' && su root -c 'apt-get clean' && su root -c 'apt-get autoclean'")
            os.system("su root -c 'rm -rf /tmp/*'")
            print
            while select:
                # Riconoscimento sistema
                print
                print
                print
                kernel = raw_input("Vuoi rimuovere delle vecchie versioni di kernel per ottimizzare il backup? [si/no] ")
                if kernel == 'si' or kernel == 's':
                    print
                    print (Fore.RED + "Kernel attualmente utilizzato:")
                    os.system("uname -r")
                    print
                    print "Lista di tutti i kernel presenti nel sistema:"
                    lista = "su root -c 'dpkg --get-selections | grep linux-image'"
                    os.system(lista)
                    print
                    print
                    print (Fore.RED + "ATTENZIONE - NON DISINSTALLARE IL KERNEL ATTUALMENTE IN USO")
                    uninstall = raw_input("Specificare il kernel da rimuovere: ")
                    command = "su root -c 'apt-get purge %s'"
                    os.system(command % (uninstall))
                    print
                    print "PULIZIA DEL SISTEMA"
                    print
                    os.system("su root -c 'apt-get autoremove' && su root -c 'apt-get clean' && su root -c 'apt-get autoclean'")
                if kernel == 'no' or kernel == 'n':
                    print
                    print
                    print "Processo avviato..."
                    print
                    command = "su root -c 'tar --xattrs -cpzf - %s --one-file-system / 2>backup.log | pv -p --timer --rate --bytes > backup/backup_%s.tgz'"
                    os.system(command % (exc, data))
                    print
                    print
                    raw_input("Backup terminato, premere un tasto per uscire!")
                    os.system("clear && clear")
                    return
backup()

def remote():
    if select == 2:
        print
        print (Fore.RED + "- !ATTENZIONE! - ")
        print (Fore.RED + "Con questo sistema potete inviare il file di backup direttamente su un altro computer o server")
        print (Fore.RED + "senza salvare alcun dato sul sistema locale!")
        print (Fore.RED + "Scompattare il file remote.tar nel server e avviatelo")
        print
        if root == "sudo":
                print
                print "Sistema riconosciuto: ", (Fore.GREEN + Style.BRIGHT + root)
                print
                print
                kernel = raw_input("Vuoi rimuovere delle vecchie versioni di kernel per ottimizzare il backup? [si/no] ")
                if kernel == 'si' or kernel == 's':
                    print
                    print (Fore.RED + "Kernel attualmente utilizzato:")
                    os.system("uname -r")
                    print
                    print "Lista di tutti i kernel presenti nel sistema:"
                    lista = "sudo dpkg --get-selections | grep linux-image"
                    os.system(lista)
                    print
                    print
                    print (Fore.RED + "ATTENZIONE - NON DISINSTALLARE IL KERNEL ATTUALMENTE IN USO")
                    uninstall = raw_input("Specificare il kernel da rimuovere: ")
                    command = "sudo apt-get purge %s"
                    os.system(command % (uninstall))
                    print
                    print "PULIZIA DEL SISTEMA"
                    print
                    os.system("sudo apt-get autoremove && sudo apt-get clean && sudo apt-get autoclean")
                if kernel == 'no' or kernel == 'n':
                    address = raw_input("Digitare l'indirizzo IP di destinazione: ")
                    port = input("Digitare la porta: ")
                    print
                    print
                    print "Processo avviato..."
                    print
                    command = "sudo tar -cvpz --xattrs backup/backup_%s.tgz %s --one-file-system / 1 2>net_backup.log | pv | nc -q 0 %s %s"
                    os.system(command % (data, exc, address, port))
                    print
                    print
                    raw_input("Backup remoto terminato, premere un tasto per uscire!")
                    os.system("clear && clear")
                    return
        if root == "su":
            print
            print "Sistema riconosciuto: ", (Fore.GREEN + Style.BRIGHT + root)
            print
            print            
            print
            print "PULIZIA DEL SISTEMA"
            print
            os.system("su root -c 'apt-get autoremove' && su root -c 'apt-get clean' && su root -c 'apt-get autoclean'")
            os.system("su root -c 'rm -rf /tmp/*'")
            print
            while select:
                # Riconoscimento sistema
                print
                print
                print
                kernel = raw_input("Vuoi rimuovere delle vecchie versioni di kernel per ottimizzare il backup? [si/no] ")
                if kernel == 'si' or kernel == 's':
                    print
                    print (Fore.RED + "Kernel attualmente utilizzato:")
                    os.system("uname -r")
                    print
                    print "Lista di tutti i kernel presenti nel sistema:"
                    lista = "su root -c 'dpkg --get-selections | grep linux-image'"
                    os.system(lista)
                    print
                    print
                    print (Fore.RED + "ATTENZIONE - NON DISINSTALLARE IL KERNEL ATTUALMENTE IN USO")
                    uninstall = raw_input("Specificare il kernel da rimuovere: ")
                    command = "su root -c 'apt-get purge %s'"
                    os.system(command % (uninstall))
                    print
                    print "PULIZIA DEL SISTEMA"
                    print
                    os.system("su root -c 'apt-get autoremove' && su root -c 'apt-get clean' && su root -c 'apt-get autoclean'")
                if kernel == 'no' or kernel == 'n':
                  address = raw_input("Digitare l'indirizzo IP di destinazione: ")
                  port = input("Digitare la porta: ")
                  print
                  print
                  print "Processo avviato..."
                  print
                  command = "su root -c 'tar --xattrs -cvpz backup/backup_%s.tgz %s --one-file-system / 1 2>net_backup.log | pv | nc -q 0 %s %s'"
                  os.system(command % (data, exc, address, port))
                  print
                  print
                  raw_input("Backup remoto terminato, premere un tasto per uscire!")
                  os.system("clear && clear")
                  return
remote()

def recovery():
    if select == 3:
        if root == "sudo":
            print
            print (Fore.MAGENTA + "Montare Unità")
            print (Fore.MAGENTA + "-------------")
            print
            print
            subprocess.call("lsblk", shell=True)
            print
            partition = raw_input("Quale partizione vuoi ripristinare? (es. sda1) ")
            fsck = "sudo fsck -y /dev/%s"
            os.system(fsck % (partition))
            mount = "sudo mount -t auto /dev/%s /mnt"
            os.system(mount % (partition))
            subprocess.call("sudo chown user.user /mnt", shell=True)
            subprocess.call("mkdir /mnt/backup", shell=True)
            print
            print
            raw_input("Trasferire il file di backup nella cartella /mnt/backup e premere il tasto INVIO")
            print
            print (Fore.MAGENTA + "Lista Backup")
            print (Fore.MAGENTA + "------------")
            print
            print
            os.system("cd /mnt/backup && ls *.tgz")
            print
            var = raw_input("Digitare un backup presente in lista: ")
            time.sleep(2)
            print
            print "Processo avviato..."
            print
            command = "sudo tar -xpzf /mnt/backup/%s -C /mnt --numeric-owner --checkpoint=.1000 2>recovery.log"
            os.system(command % (var))
            subprocess.call("sudo rm -rf /mnt/backup", shell=True)
            subprocess.call("cd /", shell=True)
            subprocess.call("sudo umount /mnt", shell=True)
            print
            print (Fore.GREEN + "Processo terminato.")
            print (Fore.RESET)
            raw_input("Premere un tasto per uscire, potete riavviare il computer!")
            os.system("clear && clear")
            return
        if root == "su":
            print
            print (Fore.MAGENTA + "Montare Unità")
            print (Fore.MAGENTA + "-------------")
            print
            print
            subprocess.call("lsblk", shell=True)
            print
            partition = raw_input("Quale partizione vuoi ripristinare? (es. sda1) ")
            fsck = "su root -c 'fsck -y /dev/%s'"
            os.system(fsck % (partition))
            mount = "su root -c 'mount -t auto /dev/%s /mnt'"
            os.system(mount % (partition))
            subprocess.call("su root -c 'chown user.user /mnt'", shell=True)
            subprocess.call("mkdir /mnt/backup", shell=True)
            print
            print
            raw_input("Trasferire il file di backup nella cartella /mnt/backup e premere il tasto INVIO")
            print
            print (Fore.MAGENTA + "Lista Backup")
            print (Fore.MAGENTA + "------------")
            print
            print
            os.system("cd /mnt/backup && ls *.tgz")
            print
            var = raw_input("Digitare un backup presente in lista: ")
            time.sleep(2)
            print
            print "Processo avviato..."
            print
            command = "su root -c 'tar -xpzf /mnt/backup/%s -C /mnt --numeric-owner --checkpoint=.1000 2>recovery.log'"
            os.system(command % (var))
            subprocess.call("su root -c 'rm -rf /mnt/backup'", shell=True)
            subprocess.call("cd /", shell=True)
            subprocess.call("su root -c 'umount /mnt'", shell=True)
            print
            print (Fore.GREEN + "Processo terminato.")
            print (Fore.RESET)
            raw_input("Premere un tasto per uscire, potete riavviare il computer!")
            os.system("clear && clear")
            return
recovery()

def manager():
    os.system("clear && clear")
    if select == 4:
        print
        print (Fore.GREEN + "   ______    ____     ____  __   ___  ____   __    __   _____ ______ __      __ ")
        print (Fore.GREEN + "  (_   _ \  (    )   / ___)() ) / __)/ __ \  ) )  ( (  / ___/(   __ \) \    / ( ")
        print (Fore.GREEN + "    ) (_) ) / /\ \  / /    ( (_/ /  / /  \ \( (    ) )( (__   ) (__) )\ \  / /  ")
        print (Fore.GREEN + "    \   _/ ( (__) )( (     ()   (  ( ()  () )\ \  / /  ) __) (    __/  \ \/ /   ")
        print (Fore.GREEN + "    /  _ \  )    ( ( (     () /\ \ ( ()  () ) \ \/ /  ( (     ) \ \  _  \  /    ")
        print (Fore.GREEN + "   _) (_) )/  /\  \ \ \___ ( (  \ \ \ \__/ /   \  /    \ \___( ( \ \_))  )(     ")
        print (Fore.GREEN + "  (______//__(  )__\ \____)()_)  \_\ \____/     \/      \____\)_) \__/  /__\    ")
        print
        print (Fore.RED + "                                  Coded by Alexis                                 ")
        print (Fore.RED + "                                http://alexis82.it/                               ")
        print
        print
        print
        print "[1] Dividere"
        print "[2] Unire"
        print
        print
        print "[0] Indietro"
        print
        try:
            select2 = input("Scegliere un opzione: ")
            if select2 >= 3:
                print "Opzione non trovata"
                raw_input("Premere un tasto per continuare")
                os.system("python backovery.py")
        except NameError:
            print "Comando non valido"
            raw_input("Premere un tasto per continuare")
            os.system("python backovery.py")
        except SyntaxError:
            print "Comando non valido"
            raw_input("Premere un tasto per continuare")
            os.system("python backovery.py")
        except UnboundLocalError:
            print "Sistema terminato"
        if select2 == 1:
            print
            print
            print "Lista Backup"
            print "------------"
            os.system("cd backup && ls *.tgz")
            print
            file_tgz = raw_input("Digitare il backup da splittare: ")
            split = raw_input("Dimensioni? [DvD - CD] ")
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
                    print
                    print "Operazione terminata"
                    raw_input("Premere un tasto per uscire")
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
                    print
                    print "Operazione terminata"
                    raw_input("Premere un tasto per uscire")
                    os.system("clear && clear")
                    return
            else:
                print "Opzione non trovata!"
                raw_input("Premere un tasto per continuare")
                os.system("python backovery.py")
        if select2 == 2:
            print
            print
            print "Lista Backup da unificare"
            print "-------------------------"
            print
            os.chdir('backup/split')
            command = "ls -1 | sed -e 's/\..*$//' | sed -n 1p"
            os.system(command)
            print
            select_file = raw_input("Digitare il backup da unire: ")
            command = "cat %s.* > %s.tgz"
            os.system(command % (select_file, select_file))
            command_2 = "mv %s.tgz ../"
            os.system(command_2 % (select_file))
            print
            print "Completato"
            print
            os.system("python ../../backovery.py")
        if select2 == 0:
            os.system("python backovery.py")
manager()

def close():
    if select == 0:
        subprocess.call("clear", shell=True)
        return
close()


