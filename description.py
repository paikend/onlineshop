# 배포
# 1. EC2 인스턴스 생성
# 2. Nginx 설치 (웹서버)
# 3. 소스코드 업로드 - 사용자, 그룹, 해당 소스코드를 업로드할 폴더 설정
# 3-1. requirements.txt
# 4. 가상환경 설정 - venv 파이썬 모듈
# 4-1. runserver로 구동되는지 확인 - python manage.py runserver 0:8000

# 5. 가상 환경 안에 uwsgi 모듈 설치
# 5-1. uwsgi로 구동되는지 꼭 확인!
# 6. uwsgi.ini 파일 만들기
# 7. uwsgi.service 시작프로그램 만들기
# 8. site-available 폴더에 onlineshop 설정 파일 만들기
# 8-1. 내용 수정 -> for django, uwsgi
# 9. onlineshop -> 심볼릭링크 -> site-enabled
# 10. hash_bucket_site => 128 변경
# 11. Nginx 재시작
