# 마리아 DB 모듈 가져오기
import mysql.connector as mariadb

# DB 접속 및 커서 오픈
mariadb_connection = mariadb.connect(user="MariaUser1", password='xxxxx', database='pythondb')
cursor = mariadb_connection.cursor()

# 레코드 입력
cursor.execute("INSERT INTO samletb1(ID, NAME) VALUES(%d, %s);", (1004, 'MariaName'))

# 레코드 조회
cursor.execute("SELECT * FROM samletb1;")

# 레코드 변경
cursor.execute("UPDATE samletb1 SET NAME = 'TEST' WHERE ID = 1004;")

# 레코드 삭제
cursor.execute("DELETE FROM samletb1 WHERE ID = 1004;")

# 데이터 반영
mariadb_connection.commit();

# 연결 종료
mariadb_connection.close();
