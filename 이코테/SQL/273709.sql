# 조건에 맞는 아이템들의 가격의 총합 구하기
SELECT SUM(PRICE) as TOTAL_PRICE
FROM ITEM_INFO
WHERE RARITY = 'LEGEND'