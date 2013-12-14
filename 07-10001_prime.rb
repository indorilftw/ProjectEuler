def isPrime(x)
    max = Math.sqrt(x)
    for i in 2 .. max
        if x % i == 0 then
            return false
        end
    end
    return true
end

i = 2
count = 0
while count < 10001
    if isPrime(i) then
        count += 1
    end
    i += 1
end
puts count, i-1

