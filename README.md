# Cracking Blake Hash

This tool for crack hash BLAKE-224 BLAKE-256 BLAKE-512 BLAKE-384 with bruteforce method

Require python3 & hashlib module</br>
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
</pre></br>

Usage : python crack_blade.py</br>

Reference for find type of blake hash : </br>
[**Python Hashlib**](https://docs.python.org/3/library/hashlib.html)<br>
[**Blake Official**](https://github.com/BLAKE2/BLAKE2)
