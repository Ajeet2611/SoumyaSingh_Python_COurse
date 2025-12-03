str = "ajeet"
print(str.upper())  # Output: 'AJEET'
print(str.capitalize())  # Output: 'Ajeet'
print(str.title())  # Output: 'Ajeet'
print(str.lower())  # Output: 'ajeet'
print(str.swapcase())  # Output: 'AJEET'
print(str.count('t'))  # Output: 1
print(str.find('e'))  # Output: 2
print(str.replace('ajeet', 'Abhay'))  # Output: 'Abhay'
print(str.strip())  # Output: 'ajeet' (no leading/trailing spaces to remove)
print(str.startswith('a'))  # Output: True  
print(str.endswith('t'))  # Output: True
print(str.isalpha())  # Output: True
print(str.isdigit())  # Output: False
print(str.split('e'))  # Output: ['aj', '', 't']
print(str.join(['a', 'j', 'e', 'e', 't']))  # Output: 'ajeet'
print(str.zfill(10))  # Output: '00000ajeet'
print(str.center(20, '*'))  # Output: '*******ajeet********'
print(str.ljust(15, '-'))  # Output: 'ajeet----------'
print(str.rjust(15, '-'))  # Output: '----------ajeet'
print(str.partition('e'))  # Output: ('aj', 'e', 'et')
print(str.rpartition('e'))  # Output: ('aje', 'e', 't')
print(str.encode())  # Output: b'ajeet'
print(str.expandtabs(tabsize=4))  # Output: 'ajeet' (no tabs to expand)
print(str.islower())  # Output: True
print(str.isupper())  # Output: False
print(str.istitle())  # Output: False

