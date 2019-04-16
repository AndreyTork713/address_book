#ab - сокращение от address book
ab = {
      'Swaroop': 'swaroop@swaroopch.com',
        'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
       'Spamer': 'spamer@hotmail.com'
    }
print('Address of Swaroop:',ab['Swaroop'])

#Удаление пары "ключ-значение"
del ab['Spamer']
print('\nВ адресной книге {0} контактов\n'.format(len(ab)))

for name,address in ab.items():
    print('Контакт {0} с адресом {1}'.format(name,address))
