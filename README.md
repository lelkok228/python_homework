Encryption.\
Works in 4 modes, supports 2 ciphers.\
Launch examples for each mode:\
1)python3 main.py encode --input_file=input.txt --output_file=output.txt --cipher=caesar --key=2\
2)python3 main.py decode --input_file=input.txt --output_file=output.txt --cipher=vigenere --key=abcDEf\
3)python3 main.py frequency --input_file=input.txt --output_file=output.json\
4)python3 main.py hack --input_file=input.txt --output_file=output.txt --frequency_file=frequency.json\
\
It is also possible to use the console for text input or output without input_file or output_file respectively.\
Added possibility to use letters of the Russian alphabet, numbers, spaces and punctuation marks.\
Now the original alphabet has the following appearance `abcdefghijklmnopqrstuvwxyzабвгдежзийклмнопрстуфхцчшщъыьэюя0123456789 !?.,:;-"{}()[]<>`

