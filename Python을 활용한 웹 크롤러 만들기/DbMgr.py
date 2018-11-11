# 디비 처리class, 연결, 해제, 검색어 가져오기, 데이터 삽입
import pymysql as my

class DBHelper:
    '''
    맴버변수 : 커넥션
    '''
    conn = None
    '''
    생성자
    '''
    def __init__(self):
        self.db_init()
    '''
    맴버 함수
    '''
    def db_init(self):
        self.conn = my.connect(
                        host='localhost',
                        user='root',
                        password='404040',
                        db='pythonDB',
                        charset='utf8',
                        cursorclass=my.cursors.DictCursor # 커리를 쳤을 때 나오는 결과를 파이썬의 딕셔너리 형식으로 뽑아줌, 안 쓰면 튜플
        )
    def db_free(self):
        if self.conn:
            self.conn.close()
    
    # 검색 키워드 가져오기 -> 웹에서 검색
    def db_selectKeyword(self):
        # 커서 오픈(커넥션부터 커서를 오픈한다.)
        # with -> 닫기 처리를 자동으로 하니까 -> I/O 많이 사용
        rows = None
        with self.conn.cursor() as cursor:
            sql = "select * from tbl_keyword;"
            cursor.execute(sql)
            rows = cursor.fetchall()
            print(rows)
        return rows
        
    def db_insertCrawlingData(self, title, price, date, contents, keyword):
        with self.conn.cursor() as cursor:
            sql = '''
            insert into `tbl_crawlingdata` 
            (title, price, date, contents, keyword) 
            values(%s, %s, %s, %s, %s)
            '''
            cursor.execute(sql, (title, price, date, contents, keyword))
        self.conn.commit()
        
# 단독으로 수행시에만 작동 -> 테스트코드를 삽입해서 사용
if __name__=='__main__':
    db = DBHelper()
    print(db.db_selectKeyword())
    print(db.db_insertCrawlingData('1','2','3','4','5'))
    db.db_free()