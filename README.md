# bat-crypt
bat file crypting


in hex editor edit 00000000 as FF FE 26 63 6C 73 0D 0A

> FF FE 26 63 6C 73 0D 0A

its &cls (ÿþ&cls)


example found in web 

https://www.developpez.net/forums/d2086811/general-developpement/programmation-systeme/windows/scripts-batch/protection-fichiers-batch/


https://pastebin.com/gnrkAUVh

ÿþ&cls ÿþ&cls ÿþ&cls ÿþ&cls ÿþ&cls ÿþ&cls ÿþ&cls ÿþ&cls


https://github.com/uchks/hone-deobf

malware example 
```
One interesting thing to note about the batch files was the use of an obfuscation technique that is not commonly seen. In early campaigns, the attacker prepended the bytes "FF FE 26 63 6C 73 0D 0A" into the file, causing various file parsers to interpret the file contents as UTF-16 LE, resulting in the parsers failing to properly display the contents of the batch file.
```

https://blog.talosintelligence.com/rat-ratatouille-revrat-orcus/
