CREATE DATABASE graDB CHARACTER SET utf8 COLLATE utf8_general_ci;

CREATE USER 'gra'@'localhost' IDENTIFIED BY 'Seoulit22@';
GRANT ALL ON graDB.* TO 'gra'@'localhost' WITH GRANT OPTION;



학생테이블
CREATE TABLE stutbl 
( 학번  	INT NOT NULL PRIMARY KEY,
  이름    	VARCHAR(10) NOT NULL,
  주소	  CHAR(2) NOT NULL,
  학과코드  CHAR(8) NOT NULL
);

FOREIGN KEY (학과코드) REFERENCES subtbl(과목명) ON UPDATE CASCADE
CREATE UNIQUE INDEX idx_stutbl_tel ON stutbl(stutel)

INSERT INTO stutbl VALUES(1011, '홍길동', '서울', 'C1234');
INSERT INTO stutbl VALUES(1012, '이순신', '경기', 'C1234');
INSERT INTO stutbl VALUES(1013, '박지성', '강원', 'C5678');
INSERT INTO stutbl VALUES(1014, '김연아', '경남', 'C0000');
INSERT INTO stutbl VALUES(1015, '박찬호', '제주', 'C0000');

ALTER TABLE stutbl
CHANGE COLUMN 학번 Num INT NOT NULL ;


과목테이블
CREATE TABLE subtbl 
( 과목코드  CHAR(3) NOT NULL PRIMARY KEY,
  과목명  CHAR(8) NOT NULL,
  과목개요  CHAR(8) NOT NULL
);
INSERT INTO subtbl VALUES('AAA', '자바','');
INSERT INTO subtbl VALUES('BBB', '오라클','');
INSERT INTO subtbl VALUES('CCC', 'php','');
INSERT INTO subtbl VALUES('DDD', 'html','');

학과(전공)테이블
CREATE TABLE majortbl 
( 학과코드  CHAR(5) NOT NULL PRIMARY KEY,
  학과명  CHAR(8) NOT NULL,
  전화번호  CHAR(11) NOT NULL
);
INSERT INTO majortbl VALUES('C1234', '컴퓨터공학과','');
INSERT INTO majortbl VALUES('C5678', '전자공학과','');
INSERT INTO majortbl VALUES('C0000', '기계공학과','');


수강테이블
CREATE TABLE lectbl 
( 수강코드 	INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
  학번  	INT NOT NULL,
  과목코드  CHAR(3) NOT NULL,
  수강신청일  DATE,
 FOREIGN KEY (과목코드) REFERENCES subtbl(과목코드)
);
INSERT INTO lectbl VALUES(NULL, 1011, 'AAA', '2018-11-12');
INSERT INTO lectbl VALUES(NULL, 1011, 'BBB', '2018-11-13');
INSERT INTO lectbl VALUES(NULL, 1011, 'CCC', '2018-11-14');
INSERT INTO lectbl VALUES(NULL, 1013, 'AAA', '2018-11-15');
INSERT INTO lectbl VALUES(NULL, 1013, 'DDD', '2018-11-16');

- 인덱스 조회
SHOW INDEX FROM 테이블명

- 인덱스 상태
SHOW TABLE STATUS LIKE '테이블명';

Data_length : 클러스터형(기본키) 인덱스 포함한 데이터 크기
Index_length : 보조 인덱스 크기(찾아보기 공간)

- 인덱스 생성

CREATE INDEX index_name
ON table_name (column1, column2, ...);

CREATE INDEX idx_userTbl_addr 
   ON usertbl1 (addr);
ANALYZE TABLE usertbl1; ==> 인덱스 적용

CREATE UNIQUE INDEX idx_userTbl_name
 ON usertbl1 (name);

select name from usertbl where name='김범수'
INSERT INTO userTbl1 VALUES('KKK', '김범수', 1979, '경남', '011', '2222222', 173, '2012-4-4');

SHOW GLOBAL STATUS LIKE 'Innodb_pages_read'; --읽은 페이지 수

SELECT * FROM Emp_Se WHERE emp_no = 100000;

SHOW GLOBAL STATUS LIKE 'Innodb_pages_read';

SELECT * FROM Emp_C WHERE emp_no < 11000;



