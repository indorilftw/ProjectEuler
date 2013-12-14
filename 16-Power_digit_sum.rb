sum = 0
num = String(2 ** 1000)
num.each_char do |i|
    sum += Integer(i)
end
puts sum