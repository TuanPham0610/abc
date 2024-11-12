-- 1. Truy vấn ra 10 quốc gia có GDP trên đầu người cao nhất

SELECT country, region, (gpd/population*1000000) AS gdp_per_capita --- vì population có đơn vị là triệu người
FROM olympics
ORDER BY gdp_per_capita DESC
LIMIT 10;

-- 2. Đưa ra 5 quốc gia có tổng số huy chương nhiều nhất

SELECT * 
FROM olympics
ORDER BY total DESC
LIMIT 5;

-- 3. Phân tích thành tích Olympic theo từng châu lục để hiểu rõ sự phân bố thành tích theo khu vực

SELECT region, SUM(gold) AS total_gold, SUM(silver) AS total_silver, SUM(bronze) AS total_bronze
FROM olympics
GROUP BY region
ORDER BY total_gold DESC;

-- 4. Tìm ra các quốc gia có hiệu quả thành tích Olympic cao so với dân số và GDP

SELECT country, (total / population) AS medals_per_million, gdp
FROM olympics
ORDER BY gdp DESC
LIMIT 10;
