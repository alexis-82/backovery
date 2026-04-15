#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import time
from lib import Fore, Back, Style, init
#import pwd
import logging

logging.basicConfig(
  filename="backovery.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

if os.geteuid() != 0:
    print("Questo script deve essere eseguito come root.")
    sys.exit(1)

sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=40, cols=90))

subprocess.call("clear && clear", shell=True)

# Sistema di riconoscimento del path all'interno del file excludes
# Definisci il percorso del file di esclusione
exclude_file = 'excludes'

# Ottieni il percorso della cartella corrente
current_dir = os.getcwd()

# Verifica se il path è già presente nel file di esclusione
with open(exclude_file, 'r') as f:
    exclude_paths = f.readlines()

# Verifica se il path è già presente nel file di esclusione
if current_dir + '\n' not in exclude_paths:
    # Aggiungi il path al file di esclusione
    with open(exclude_file, 'a') as f:
        f.write(current_dir + '\n')

# nodir = open("excludes","r")
# exc = nodir.read()
# nodir.close()

init(autoreset=True)

data = (time.strftime("%d_%m_%Y"))
#directory = "$(pwd)"
directory = os.getcwd()

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

def mostra_menu():
    print()
    print("Seleziona un numero")
    print()
    print("[1] Esporta pacchetti e configurazioni")
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

def main():
      while True:
        mostra_menu()
        try:
          scelta = int(input(": ").strip())
        except ValueError:
          print("Inserire un numero valido.")
          continue

        if scelta == 0:
            break
        elif scelta == 1:
          esporta()
        elif scelta == 2:
            backup()
        elif scelta == 3:
            remote()
        elif scelta == 4:
            recovery()
        elif scelta == 5:
            manager()
        else:
            print("Opzione non trovata.")


def esporta(scelta):
    if scelta == 1:
        time.sleep(2)
        print()
        print("INIZIO PROCEDURA, NON INTERROMPERE...")
        print()
        time.sleep(2)

        print("Esportazione del file di configurazione desktop")
        print()
        TMP_DIR = os.environ.get('TMP_DIR', 'tmp')
        # esegui il dump di dconf
        utente = input("Inserisci l'username per eseguire il dump di dconf: ")
        #subprocess.run(f"runuser -u {utente} dconf dump / > {TMP_DIR}/dump.conf")
        subprocess.run(["runuser", "-u", utente, "dconf", "dump", "/"], stdout=open(f"{TMP_DIR}/dump.conf", "w"))
        conf = input(
            "Nominare il file di configurazione: (consigliato il nome del DE) ")
        subprocess.run(f"mv {TMP_DIR}/dump.conf {TMP_DIR}/{conf}_{data}.conf")
        print()
        time.sleep(1)

        while True:
            print(
                f"\n{Fore.RED}Scegli la destinazione del file di configurazione:{Fore.RESET}")
            print()
            print("1. Cartella predefinita (Backup)")
            print("2. Altra cartella")
            print()
            print("0. Annulla e torna indietro")
            print()
            try:
                scelta = input("Inserisci il numero della scelta: ")
                if scelta == "0":
                    print("Operazione annullata.")
                    subprocess.run("python3 backovery.py")
                    return
                elif scelta == "1":
                    destinazione = "Backup"
                    subprocess.run(f"mv {TMP_DIR}/{conf}_{data}.conf Backup")
                    break
                elif scelta == "2":
                    destinazione = input(
                        "Inserisci il percorso della cartella di destinazione: ")
                    if os.path.isdir(destinazione):
                        subprocess.run(
                            f"mv {TMP_DIR}/{conf}_{data}.conf {destinazione}")
                        break
                    else:
                        print(
                            "Il percorso inserito non è una cartella valida. Riprova.")
                else:
                    raise ValueError
            except ValueError:
                print("Scelta non valida. Per favore, seleziona 0, 1 o 2.")

        if 'destinazione' in locals():
            print(
                f"Destinazione del file di configurazione selezionata: {destinazione}")
        else:
            print("Nessuna destinazione del file di configurazione selezionata.")

        print()
        time.sleep(2)

        # Esportazione dei pacchetti
        subprocess.run(
            f"apt-mark showmanual | grep -vE 'linux-(generic|headers|image|modules)' > {destinazione}/packages_{data}.txt")
        subprocess.run(
            f"sort {destinazione}/packages_{data}.txt -o {destinazione}/all_packages_{data}.txt")
        subprocess.run(f"rm {destinazione}/packages_{data}.txt")
        print()
        time.sleep(1)
        input("File generati, premere un tasto per tornare indietro!")
        subprocess.run("clear && clear")
        subprocess.run("python3 backovery.py")


esporta()


def stampa_avanzamento(passi):
    contatore = 0
    while contatore < passi:
        print(
            f"\r[{'#' * contatore}{'.' * (passi - contatore)}] {contatore}/{passi}", end="", flush=True)
        contatore += 1
        time.sleep(0.3)
    print("\r[" + "#" * passi + "] Operazione completata!")


def backup(scelta):
    if scelta == 2:
        time.sleep(2)
        print()
        print("INIZIO PROCEDURA, NON INTERROMPERE...")
        print()
        time.sleep(1)
        print("PULIZIA DEL SISTEMA")
        result = subprocess.run("apt-get autoremove && apt-get clean && apt-get autoclean", shell=True, capture_output=True, text=True)
        logging.info(result.stdout)
        if result.stderr:
            logging.error(result.stderr)
        subprocess.run("rm -rf /tmp/*")
        subprocess.run("rm -rf ~/.local/share/Trash/files/*")
        # Stampa della barra di avanzamento per la pulizia del sistema
        passi = 10
        stampa_avanzamento(passi)
        print()
        time.sleep(1)
        while scelta == 2:
            print()
            print()
            kernel = input(
                "Vuoi rimuovere delle vecchie versioni di kernel per ottimizzare il backup? [si/no] ")
            if kernel == 'si' or kernel == 's':
                print()
                print((Fore.RED + "Kernel attualmente utilizzato:"))
                subprocess.run("uname -r")
                print()
                print("Lista di tutti i kernel presenti nel sistema:")
                lista = "dpkg --get-selections | grep linux-image"
                subprocess.run(lista)
                print()
                print()
                print(
                    (Fore.RED + "ATTENZIONE - NON DISINSTALLARE IL KERNEL ATTUALMENTE IN USO"))
                uninstall = input("Specificare il kernel da rimuovere: ")
                command = "apt-get purge %s"
                subprocess.run(command % (uninstall))
                print()
                print("PULIZIA DEL SISTEMA")
                print()
                result = subprocess.run("apt-get autoremove && apt-get clean && apt-get autoclean", shell=True, capture_output=True, text=True)
        logging.info(result.stdout)
        if result.stderr:
            logging.error(result.stderr)
            if kernel == 'no' or kernel == 'n':
                print()
                print()
                print("Processo avviato...")
                print()
                time.sleep(2)

                # Scelta della destinazione del file di backup
                while True:
                    print(
                        f"\n{Fore.RED}Scegli la destinazione del file di backup:{Fore.RESET}")
                    print()
                    print("1. Cartella predefinita (Backup)")
                    print("2. Altra cartella")
                    print()
                    print("0. Annulla e torna indietro")
                    print()

                    try:
                        scelta = input("Inserisci il numero della scelta: ")

                        if scelta == "0":
                            print("Operazione annullata.")
                            subprocess.run("python3 backovery.py")
                            break
                        elif scelta == "1":
                            destinazione = "Backup"
                            break
                        elif scelta == "2":
                            destinazione = input(
                                "Inserisci il percorso della cartella di destinazione: ")
                            if os.path.isdir(destinazione):
                                break
                            else:
                                print(
                                    "Il percorso inserito non è una cartella valida. Riprova.")
                        else:
                            raise ValueError
                    except ValueError:
                        print("Scelta non valida. Per favore, seleziona 0, 1 o 2.")

                if 'destinazione' in locals():
                    print(
                        f"Destinazione del file di backup selezionata: {destinazione}")
                else:
                    print("Nessuna destinazione del file di backup selezionata.")

                print()
                time.sleep(1)
                # Se si vuole una minor compressione sostituire il flag -cpzf con -cpf
                command = "tar --xattrs -cpzf - --exclude-from='excludes' --one-file-system / 2>backup.log | pv -p --timer --rate --bytes > %s/backup_%s.tgz" % (
                    destinazione, data)
                subprocess.call(command, shell=True)
                print()
                print()
                input("Backup terminato, premere un tasto per uscire!")
                subprocess.run("clear && clear")
                return
backup()


def remote(scelta):
    if scelta == 3:
        print()
        print((Fore.RED + "                                    - !ATTENZIONE! -                                   "))
        print((Fore.RED + "Con questo sistema potete inviare il file di backup direttamente su un altro computer o server"))
        print((Fore.RED + "senza salvare alcun dato sul sistema locale!"))
        print((Fore.RED + "Scompattare il file remote.tar nel server e avviatelo"))
        print()
        time.sleep(2)
        print()
        kernel = input(
            "Vuoi rimuovere delle vecchie versioni di kernel per ottimizzare il backup? [si/no] ")
        if kernel == 'si' or kernel == 's':
            print()
            print((Fore.RED + "Kernel attualmente utilizzato:"))
            subprocess.run("uname -r")
            print()
            print("Lista di tutti i kernel presenti nel sistema:")
            lista = "dpkg --get-selections | grep linux-image"
            subprocess.run(lista)
            print()
            print()
            print(
                (Fore.RED + "ATTENZIONE - NON DISINSTALLARE IL KERNEL ATTUALMENTE IN USO"))
            uninstall = input("Specificare il kernel da rimuovere: ")
            command = "apt-get purge %s"
            subprocess.run(command % (uninstall))
            print()
            print("PULIZIA DEL SISTEMA")
            print()
            subprocess.run("apt-get autoremove && apt-get clean && apt-get autoclean")
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
            subprocess.run(command % (data, address, port))
            print()
            print()
            input("Backup remoto terminato, premere un tasto per uscire!")
            subprocess.run("clear && clear")
            return


remote()


def recovery(scelta):
    if scelta == 4:
        time.sleep(2)
        print()
        print((Fore.MAGENTA + "Lista Backup"))
        print((Fore.MAGENTA + "------------"))
        print()
        # Scelta della destinazione dei file di backup e pacchetti

        while True:
            print(f"\n{Fore.RED}Scegli la cartella di destinazione:{Fore.RESET}")
            print()
            print("1. Cartella predefinita (Backup)")
            print("2. Altra cartella")
            print()
            print("0. Annulla e torna indietro")
            print()

            try:
                scelta = input("Inserisci il numero della scelta: ")

                if scelta == "0":
                    print("Operazione annullata.")
                    subprocess.run("python3 backovery.py")
                    break
                elif scelta == "1":
                    destinazione = "Backup"
                    break
                elif scelta == "2":
                    destinazione = input(
                        "Inserisci il percorso della cartella: ")
                    if os.path.isdir(destinazione):
                        break
                    else:
                        print(
                            "Il percorso inserito non è una cartella valida. Riprova.")
                else:
                    raise ValueError
            except ValueError:
                print("Scelta non valida. Per favore, seleziona 0, 1 o 2.")

        if 'destinazione' in locals():
            print(f"Cartella di destinazione selezionata: {destinazione}")
        else:
            print("Nessuna cartella di destinazione selezionata.")

        print()
        input('Trasferire il file backup e file pacchetti nella cartella ' +
              Fore.RED + destinazione + Style.RESET_ALL + ' e premere il tasto INVIO')
        print()
        subprocess.run("apt-mark showmanual > tmp/new_packages.txt")
        subprocess.run("sort tmp/new_packages.txt -o tmp/newsystem_packages.txt")
        subprocess.run("mv tmp/newsystem_packages.txt %s/" % destinazione)
        subprocess.run("rm tmp/new_packages.txt")
        print()
        print()
        subprocess.run("cd %s && ls *.tgz" % destinazione)
        print()
        print()
        var_backup = input("Digitare un backup presente in lista: ")
        time.sleep(2)
        print()
        print("Processo avviato...")
        print()
        command2 = "pv %s/%s | tar -xpzf - -C / 2> recovery.log" % (
            destinazione, var_backup)
        subprocess.run(command2)
        print()
        print((Fore.MAGENTA + "Lista file pacchetti da ripristinare"))
        print((Fore.MAGENTA + "------------------------------------"))
        print()
        # Scelta della destinazione del file di pacchetti
        while True:
            print(f"\n{Fore.RED}Scegli la cartella dei pacchetti:{Fore.RESET}")
            print()
            print("1. Cartella predefinita (Backup)")
            print("2. Altra cartella")
            print()
            print("0. Annulla e torna indietro")
            print()

            try:
                scelta_pacchetti = input("Inserisci il numero della scelta: ")

                if scelta_pacchetti == "0":
                    print("Operazione annullata.")
                    subprocess.run("python3 backovery.py")
                    break
                elif scelta_pacchetti == "1":
                    destinazione_pacchetti = "Backup"
                    break
                elif scelta_pacchetti == "2":
                    destinazione_pacchetti = input(
                        "Inserisci il percorso della cartella: ")
                    if os.path.isdir(destinazione_pacchetti):
                        break
                    else:
                        print(
                            "Il percorso inserito non è una cartella valida. Riprova.")
                else:
                    raise ValueError
            except ValueError:
                print("Scelta non valida. Per favore, seleziona 0, 1 o 2.")

        if 'destinazione_pacchetti' in locals():
            print(
                f"Cartella dei pacchetti selezionata: {destinazione_pacchetti}")
        else:
            print("Nessuna cartella dei pacchetti selezionata.")
        print()
        subprocess.run("cd %s && ls all*.txt" % destinazione_pacchetti)
        print()
        var_list = input("Digitare la lista dei pacchetti da installare: ")
        # qui andrebbe il nuovo codice per confrontare i due file packages
        subprocess.run("chmod 666 %s/newsystem_packages.txt" %
                  destinazione_pacchetti)
        subprocess.run("awk 'NR==FNR{a[$0];next}!($0 in a)' %s/%s %s/newsystem_packages.txt > %s/packages_%s.txt" %
                  (destinazione_pacchetti, var_list, destinazione_pacchetti, destinazione_pacchetti, data))
        subprocess.run("rm %s/%s && rm %s/newsystem_packages.txt" %
                  (destinazione_pacchetti, var_list, destinazione_pacchetti))
        # -------------------------------------------------------------------------- #
        print()
        time.sleep(2)
        subprocess.run("apt update && apt upgrade -y")
        print()
        print()
        command = "xargs apt-get install --reinstall -y < %s/packages_%s.txt 2>recovery.log" % (
            destinazione_pacchetti, data)
        subprocess.run(command)
        time.sleep(2)
        print()
        print()
        print((Fore.MAGENTA + "Lista file di configurazione"))
        print((Fore.MAGENTA + "----------------------------"))
        print()
        # Scelta della destinazione del file di configurazione
        print()
        while True:
            print(
                f"\n{Fore.RED}Scegli la cartella del file di configurazione:{Fore.RESET}")
            print()
            print("1. Cartella predefinita (Backup)")
            print("2. Altra cartella")
            print()
            print("0. Annulla e torna indietro")

            try:
                scelta_config = input("Inserisci il numero della scelta: ")

                if scelta_config == "0":
                    print("Operazione annullata.")
                    subprocess.run("python3 backovery.py")
                    break
                elif scelta_config == "1":
                    destinazione_config = "Backup"
                    break
                elif scelta_config == "2":
                    destinazione_config = input(
                        "Inserisci il percorso della cartella: ")
                    if os.path.isdir(destinazione_config):
                        break
                    else:
                        print(
                            "Il percorso inserito non è una cartella valida. Riprova.")
                else:
                    raise ValueError
            except ValueError:
                print("Scelta non valida. Per favore, seleziona 0, 1 o 2.")

        if 'destinazione_config' in locals():
            print(
                f"Cartella di configurazione selezionata: {destinazione_config}")
        else:
            print("Nessuna cartella di configurazione selezionata.")
        print()
        print()

        utente = input("Inserisci l'username per eseguire il load di dconf: ")
        print()
        subprocess.run("cd %s && ls *.conf" % destinazione_config)
        print()
        conf = input("Digitare il file per la configurazione: ")

        # Esegui lo script separato come root, che preparerà il caricamento di dconf al prossimo login
        subprocess.run("python3 dconf_load.py {} {}/{}".format(utente,
                  destinazione_config, conf))

        print("Le impostazioni dconf verranno caricate al prossimo login dell'utente {}".format(utente))

        print()
        time.sleep(2)
        print()
        print((Fore.GREEN + "Processo terminato."))
        print((Fore.RESET))
        input("Premere un tasto per uscire, potete riavviare il computer!")
        subprocess.run("clear && clear")
        return


recovery()


def manager(scelta):
    subprocess.run("clear && clear")
    if scelta == 5:
        print()
        print((Fore.GREEN + "   ______    ____     ____  __   ___  ____   __    __   _____ ______ __      __ "))
        print((Fore.GREEN + "  (_   _ \  (    )   / ___)() ) / __)/ __ \  ) )  ( (  / ___/(   __ \) \    / ( "))
        print((Fore.GREEN + "    ) (_) ) / /\ \  / /    ( (_/ /  / /  \ \( (    ) )( (__   ) (__) )\ \  / /  "))
        print((
            Fore.GREEN + "    \   _/ ( (__) )( (     ()   (  ( ()  () )\ \  / /  ) __) (    __/  \ \/ /   "))
        print((
            Fore.GREEN + "    /  _ \  )    ( ( (     () /\ \ ( ()  () ) \ \/ /  ( (     ) \ \  _  \  /    "))
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
            select2 = int(input("Scegliere un opzione: "))
            if select2 >= 3:
                print("Opzione non trovata")
                input("Premere un tasto per continuare")
                subprocess.run("python3 backovery.py")
        except NameError:
            print("Comando non valido")
            input("Premere un tasto per continuare")
            subprocess.run("python3 backovery.py")
        except SyntaxError:
            print("Comando non valido")
            input("Premere un tasto per continuare")
            subprocess.run("python3 backovery.py")
        except UnboundLocalError:
            print("Sistema terminato")

        if select2 == 1:
            print()
            print()
            print("Lista Backup")
            print("------------")
            subprocess.run("cd backup && ls *.tgz")
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
                    subprocess.run("mkdir split")
                if size > byte:
                    command = "split -b %s -d --suffix-length=2 %s %s."
                    subprocess.run(command % (byte, file_tgz, file_tgz))
                    command_2 = "mv %s.*  split/"
                    subprocess.run(command_2 % (file_tgz))
                    print()
                    print("Operazione terminata")
                    input("Premere un tasto per uscire")
                    subprocess.run("clear && clear")
                    return
            if split == 'cd':
                os.chdir('backup')
                size = os.path.getsize(file_tgz)
                # Impostato per CD a 650Mb
                byte = 681574400
                check_dir = os.path.exists("split")
                if check_dir is False:
                    subprocess.run("mkdir split")
                if size > byte:
                    command = "split -b %s -d --suffix-length=2 %s %s."
                    subprocess.run(command % (byte, file_tgz, file_tgz))
                    command_2 = "mv %s.*  split/"
                    subprocess.run(command_2 % (file_tgz))
                    print()
                    print("Operazione terminata")
                    input("Premere un tasto per uscire")
                    subprocess.run("clear && clear")
                    return
            else:
                print("Opzione non trovata!")
                input("Premere un tasto per continuare")
                subprocess.run("python3 backovery.py")
        if select2 == 2:
            print()
            print()
            print("Lista Backup da unificare")
            print("-------------------------")
            print()
            os.chdir('backup/split')
            command = "ls -1 | sed -e 's/\..*$//' | sed -n 1p"
            subprocess.run(command)
            print()
            select_file = input("Digitare il backup da unire: ")
            command = "cat %s.* > %s.tgz"
            subprocess.run(command % (select_file, select_file))
            command_2 = "mv %s.tgz ../"
            subprocess.run(command_2 % (select_file))
            print()
            print("Completato")
            print()
            subprocess.run("python3 ../../backovery.py")
        if select2 == 0:
            subprocess.run("python3 backovery.py")


manager()


def close(scelta):
    if scelta == 0:
        subprocess.run("rm id")
        subprocess.call("clear", shell=True)
        return


close()
