'''
	[문제]	  	
		철수는 현금 10000원을가지고 마트에갔다.
		사과한개의 가격은 200원이고, 귤한개의 가격은  110원이다. 
		사과 3개 와 귤 10개를 사려고 한다 .  
		모두 사면 거스름돈은 얼마인지 구하시오.
	[정답]
		8300
'''
print("240801TH")

cash = 10000

UNIT_PRICE_APPLE = 200
UNIT_PRICE_TANGERINE = 110

cash -= 3 * UNIT_PRICE_APPLE
cash -= 10 * UNIT_PRICE_TANGERINE

print(cash)

