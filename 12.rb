i = triang = 1
found = false
loop do
    i += 1
    triang += i
    count = 0
    for div in 2..Math.sqrt(triang) do
        count += 1 if (triang % div == 0)
    end
    #puts "count of #{triang}  =  #{count}"
    if count >= 250 then
        found = true
        puts "result = #{triang}"
    end
    break if found
end