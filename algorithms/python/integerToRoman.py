#coding=utf-8

import sys

#相同的数字连写，所表示的数等于这些数字相加得到的数，如 Ⅲ=3；
#小的数字在大的数字的右边，所表示的数等于这些数字相加得到的数，如 Ⅷ=8、Ⅻ=12；
#小的数字（限于 Ⅰ、X 和 C）在大的数字的左边，所表示的数等于大数减小数得到的数，如 Ⅳ=4、Ⅸ=9；
#在一个数的上面画一条横线，表示这个数增值 1,000 倍，如=5000。
#V 和 X 左边的小数字只能用 Ⅰ
#L 和 C 左边的小数字只能用X
#D 和 M 左边的小数字只能用 C
# 4 : IV  9: IX   40: XL  90:XC  400:CD 900:CM
def intToRoman(num):
	rdic = {1 : 'I', 5 :'V', 10 : 'X', 50 : 'L', 100 : 'C',  500 : 'D', 1000 : 'M'}

	result = ''
	thousand = num / 1000
	if thousand > 0:
		result += 'M' * thousand
		num -= 1000 * thousand

	hundred = num / 100
	if hundred > 0:
		num -= 100 * hundred
		result += convert('C', 'D','M', hundred)

	ten = num/10
	if ten > 0:
		num -= 10*ten
		result += convert('X', 'L','C', ten)

	zero = num % 10
	result += convert('I', 'V','X', zero)

	return result

def convert(i,v,x, num):
	if num == 9:
		return i+x
	if num > 5:
		return v + (num-5)*i
	if num == 5:
		return v
	if num == 4:
		return i + v
	if num > 0:
		return i * num
	return ''


if __name__ == '__main__':
	if len(sys.argv) > 1:
		print intToRoman(int(sys.argv[1]))
