## Research Of Django
 - Develop 에 관한 고찰

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
  - `[2021.07.11]`
    - Response는 관리 포인트를 하나로 두는 것이 좋을 듯
    - Serializer보다는 Service라는 워딩으로
    - Rest FrameWork에서 CBV로 권한관리를 하고 싶으면 커스터마이징 해야됨  
  - `[2021.07.10]` 
    - 빠른 개발을 위한 DRF 다루기
    - `model`과 `manager` 분리  
  - `[2021.06.19]`
    - 비즈니스 로직의 분리

## ToDo
  - CBV에서 메소드별 권한 관리가 되는지 조사