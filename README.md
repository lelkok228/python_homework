Шифрование.\
Работает в 4 режимах, поддерживает 2 шифра.\
Примеры запуска для каждого из режимов:\
1)python3 main.py encode --input_file=input.txt --output_file=output.txt --cipher=caesar --key=2\
2)python3 main.py decode --input_file=input.txt --output_file=output.txt --cipher=vigenere --key=abcDEf\
3)python3 main.py frequency --input_file=input.txt --output_file=output.json\
4)python3 main.py hack --input_file=input.txt --output_file=output.txt --frequency_file=frequency.json\
\
Также есть возможность использовать консоль для ввода или вывода текста, для этого следует не указывать input_file или output_file соответственно. 
