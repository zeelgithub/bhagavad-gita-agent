from langchain_core.tools import tool


def create_bhagavad_gita_tool(vector_store, number_of_retrieved_docs: int = 3):

    retriever = vector_store.as_retriever(
        search_kwargs={"k": number_of_retrieved_docs})

    @tool
    def bhagavad_gita_tool(query: str) -> str:
        """Use this tool to answer questions about the Bhagavad Gita"""
        result = retriever.invoke(query)
        return "\n".join([doc.page_content for doc in result])

    return bhagavad_gita_tool
