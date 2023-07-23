-- 코드를 입력하세요
SELECT board_id, writer_id, title, price, 
case when STATUS="DONE" then "거래완료"
    when STATUS="SALE" then "판매중"
    else "예약중"
    end STATUS

from USED_GOODS_BOARD 
where date_format(created_date,"%Y-%m-%d") = "2022-10-05"
order by board_id desc