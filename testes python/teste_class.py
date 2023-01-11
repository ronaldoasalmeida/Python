class Carros:

# class attribute
  auto = 'carro'

# instance attribute
 def __init__(self, marca, ano, n_portas, cor):
    self.marca = marca
    self.ano = ano
    self.portas = n_portas
    self.cor = cor
    

# instantiate the Parrot class
fusca = Carros('Volkswagen', 2022, 2, 'prata')
ka = Carros('Ford', 2018, 4, 'preto')
a8 = Carros('Audi', 2010, 3, 'branco')

# access the class attributes
print('Fusca é um {}'.format(fusca.__class__.auto))
print('Ka também é {}'.format(ka.__class__.auto))
print('Audi A8 é outro {}'.format(a8.__class__.auto))


print('Características do primeiro carro que temos: ', fusca.marca, 'Fusca'',', fusca.ano,',',fusca.portas, 'portas',',',fusca.cor)
print('Características do segundo carro que temos: ', ka.marca, 'Ka'',', ka.ano,',',ka.portas, 'portas',',',ka.cor)
print('Características do terceiro carro que temos: ', a8.marca, 'A8'',', a8.ano,',',a8.portas, 'portas',',',a8.cor)

# access the instance attributes
# print('{} is {} years old'.format( blu.name, blu.age))
# print('{} is {} years old'.format( woo.name, woo.age)

name = 'Ronaldo'
print(name)
