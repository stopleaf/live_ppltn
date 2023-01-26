# 서울시 실시간 도시 데이터 수집 

### 내용
    Airflow, Kafka, MongoDB 학습 목적

### 목표
    OpenAPI 데이터 수집 -> Kafka -> MongoDB -> ETL -> ...
    
### 진행 상황
    O분마다 OpenAPI 데이터 수집 후 Kafka에 메시지 전송
    O분마다 Kafka에서 메시지 꺼내어 MongoDB에 저장 

### 문제 해결
    1. Kafka 메시지 중복 소비
        원인: Kafka consumer 오프셋 커밋이 안되고 있었음
        해결: consumer 옵션 중 enable_auto_commit를 False로 변경하고, .commit 명령어를 추가

### 버전 관리
    ver 0.0.1 서울시 인구밀집지역 데이터 수집 테스트 코드 생성
    ver 0.0.2 서울시 실시간 도시 데이터 수집으로 변경 및 Kafka 테스트
    ver 0.0.3 Airflow로 1분 마다 데이터 수집 테스트
    ver 0.0.4 kafka produce, consumer 코드 수정