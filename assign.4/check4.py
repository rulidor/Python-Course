import hw4_part1 
print(hw4_part1.base_to_decimal("10121",3) == 97)
print(hw4_part1.base_to_decimal("435",6) == 167)
print(hw4_part1.base_to_decimal("22",11) == 24)
print(hw4_part1.base_to_decimal("244",14) == 452)
print(hw4_part1.base_to_decimal("c",14) == 12)

print(hw4_part1.int_to_base(174,7) == "336")
print(hw4_part1.int_to_base(2,11) == "2")
print(hw4_part1.int_to_base(480,6) == "2120")
print(hw4_part1.int_to_base(299,14) == "175")
print(hw4_part1.int_to_base(122870876,15) == "abc12bb")

print(hw4_part1.base_to_base("abc12bb",14,15) == "728532c")
print(hw4_part1.base_to_base("a4bb30153",12,8) == "41275163717")
print(hw4_part1.base_to_base("a4bb53c12007",13,11) == "5a20874838753")
print(hw4_part1.base_to_base("2043112",5,2) == "1000010101101101")
print(hw4_part1.base_to_base("122001002",3,7) == "51134")
