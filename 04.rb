def palindrome?(str)
  str == str.reverse
end

max = 0
999.downto(1) do |i|
    999.downto(1) do |j|
        if (palindrome?(String(i*j)) && (i * j) > max)
            max = i * j
        end
    end
end
puts max