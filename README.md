회원 인증 카테고리 기능이있는 간단한 게시판입니다.
=======
사용 기술
=====
- django
- background_tasks
- vanila javascript
- bootstrap3


 사용법
============
1. DB_NAME DB_USER DB_PASSWORD 환경변수 설정후
3. python manage.py migrate
4. django admin 에서 Category 추가
5. 글을 작성하려면 해당 유저 profile status가 true 상태여야합니다.
6. localhost:8000/board/로 접속

#### postgres db로 세팅되어있습니다.



![alt text](https://github.com/dizzyplay/djangoboard/blob/master/readme_image/1.png)