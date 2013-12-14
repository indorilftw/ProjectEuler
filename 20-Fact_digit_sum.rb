fac = 1
for i in 1..100
    fac *= i
end
sum = 0
String(fac).each_char do |i| 
    sum += Integer(i)
end
puts sum