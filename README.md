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
  - [2021.07.10] 
    - 빠른 개발을 위한 DRF 다루기
    - `model`과 `manager` 분리  
  - [2021.06.19] 비즈니스 로직의 분리
