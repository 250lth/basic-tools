# basic data type

p (true && false) || true
p (3 + 3) * (14 / 2)
p 'hello ' + 'world'
p 'hello world'.slice(6)

p :my_symbol
p :my_symbol == :my_symbol
p :my_symbol == :another_symbol

p 'hello world'.slice(11)


# data struct

p numbers = ['zero', 'one', 'two']
p numbers[1]
p numbers.push('three', 'four')
p numbers
p numbers.drop(2)

p ages = 18..30
p ages.entries
p ages.include?(25)
p ages.include?(33)

p fruit = { 'a' => 'apple', 'b' => 'banana', 'c' => 'coconut' }
p fruit['b']
p fruit['d'] = 'date'
p fruit

p dimensions = { width: 1000, height: 2250, depth: 250 }
p dimensions[:depth]

# proc
p multiply = -> x, y { x * y }
p multiply.call(6, 9)
p multiply.call(2, 3)
p multiply[3, 4]