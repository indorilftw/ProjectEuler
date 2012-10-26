fib1 = fib2 = 1
fib = 2
count = 3
while String(fib).length < 1000 do
  fib1 = fib2
  fib2 = fib
  fib = fib1 + fib2
  count += 1
end
puts "Fib = #{fib} \n\ncount = #{count}"