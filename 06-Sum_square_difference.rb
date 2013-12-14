sum1 = sum2 = 0
for i in 1..100 do
    sum1 += i
    sum2 += i**2
end
sum1 **=2
puts "sum1 = #{sum1}"
puts "sum2 = #{sum2}"
puts sum1 - sum2