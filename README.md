# Configuration file Backovery
>System of backup and recovery

Required Python3.x with pip


### <span style="color:red">BACKUP</span>


* **Step 1**	
Install package pv and colorama

```
pip install -r requirements.txt 
```

* **Step 2**	
Download Backovery

```
git clone https://github.com/alexis-82/backovery.git
```

* **Step 3**	
Exclude folders in file exclude ex. syntax =--exclude=/proc

```
vim excludes
```

* **Step 4**	
Run file backovery.py

```
python backovery.py
```

* **Step 5**	
This folder contains the backup:

```
cd backup/
```	


### <span style="color:red">RECOVERY IN LIVE</span>
* **Step 1**	
Install package pv

```
sudo apt-get update
```
```
pip install -r requirements.txt 
```
* **Step 2**	
Download Backovery

```
git clone https://github.com/alexis-82/backovery.git
```
* **Step 2**	
Run file backovery.py

```
python backovery.py
```
