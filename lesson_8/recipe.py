pasta=('pasta','tomatoes','cheese','seasoning','vegetables','water',30)
print(pasta)
print(pasta[0])
print(pasta[1:4])
print(pasta[-4:-1])

for i in (pasta):
    print(i)


pasta={'pasta','tomatoes','cheese','seasoning','vegetables','water',30}
print(pasta)
pasta.add("onion")
print(pasta)
pasta.add('spices')
print(pasta)
pasta.discard('vegetables')
print(pasta)
burger={'bread','sauces','tomatoes','cheese','patty','spices','garlic'}

print('\nnow string operations')

print(pasta|burger)
print(pasta & burger)
print(pasta -burger)
print(pasta^burger)
