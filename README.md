# Cracking Blake Hash
This tool for crack hash BLAKE-224 BLAKE-256 BLAKE-512 BLAKE-384 with bruteforce method

<b>Require</b> python3++ & hashlib module</br>
tested on Linux kali 4.14.0-kali3-amd64 #1 SMP Debian 4.14.12-2kali1 (2018-01-08) x86_64 GNU/Linux </br>
tested on Python 3.6.4</br></br>
![Markdown Here logo](https://github.com/mirfansulaiman/Cracking-Blake-Hash/blob/master/Capture.PNG)
## For cracking : 
Usage : python crack_blade.py</br>
1. Please change the wordlist <i>rockyou.txt</i>
<pre>
with open("rockyou.txt", encoding='utf-8', errors='ignore') as infile:
</pre></br>
2. If you want to use another blake , make you sure change the <i>BLAKE2b512</i></br>
<pre>
blake = hashlib.new('BLAKE2b512')
</pre></br>
3. And the last, dont forget change the hash <i>999999999999999999999999</i> with what do you want to crack it ! </br>
<pre>
if not blake.hexdigest() == '999999999999999999999999':
</pre></br></br>
## For Encryption :
Just like this and change the text <i>The quick brown fox jumps over the lazy dog</i></br>
<pre>print(encrypt('The quick brown fox jumps over the lazy dog'))</pre>

Reference for find type of blake hash : </br></br>
[**BLAKE (Hash Funtion)**](https://en.wikipedia.org/wiki/BLAKE_(hash_function))</br>
[**Python Hashlib**](https://docs.python.org/3/library/hashlib.html)<br>
[**Blake Official**](https://github.com/BLAKE2/BLAKE2)
[***Pyblake2*](https://pythonhosted.org/pyblake2/)
