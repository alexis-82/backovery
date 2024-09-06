#!/usr/bin/env python3
import os
import sys
import shutil

if len(sys.argv) != 3:
    print("Usage: {} <username> <config_file>".format(sys.argv[0]))
    sys.exit(1)

username = sys.argv[1]
config_file = sys.argv[2]

# Verifica che il file di configurazione esista
if not os.path.exists(config_file):
    print("Error: Configuration file {} does not exist.".format(config_file))
    sys.exit(1)

# Crea una directory temporanea per l'utente se non esiste
user_temp_dir = "/home/{}/.config/backovery_temp".format(username)
os.makedirs(user_temp_dir, exist_ok=True)

# Copia il file di configurazione nella directory temporanea
shutil.copy2(config_file, os.path.join(user_temp_dir, "dconf_settings.conf"))

# Crea uno script che verrà eseguito al login
login_script = """#!/bin/bash
if [ -f ~/.config/backovery_temp/dconf_settings.conf ]; then
    dconf load / < ~/.config/backovery_temp/dconf_settings.conf
    rm -f ~/.config/backovery_temp/dconf_settings.conf
    rm -f ~/.config/autostart/load_dconf_settings.desktop
    rm -f ~/.config/backovery_temp/load_dconf_settings.sh
    rmdir ~/.config/backovery_temp 2>/dev/null
    notify-send "Backovery" "Le impostazioni dconf sono state caricate con successo."
fi
"""

# Salva lo script nella home dell'utente
with open("/home/{}/.config/backovery_temp/load_dconf_settings.sh".format(username), "w") as f:
    f.write(login_script)

# Rendi lo script eseguibile
os.chmod("/home/{}/.config/backovery_temp/load_dconf_settings.sh".format(username), 0o755)

# Crea un file .desktop per eseguire lo script al login
desktop_file = """[Desktop Entry]
Type=Application
Exec=/home/{}/.config/backovery_temp/load_dconf_settings.sh
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name[en_US]=Load dconf settings
Name=Load dconf settings
Comment[en_US]=Load dconf settings at login
Comment=Load dconf settings at login
"""

# Salva il file .desktop
autostart_dir = "/home/{}/.config/autostart".format(username)
os.makedirs(autostart_dir, exist_ok=True)
with open(os.path.join(autostart_dir, "load_dconf_settings.desktop"), "w") as f:
    f.write(desktop_file.format(username))

# Cambia il proprietario dei file creati all'utente specificato
os.system("chown -R {0}:{0} {1}".format(username, user_temp_dir))
os.system("chown {0}:{0} {1}/load_dconf_settings.desktop".format(username, autostart_dir))