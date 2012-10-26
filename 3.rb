def isPrime(x)
    max = Math.sqrt(x)
    for i in 2 .. max
        if x % i == 0 then
            return false
        end
    end
    return true
end

max = 2
i = 2
num = 600851475143
while i <= num
    if isPrime(i) then
      max = i
      while num % i == 0 do
        num /= i
        puts num
      end
    end
    i += 1
end
puts "max = #{max}"
