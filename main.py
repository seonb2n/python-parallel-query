import psycopg2
from concurrent.futures import ThreadPoolExecutor


def connect_db():
    # PostgreSQL 연결 정보 설정
    conn = psycopg2.connect(
        host="your_host",
        database="your_database",
        user="your_user",
        password="your_password"
    )
    return conn


# 특정 쿼리 실행 함수
# psycopg2 는 병렬 세션을 지원하지 않기 때문에 여러 스레드에서 각각 db connection 을 생성해줘야 한다.
def execute_query(query):
    conn = connect_db()
    with conn.cursor() as cur:
        cur.execute(query)
        result = cur.fetchall()
    conn.close()
    return result

# 병렬 쿼리 실행 함수
def parallel_query(queries):
    with ThreadPoolExecutor() as executor:
        results = executor.map(execute_query, queries)
    return list(results)

# 테스트용 쿼리 리스트
queries = [
    "SELECT * FROM table1",
    "SELECT * FROM table2",
    "SELECT * FROM table3",
    # 추가 쿼리 추가 가능
]

# 병렬 쿼리 실행
query_results = parallel_query(queries)

# 결과 출력
for query, result in zip(queries, query_results):
    print(f"Query: {query}")
    print("Result:")
    for row in result:
        print(row)
    print()
