sum = 0
for i in 3..999 do
  sum += i if ((i % 3 == 0) or (i % 5 == 0))
end
puts sum
