# 상품 정보를 담는 클래스
# DB에 넣는 플랫폼까지 고려
class TourInfo:
    # 멤버변수(실제 컬럼보다는 작게 셋팅)
    title = ''
    price = ''
    area = ''
    link = ''
    img = ''
    # 생성자
    def __init__(self, title, price, date, link, img):
        self.title = title
        self.price = price
        self.date = date
        self.link = link
        self.img = img