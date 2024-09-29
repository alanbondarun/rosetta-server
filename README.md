# Rosetta-server: Rosetta stone of server projects

## Goal

- 동일한 기능을 하는 서버 구현체를 비교

## Server Requirements

- `GET /category?name=<name>`: 북마크 카테고리 목록 조회

  - `name` 쿼리 파라미터가 주어질 경우 이름으로 카테고리 검색

  - Response

  ```json
  [
    {
      "id": "<카테고리 ID>",
      "name": "<카테고리 이름>"
    }
    // ...
  ]
  ```

- `POST /category`: 북마크 카테고리 생성

  - Request

  ```json
  {
    "name": "<카테고리 이름>"
  }
  ```

  - Response

  ```json
  {
    "id": "<카테고리 ID>",
    "name": "<카테고리 이름>"
  }
  ```
