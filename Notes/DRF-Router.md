## DRF, Route에 관한 노트 

- `Declare`
    ```python
     from rest_framework.routers import *
    ```

- `SimpleRouter`
  - list, create, retrieve, update, partial_update, destroy 표준 set 작업에 대한 경로가 포함
  - 기본적으로 SimpleRouter로 만든 URL 뒤에는 슬래시가 추가됩니다.
  - 이 동작은 라우터를 인스턴스화 할때 trailing_slash 인수를 False로 설정하여 수정 가능
