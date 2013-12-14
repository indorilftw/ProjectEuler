for a in 1..999 do
    b = 1
    sum = 1
    while (sum < 1000) do
        b += 1
        c = Math.sqrt(a**2 + b**2)
        sum = a + b + c
    end
    if sum == 1000 then
        puts "a = #{a}, b = #{b}, c = #{c}, abc = #{a * b * c}"
        break
    end
end