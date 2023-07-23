-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, 
CASE WHEN sex_upon_intake like "%Neutered%" Then "O"
     WHEN sex_upon_intake like "%Spayed%" Then "O"
     ELSE "X"
     END
     as 중성화
from animal_ins
order by ANIMAL_ID