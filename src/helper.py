from src.qa_chain import qa_chain

def get_response(query: str) -> str:
    response = qa_chain.invoke(query)
    return response['result']
