def isPrime(x)
    max = Math.sqrt(x)
    for i in 2 .. max
        if x % i == 0 then
            return false
        end
    end
    return true
end

sum = 0
for i in 2..2000000
    if isPrime(i) then
        sum += i
    end
end

puts sum

