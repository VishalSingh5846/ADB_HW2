
DROP TABLE IF EXISTS TRADE;

CREATE TABLE TRADE(Time int, Symbol int, Quantity int, Price int);

LOAD DATA LOCAL INFILE 'trade.txt'
INTO TABLE TRADE FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
(Time, Symbol , Quantity, Price);
CREATE INDEX index1 ON Trade (Time);


SELECT SUM(Price * Quantity) / SUM(Quantity) from TRADE GROUP BY SYMBOL;


Select Time, Symbol, Quantity, Price, Q2,P2, SUM(P2 * Q2) / SUM(Q2) FROM ( Select T1.*,T2.Price as P2,T2.Quantity as Q2 from Trade T1, Trade T2 WHERE T2.Time BETWEEN T1.Time-9 AND T1.Time AND T2.Symbol = T1.Symbol ) TX GROUP BY Symbol,Time ORDER BY Symbol,Time


SELECT *, (SELECT AVG(PRICE) FROM Trade WHERE Symbol = T1.Symbol AND Time <= T1.Time ORDER BY Time DESC LIMIT 10) AS MovAvg FROM Trade T1;


SELECT *, (SELECT SUM(Price * Quantity) / SUM(Quantity) FROM Trade WHERE Symbol = T1.Symbol AND Time <= T1.Time ORDER BY Time DESC LIMIT 10) AS MovAvgWeighted FROM Trade T1 ORDER BY Symbol, Time;


SELECT Symbol, MAX(Price - MinPrice) from  (select T1.Time,T1.Symbol,T1.Price,(select MIN(Price) from Trade where Time<=T1.Time AND T1.Symbol = Symbol)  AS MinPrice from Trade T1 ORDER BY Symbol,Time ) T2 GROUP BY Symbol; 




