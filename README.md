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

- `DELETE /category/{id}`: 북마크 카테고리 제거

  - Response

  ```json
  {
    "isDeleted": true // 삭제 성공 여부
  }
  ```

- `GET /bookmark?categoryId=<categoryId>`: 북마크 목록 조회

  - `categoryId` 쿼리 파라미터가 주어질 경우 카테고리 ID로 북마크 검색

  - Response

  ```json
  [
    {
      "id": "<북마크 ID>",
      "name": "<북마크 이름>",
      "url": "<북마크 URL>",
      "categories": [
        {
          "id": "<카테고리 ID>",
          "name": "<카테고리 이름>"
        }
      ]
    }
  ]
  ```

- `POST /bookmark`: 북마크 생성

  - Request

  ```json
  {
    "name": "<북마크 이름>",
    "url": "<북마크 URL>",
    "categoryIds": [ "<카테고리 ID>" ]
  }
  ```

  - Response

  ```json
  {
    "id": "<북마크 ID>",
    "name": "<북마크 이름>",
    "url": "<북마크 URL>",
    "categoryIds": [
      {
        "id": "<카테고리 ID>",
        "name": "<카테고리 이름>"
      }
    ]
  }
  ```

- `DELETE /bookmark/{id}`: 북마크 제거

  - Response

  ```json
  {
    "isDeleted": true // 삭제 성공 여부
  }
  ```
