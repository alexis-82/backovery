# System of backup and recovery
Configuration file Backovery


Required Python3.x with pip


### <span style="color:red">BACKUP</span>


* **Step 1**

Download Backovery

```
git clone https://github.com/alexis-82/backovery.git
```	

* **Step 2**	

Install package pv and colorama

```
pip install -r requirements.txt 
```
and
```
apt install pv
```

* **Step 3**	

Exclude folders in file exclude ex. syntax = /proc <span style="color:red">(already configures)</span>

```
vim excludes
```

* **Step 4**	

Run file backovery.py

```
python3 backovery.py
```

* **Step 5**	

This folder contains the backup:

```
cd backup/
```	


### <span style="color:red">RECOVERY</span>
* **Step 1**	

Download Backovery

```
git clone https://github.com/alexis-82/backovery.git
```
* **Step 2**	

Install package pv and colorama

```
pip install -r requirements.txt 
```
and
```
apt install pv
```
* **Step 3**

Put the backup file in the backup/ 
* **Step 4**

Run file backovery.py

```
python3 backovery.py
```
# Todo List

## Things to do
- [x] Export and Import file config desktop
- [x] Empty trash
- [x] Fix function remote
- [ ] Install libraries from script
- [ ] Check code with 'su' system
- [ ] Update all systems

## Fix bugs
- [ ] 
