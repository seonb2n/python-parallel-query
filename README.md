# python-parallel-query
파이썬 코드로 db session 을 병렬 처리해서 쿼리를 실행할 수 있도록 구현했다.

- 파이썬과 postgresql 사이에 db connection 에 사용되는 psycopg2 는 하나의 DB connection 으로 쓰레드간 병렬 세션을 허용하지 않는다.
- 따라서, 각각의 쓰레드마다 독립적으로 db connection 을 맺어줘야 한다.
- Postgresql 에서는 테이블 insert 시 별개의 행에 대해서는 lock 이 걸리지 않기 때문에 여러 커넥션에서 insert 를 실행해도 괜찮다.
