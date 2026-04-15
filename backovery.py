#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import time
from lib import Fore, Back, Style, init
#import pwd
import logging

def pulisci_schermo():
    os.system('cls' if os.name == 'nt' else 'clear')

logging.basicConfig(
    filename="backovery.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

if hasattr(os, "geteuid") and os.geteuid() != 0:
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

if current_dir + '\n' not in exclude_paths:
    # Aggiungi il path al file di esclusione
    with open(exclude_file, 'a') as f:
        f.write(current_dir + '\n')

init(autoreset=True)

data = (time.strftime("%d_%m_%Y"))
directory = os.getcwd()

def stampa_header():
    print()
    print(Fore.GREEN + "   ______    ____     ____  __   ___  ____   __    __   _____ ______ __      __ ")
    print(Fore.GREEN + "  (_   _ \\  (    )   / ___)() ) / __)/ __ \\  ) )  ( (  / ___/(   __ \\) \\    / ( ")
    print(Fore.GREEN + "    ) (_) ) / /\\ \\  / /    ( (_/ /  / /  \\ \\( (    ) )( (__   ) (__) )\\ \\  / /  ")
    print(Fore.GREEN + "    \\   _/ ( (__) )( (     ()   (  ( ()  () )\\ \\  / /  ) __) (    __/  \\ \\/ /   ")
    print(Fore.GREEN + "    /  _ \\  )    ( ( (     () /\\ \\ ( ()  () ) \\ \\/ /  ( (     ) \\ \\  _  \\  /    ")
    print(Fore.GREEN + "   _) (_) )/  /\\  \\ \\ \\___ ( (  \\ \\ \\ \\__/ /   \\  /    \\ \\___( ( \\ \\_))  )(     ")
    print(Fore.GREEN + "  (______//__(  )__\\ \\____)()_)  \\_\\ \\____/     \\/      \\____\\)_) \\__/  /__\\    ")
    print()
    print(Fore.RED + "                                  Coded by Alexis")
    print(Fore.RED + "                                https://alexis82.it/")
    print(Style.RESET_ALL)
    print()


# ---------------------------------------------------------------------------- #
#                                    MENU                                      #
# ---------------------------------------------------------------------------- #

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
        pulisci_schermo()
        stampa_header()
        mostra_menu()
        try:
            scelta = int(input(": ").strip())
        except ValueError:
            print("Inserire un numero valido.")
            continue

        if scelta == 0:
            close()
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


# ---------------------------------------------------------------------------- #
#                                  FUNZIONI                                    #
# ---------------------------------------------------------------------------- #

def esporta():
    pulisci_schermo()
    stampa_header()
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
    subprocess.run(["runuser", "-u", utente, "dconf", "dump", "/"], stdout=open(f"{TMP_DIR}/dump.conf", "w"))
    conf = input("Nominare il file di configurazione: (consigliato il nome del DE) ")
    subprocess.run(f"mv {TMP_DIR}/dump.conf {TMP_DIR}/{conf}_{data}.conf", shell=True)
    print()
    time.sleep(1)

    destinazione = None
    while True:
        print(f"\n{Fore.RED}Scegli la destinazione del file di configurazione:{Fore.RESET}")
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
                return
            elif scelta == "1":
                destinazione = "Backup"
                subprocess.run(f"mv {TMP_DIR}/{conf}_{data}.conf Backup", shell=True)
                break
            elif scelta == "2":
                destinazione = input("Inserisci il percorso della cartella di destinazione: ")
                if os.path.isdir(destinazione):
                    subprocess.run(f"mv {TMP_DIR}/{conf}_{data}.conf {destinazione}", shell=True)
                    break
                else:
                    print("Il percorso inserito non è una cartella valida. Riprova.")
            else:
                raise ValueError
        except ValueError:
            print("Scelta non valida. Per favore, seleziona 0, 1 o 2.")

    if destinazione:
        print(f"Destinazione del file di configurazione selezionata: {destinazione}")
    else:
        print("Nessuna destinazione del file di configurazione selezionata.")

    print()
    time.sleep(2)

    # Esportazione dei pacchetti
    subprocess.run(
        f"apt-mark showmanual | grep -vE 'linux-(generic|headers|image|modules)' > {destinazione}/packages_{data}.txt",
        shell=True)
    subprocess.run(
        f"sort {destinazione}/packages_{data}.txt -o {destinazione}/all_packages_{data}.txt",
        shell=True)
    subprocess.run(f"rm {destinazione}/packages_{data}.txt", shell=True)
    print()
    time.sleep(1)
    input("File generati, premere un tasto per tornare indietro!")
    subprocess.call("clear && clear", shell=True)


def stampa_avanzamento(passi):
    contatore = 0
    while contatore < passi:
        print(
            f"\r[{'#' * contatore}{'.' * (passi - contatore)}] {contatore}/{passi}", end="", flush=True)
        contatore += 1
        time.sleep(0.3)
    print("\r[" + "#" * passi + "] Operazione completata!")


def backup():
    pulisci_schermo()
    stampa_header()
    time.sleep(2)
    print()
    print("INIZIO PROCEDURA, NON INTERROMPERE...")
    print()
    time.sleep(1)
    print("PULIZIA DEL SISTEMA")
    result = subprocess.run(
        "apt-get autoremove -y && apt-get clean && apt-get autoclean",
        shell=True, capture_output=True, text=True)
    logging.info(result.stdout)
    if result.stderr:
        logging.error(result.stderr)
    subprocess.run("rm -rf /tmp/*", shell=True)
    subprocess.run("rm -rf ~/.local/share/Trash/files/*", shell=True)
    # Stampa della barra di avanzamento per la pulizia del sistema
    stampa_avanzamento(10)
    print()
    time.sleep(1)

    # Domanda rimozione kernel — loop finché risposta valida
    while True:
        print()
        print()
        kernel = input("Vuoi rimuovere delle vecchie versioni di kernel per ottimizzare il backup? [si/no] ")
        if kernel == 'si' or kernel == 's':
            print()
            print((Fore.RED + "Kernel attualmente utilizzato:"))
            subprocess.run("uname -r", shell=True)
            print()
            print("Lista di tutti i kernel presenti nel sistema:")
            subprocess.run("dpkg --get-selections | grep linux-image", shell=True)
            print()
            print()
            print((Fore.RED + "ATTENZIONE - NON DISINSTALLARE IL KERNEL ATTUALMENTE IN USO"))
            uninstall = input("Specificare il kernel da rimuovere: ")
            subprocess.run("apt-get purge %s" % uninstall, shell=True)
            print()
            print("PULIZIA DEL SISTEMA")
            print()
            result2 = subprocess.run(
                "apt-get autoremove -y && apt-get clean && apt-get autoclean",
                shell=True, capture_output=True, text=True)
            logging.info(result2.stdout)
            if result2.stderr:
                logging.error(result2.stderr)
            break
        elif kernel == 'no' or kernel == 'n':
            break
        else:
            print("Risposta non valida. Digitare 'si' oppure 'no'.")

    print()
    print()
    print("Processo avviato...")
    print()
    time.sleep(2)

    # Scelta della destinazione del file di backup
    destinazione = None
    while True:
        print(f"\n{Fore.RED}Scegli la destinazione del file di backup:{Fore.RESET}")
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
                return
            elif scelta == "1":
                destinazione = "Backup"
                break
            elif scelta == "2":
                destinazione = input("Inserisci il percorso della cartella di destinazione: ")
                if os.path.isdir(destinazione):
                    break
                else:
                    print("Il percorso inserito non è una cartella valida. Riprova.")
            else:
                raise ValueError
        except ValueError:
            print("Scelta non valida. Per favore, seleziona 0, 1 o 2.")

    if destinazione:
        print(f"Destinazione del file di backup selezionata: {destinazione}")
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
    subprocess.call("clear && clear", shell=True)


def remote():
    pulisci_schermo()
    stampa_header()
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
        subprocess.run("uname -r", shell=True)
        print()
        print("Lista di tutti i kernel presenti nel sistema:")
        subprocess.run("dpkg --get-selections | grep linux-image", shell=True)
        print()
        print()
        print((Fore.RED + "ATTENZIONE - NON DISINSTALLARE IL KERNEL ATTUALMENTE IN USO"))
        uninstall = input("Specificare il kernel da rimuovere: ")
        subprocess.run("apt-get purge %s" % uninstall, shell=True)
        print()
        print("PULIZIA DEL SISTEMA")
        print()
        subprocess.run("apt-get autoremove -y && apt-get clean && apt-get autoclean", shell=True)
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
        subprocess.run(command % (data, address, port), shell=True)
        print()
        print()
        input("Backup remoto terminato, premere un tasto per uscire!")
        subprocess.call("clear && clear", shell=True)


def recovery():
    pulisci_schermo()
    stampa_header()
    time.sleep(2)
    print()
    print((Fore.MAGENTA + "Lista Backup"))
    print((Fore.MAGENTA + "------------"))
    print()

    # Scelta della cartella di destinazione
    destinazione = None
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
                return
            elif scelta == "1":
                destinazione = "Backup"
                break
            elif scelta == "2":
                destinazione = input("Inserisci il percorso della cartella: ")
                if os.path.isdir(destinazione):
                    break
                else:
                    print("Il percorso inserito non è una cartella valida. Riprova.")
            else:
                raise ValueError
        except ValueError:
            print("Scelta non valida. Per favore, seleziona 0, 1 o 2.")

    if destinazione:
        print(f"Cartella di destinazione selezionata: {destinazione}")
    else:
        print("Nessuna cartella di destinazione selezionata.")

    print()
    input('Trasferire il file backup e file pacchetti nella cartella ' +
          Fore.RED + destinazione + Style.RESET_ALL + ' e premere il tasto INVIO')
    print()
    subprocess.run("apt-mark showmanual > tmp/new_packages.txt", shell=True)
    subprocess.run("sort tmp/new_packages.txt -o tmp/newsystem_packages.txt", shell=True)
    subprocess.run("mv tmp/newsystem_packages.txt %s/" % destinazione, shell=True)
    subprocess.run("rm tmp/new_packages.txt", shell=True)
    print()
    print()
    subprocess.run("cd %s && ls *.tgz" % destinazione, shell=True)
    print()
    print()
    var_backup = input("Digitare un backup presente in lista: ")
    time.sleep(2)
    print()
    print("Processo avviato...")
    print()
    command2 = "pv %s/%s | tar -xpzf - -C / 2> recovery.log" % (destinazione, var_backup)
    subprocess.run(command2, shell=True)
    print()
    print((Fore.MAGENTA + "Lista file pacchetti da ripristinare"))
    print((Fore.MAGENTA + "------------------------------------"))
    print()

    # Scelta della cartella dei pacchetti
    destinazione_pacchetti = None
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
                return
            elif scelta_pacchetti == "1":
                destinazione_pacchetti = "Backup"
                break
            elif scelta_pacchetti == "2":
                destinazione_pacchetti = input("Inserisci il percorso della cartella: ")
                if os.path.isdir(destinazione_pacchetti):
                    break
                else:
                    print("Il percorso inserito non è una cartella valida. Riprova.")
            else:
                raise ValueError
        except ValueError:
            print("Scelta non valida. Per favore, seleziona 0, 1 o 2.")

    if destinazione_pacchetti:
        print(f"Cartella dei pacchetti selezionata: {destinazione_pacchetti}")
    else:
        print("Nessuna cartella dei pacchetti selezionata.")

    print()
    subprocess.run("cd %s && ls all*.txt" % destinazione_pacchetti, shell=True)
    print()
    var_list = input("Digitare la lista dei pacchetti da installare: ")
    # confronto dei due file packages
    subprocess.run("chmod 666 %s/newsystem_packages.txt" % destinazione_pacchetti, shell=True)
    subprocess.run(
        "awk 'NR==FNR{a[$0];next}!($0 in a)' %s/%s %s/newsystem_packages.txt > %s/packages_%s.txt" %
        (destinazione_pacchetti, var_list, destinazione_pacchetti, destinazione_pacchetti, data),
        shell=True)
    subprocess.run(
        "rm %s/%s && rm %s/newsystem_packages.txt" %
        (destinazione_pacchetti, var_list, destinazione_pacchetti),
        shell=True)
    print()
    time.sleep(2)
    subprocess.run("apt update && apt upgrade -y", shell=True)
    print()
    print()
    command = "xargs apt-get install --reinstall -y < %s/packages_%s.txt 2>recovery.log" % (
        destinazione_pacchetti, data)
    subprocess.run(command, shell=True)
    time.sleep(2)
    print()
    print()
    print((Fore.MAGENTA + "Lista file di configurazione"))
    print((Fore.MAGENTA + "----------------------------"))
    print()

    # Scelta della cartella del file di configurazione
    destinazione_config = None
    while True:
        print(f"\n{Fore.RED}Scegli la cartella del file di configurazione:{Fore.RESET}")
        print()
        print("1. Cartella predefinita (Backup)")
        print("2. Altra cartella")
        print()
        print("0. Annulla e torna indietro")
        print()
        try:
            scelta_config = input("Inserisci il numero della scelta: ")
            if scelta_config == "0":
                print("Operazione annullata.")
                return
            elif scelta_config == "1":
                destinazione_config = "Backup"
                break
            elif scelta_config == "2":
                destinazione_config = input("Inserisci il percorso della cartella: ")
                if os.path.isdir(destinazione_config):
                    break
                else:
                    print("Il percorso inserito non è una cartella valida. Riprova.")
            else:
                raise ValueError
        except ValueError:
            print("Scelta non valida. Per favore, seleziona 0, 1 o 2.")

    if destinazione_config:
        print(f"Cartella di configurazione selezionata: {destinazione_config}")
    else:
        print("Nessuna cartella di configurazione selezionata.")

    print()
    print()
    utente = input("Inserisci l'username per eseguire il load di dconf: ")
    print()
    subprocess.run("cd %s && ls *.conf" % destinazione_config, shell=True)
    print()
    conf = input("Digitare il file per la configurazione: ")

    # Esegui lo script separato come root, che preparerà il caricamento di dconf al prossimo login
    subprocess.run("python3 dconf_load.py {} {}/{}".format(utente, destinazione_config, conf), shell=True)
    print("Le impostazioni dconf verranno caricate al prossimo login dell'utente {}".format(utente))

    print()
    time.sleep(2)
    print()
    print((Fore.GREEN + "Processo terminato."))
    print((Fore.RESET))
    input("Premere un tasto per uscire, potete riavviare il computer!")
    subprocess.call("clear && clear", shell=True)


def manager():
    pulisci_schermo()
    stampa_header()
    subprocess.call("clear && clear", shell=True)
    print()
    print((Fore.GREEN + "   ______    ____     ____  __   ___  ____   __    __   _____ ______ __      __ "))
    print((Fore.GREEN + r"  (_   _ \  (    )   / ___)() ) / __)/ __ \  ) )  ( (  / ___/(   __ \) \    / ( "))
    print((Fore.GREEN + r"    ) (_) ) / /\ \  / /    ( (_/ /  / /  \ \( (    ) )( (__   ) (__) )\ \  / /  "))
    print((Fore.GREEN + r"    \   _/ ( (__) )( (     ()   (  ( ()  () )\ \  / /  ) __) (    __/  \ \/ /   "))
    print((Fore.GREEN + r"    /  _ \  )    ( ( (     () /\ \ ( ()  () ) \ \/ /  ( (     ) \ \  _  \  /    "))
    print((Fore.GREEN + r"   _) (_) )/  /\  \ \ \___ ( (  \ \ \ \__/ /   \  /    \ \___( ( \ \_))  )(     "))
    print((Fore.GREEN + r"  (______//__(  )__\ \____)()_)  \_\ \____/     \/      \____\)_) \__/  /__\    "))
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
    except ValueError:
        print("Comando non valido. Inserire un numero.")
        input("Premere un tasto per continuare")
        return

    if select2 not in (0, 1, 2):
        print("Opzione non trovata.")
        input("Premere un tasto per continuare")
        return

    if select2 == 0:
        return

    if select2 == 1:
        print()
        print()
        print("Lista Backup")
        print("------------")
        subprocess.run("ls backup/*.tgz", shell=True)
        print()
        file_tgz = input("Digitare il backup da splittare: ")
        split = input("Dimensioni? [dvd / cd] ").strip().lower()
        if split == 'dvd':
            byte = 4294967296  # 4 GB
        elif split == 'cd':
            byte = 681574400   # 650 MB
        else:
            print("Opzione non trovata!")
            input("Premere un tasto per continuare")
            return

        backup_path = os.path.join('backup', file_tgz)
        size = os.path.getsize(backup_path)
        split_dir = os.path.join('backup', 'split')
        if not os.path.exists(split_dir):
            os.makedirs(split_dir)

        if size > byte:
            command = "split -b %s -d --suffix-length=2 %s %s." % (byte, backup_path, backup_path)
            subprocess.run(command, shell=True)
            subprocess.run("mv backup/%s.* backup/split/" % file_tgz, shell=True)
            print()
            print("Operazione terminata")
            input("Premere un tasto per uscire")
            subprocess.call("clear && clear", shell=True)
        else:
            print("Il file è già più piccolo della dimensione selezionata, split non necessario.")
            input("Premere un tasto per continuare")

    if select2 == 2:
        print()
        print()
        print("Lista Backup da unificare")
        print("-------------------------")
        print()
        subprocess.run("ls -1 backup/split/ | sed -e 's/\\..*$//' | sort -u", shell=True)
        print()
        select_file = input("Digitare il backup da unire: ")
        subprocess.run("cat backup/split/%s.* > backup/%s.tgz" % (select_file, select_file), shell=True)
        print()
        print("Completato")
        print()
        input("Premere un tasto per tornare indietro")
        subprocess.call("clear && clear", shell=True)


def close():
    subprocess.run("rm -f id", shell=True)
    subprocess.call("clear", shell=True)


# ---------------------------------------------------------------------------- #
#                                   AVVIO                                      #
# ---------------------------------------------------------------------------- #

if __name__ == "__main__":
    main()