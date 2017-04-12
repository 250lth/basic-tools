p (
  if 2 < 3
    'less'
  else
    'more'
  end
  )

p quantify =
    -> number {
      case number
        when 1
          'one'
        when 2
          'two'
        else
          'many'
      end
    }
p quantify.call(2)
p quantify.call(10)

p x = 1
p (
  while x < 1000
    x = x * 2
  end
  )
p x