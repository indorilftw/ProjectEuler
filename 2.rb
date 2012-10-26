sum = fib1 = fib2 = 0
fib = 1
while fib < 4000000 do
  sum += fib if (fib % 2 == 0)
  fib1 = fib2
  fib2 = fib
  fib = fib1 + fib2
end
puts sum