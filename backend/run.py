from app.index import get_index

question = "What is SR22?"

index = get_index()
query_engine = index.as_query_engine()
response = query_engine.query(question)
sources = list({v['Source'] for v in response.metadata.values()})

print(str(response))

for i, s in enumerate(sources):
    print(f'Source {i + 1}: {s}')