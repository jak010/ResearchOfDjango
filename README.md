## Research Of Django

- DRF 에 관한 고찰

## Policy

- 모든 API는 JWT를 발급받고 인증을 통해 접근해야 한다.

## Current API

- `authenticate/login`
    - jwt 토큰 발급용 api

## Settings

- `DATABASE`
    - `System`
        - `MySQL 5.7`
    - `config/settings.py`
    ```text
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'research',
                'USER': 'root',
                'PASSWORD': '1234',
                'HOST': '127.0.0.1',
                'PORT': '3306',
            }
        }
    ```

## Topic

- `[2021.08.16]`
    - url path 변수를 두 개이상 사용할 때 본 action 데코레이터를 이용하자
- `[2021.08.15]`
    - 비로그인 유저가 글을 등록할 때의 계정처리 생각해보기, viewset을 구조 사용해보기
- `[2021.08.13]`
    - Project 생성 시에는 Project 이름을 config 로 줘서 환경설정에 관련된 디렉토리임을 명시적으로 둬야함
    - jwt를 발급하고 API에 접근할 때 어떻게 오픈할 지 생각해보기
- `[2021.07.19]`
    - JWT 를 쓰려면 Token Claims의 내용을 고려해보자
- `[2021.07.18]`
    - Rest API Response 구조는 어떤 식으로 가져갈 지 고민해보는 게 좋을 듯
- `[2021.07.11]`
    - Response는 관리 포인트를 하나로 두는 것이 좋을 듯
    - ~~Serializer보다는 Service라는 워딩으로~~
    - Rest FrameWork에서 CBV로 권한관리를 하고 싶으면 커스터마이징 해야됨
- `[2021.07.10]`
    - 빠른 개발을 위한 DRF 다루기
    - `model`과 `manager` 분리
- `[2021.06.19]`
    - 비즈니스 로직의 분리

## ToDo

- CBV에서 메소드별 권한 관리 방법 고찰

## Django Official Document Link

- `import 순서에 관한 링크`
    - https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/