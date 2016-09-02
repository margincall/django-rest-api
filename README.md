# django-rest-api

An api server based on token authentication including facebook OAuth2

## Getting Started

#### Environment Setting
```
virtualenv YOUR_VIRTUALENV_NAME
source YOUR_VIRTUALENV_NAME/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

#### Run Server
```
python manage.py runserver
```

## References
>  
Django 1.9.9 : https://pypi.python.org/pypi/Django/1.9.9  
DjangoRestFramework : http://www.django-rest-framework.org/  
QuickStart Guide : http://www.django-rest-framework.org/tutorial/quickstart/  

## (PyCharm 기준) 개발 환경 세팅 가이드

//그는 간지나게 도커를 써보고 싶었지만 아직 쓸 줄 모른다고 한다

### 요약
1. Python3.5, PyCharm 설치
1. git clone
1. venv 설정 & requirements 설치
1. PyCharm Django 실행 환경 세팅
1. db migration
1. PyCharm Django Test 환경 세팅

### Step by Step
1. 시작 전에 필요한 것
    - Python3.5
        - 맥 : `brew install python3`
        - Debian 계열 : `apt-get install python3`
        - python3로 버전을 확인합시다.
        (저는 3.3이 깔려서 `brew upgrade python3`가 필요했음)
    - PyCharm

1. PyCharm 실행
1. GitHub에서 clone
    1. (설치 후 첫 실행 기준)`Checkout from Version Control` > `GitHub`

1. Python Interpreter 가상 환경 설정
    1. 상단메뉴 `PyCharm` > `Preferences`
    (Win/Linux 버전은 `Files` > `Settings`)
    1. `Project: django-rest-api` > `Project Interpreter`
    1. `Project Interpreter:`의 드롭다운 메뉴 우측의 `설정(톱니바퀴) 아이콘`에서
    `Create VirtualEnv` 클릭
    1. 이름 정하고(e.g. `venv-3000won`), `OK`
    1. `OK`를 눌러서 Preferences(or Settings)창 닫아줌
    1. PyCharm이 혼자서 지지고 볶는 동안 느긋하게 기다림

1. PyCharm Django Support
    1. `Preferences` > `Languages & Frameworks`
    1. `Django`에서 `Enable Django Support` 체크
    1. `Django project root:`는 clone 받은 프로젝트의 root,
    `Settings`는 프로젝트에서 `threethousandwon/settings.py` 선택
    1. `OK`

1. Django runserver 실행 환경
    1. 우상단의 녹색 실행아이콘(`▶`) 왼쪽의 드롭다운 메뉴(또는 상단 메뉴의 `Run`) 선택
    1. `Edit Configurations...`
    1. 좌상단의 `+` 아이콘(Add New Configuration) > `Django Server`
    1. 실행 환경 이름을 `local-django-runserver`로 바꿔줌
    1. `OK`
    1. Django가 안 깔려있다고 경고문 띄우면서 징징대지만, 일단 무시

1. 필요한 패키지 설치
    1. 프로젝트 내에서 아무 `.py` 코드 파일을 열면,
    위에 `Packae reqirements (어쩌고 저쩌고)`라고 뜸
    1. 경고문 우측의 `Install requirements`
    (이 방법이 간편해서 개인적으로 좋아함)
    1. PyCharm이 또 열심히 알아서 하는 동안 맥주 한 잔

1. 여기까지 성공 확인
    1. `▶` 클릭
    1. 밑의 Run 창에서 주소를 클릭하면 브라우저로 열림

1. DB Migration
    1.  `Tools` > `Run manage.py Task…`
    (왜 터미널에서 직접 안 하느냐면, 가상환경이라서 python 경로가 개떡같기 때문.
    ~/sth/venv/bin/python3 같은 걸 호출해야 한다. 이걸로 하면 편함)
    1. `migrate` 엔터

1. Test 환경 세팅
    1. `Run` > `Edit Configurations...` > `+` > `Django tests`
    1. 이름 변경(e.g. `test`)
    1. 우상단 드롭다운에서 `test`를 선택한 뒤, 실행(`▶`)하면 화면 하단에 녹색바가 뜸
    1. `All Tests Passed`라고 왼쪽에 적혀 있으니 뿌듯해하면 된다

1. 끝