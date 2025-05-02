import os
from dotenv import load_dotenv
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import chromadb
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from typing import List
import cohere

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
cohere_api_key = os.getenv("cohere_api_key")

# Initialize Cohere client
co = cohere.Client(cohere_api_key)

CHROMA_DB_PATH = "/home/tanisha.ramani@simform.dom/Desktop/github-posts/daily-tasks/complete_chromadb_nhs"
COLLECTION_NAME = "nhs_conditions"

def setup_vector_store(load_only=True):
    embedding_model = OpenAIEmbeddings(
        model="text-embedding-ada-002",
        openai_api_key=openai_api_key
    )

    chroma_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
    collection = chroma_client.get_or_create_collection(name=COLLECTION_NAME)

    vectorstore = Chroma(
        client=chroma_client,
        collection_name=COLLECTION_NAME,
        embedding_function=embedding_model,
        persist_directory=CHROMA_DB_PATH  
    )

    if load_only:
        print(" Loaded vectorstore from disk.")
        return vectorstore

    print(" Initialized vectorstore.")
    return vectorstore

def ingest_uploaded_files_in_rag(file_paths: List[str]):
    embedding_model = OpenAIEmbeddings(
        model="text-embedding-ada-002",
        openai_api_key=openai_api_key
    )
    chroma_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
    vectorstore = Chroma(
        client=chroma_client,
        collection_name=COLLECTION_NAME,
        embedding_function=embedding_model,
        persist_directory=CHROMA_DB_PATH
    )

    docs = []

    for file_path in file_paths:
        loader = UnstructuredMarkdownLoader(file_path)
        loaded_docs = loader.load()
        for doc in loaded_docs:
            doc.metadata["source"] = file_path
        docs.extend(loaded_docs)

    print(f" Loaded {len(docs)} new uploaded documents.")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        separators=["\n\n", "\n", ".", "!", "?", " ", ""]
    )
    chunks = splitter.split_documents(docs)
    print(f" Split into {len(chunks)} chunks.")

    BATCH_SIZE = 150
    for i in range(0, len(chunks), BATCH_SIZE):
        batch = chunks[i:i + BATCH_SIZE]
        try:
            vectorstore.add_documents(batch)
            print(f" Inserted batch {i // BATCH_SIZE + 1} with {len(batch)} documents.")
        except Exception as e:
            print(f" Error during batch insertion: {e}")

    print(" Uploaded documents successfully ingested.")

def get_qa_chain(vectorstore):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
    llm = ChatOpenAI(
        model_name="gpt-4o",  # or "gpt-3.5-turbo"
        temperature=0,
        openai_api_key=openai_api_key
    )

    # Define the prompt template
    prompt_template_str = """
        
        You are a friendly, supportive, and helpful medical assistant. Your role is to answer health-related questions using information from retrieved document chunks. Your goal is to provide accurate, kind, and easy-to-understand responses, while making users feel heard, supported, and informed.

        Follow these principles without exception:

        - **Warm Conversational Tone**: Greet users warmly and respond to personal statements empathetically (e.g., “Hi”, “I feel upset”). Maintain a natural, kind dialogue.
        - **Simple and Compassionate Language**: Use clear, friendly, and reassuring language, especially when explaining medical information.
        - **Context Awareness**: Remember user details across interactions using memory. If someone shares they're in pain, check in gently later.
        - **Emotional Sensitivity**: Acknowledge feelings and respond with emotional care, especially when users are anxious, confused, or upset.
        - **Use of Memory**: Leverage LangChain memory to recall and reference user-specific information across turns when helpful.

        - **Factual Discipline**:
            - Only use information found in the retrieved document chunks.
            - Never guess, assume, or fabricate information that isn’t supported by the context.
            - If unsure, say kindly: "I want to be as accurate as possible, and I don't have enough information from the documents I saw. But I’m here if you’d like to ask about something else."

        - **Helpful but Honest**: Being transparent about what’s known or unknown shows care. Don't speculate.

        - **Answering Strategy**:
            - If the answer is **clearly stated** in the documents: explain it gently and simply.
            - If the documents include **partially relevant info**: summarize helpfully without adding unsupported details.
            - If the documents provide **no useful info**: use the fallback response above.

        - **Formatting & Clarity**:
            - Use short paragraphs.
            - Use bullet points where it improves readability.
            - Avoid unexplained medical jargon.

        Always aim to be:
        - Factually correct
        - Compassionate
        - Easy to understand
        - Supportive, even when unable to give an answer

        Your responsibility is to offer care, clarity, and honesty—never speculation.
                
        Context:
        {context}

        Question:
        {question}

        Answer:
        """

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=prompt_template_str.strip()
    )

    # Create the chain with the custom prompt
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",  # use "stuff" for simple prompt+context formatting
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True
    )

    return qa_chain, retriever


def rerank_results(query, retrieved_docs, top_n=5):
    doc_texts = [doc.page_content for doc in retrieved_docs]

    response = co.rerank(query=query, documents=doc_texts, model="rerank-english-v3.0", top_n=top_n)

    ranked_docs = sorted(zip(response.results, retrieved_docs), key=lambda x: x[0].relevance_score, reverse=True)

    return [doc for _, doc in ranked_docs[:top_n]]

def run_query(qa_chain, retriever, query):
    # try:
        retrieved_docs = retriever.get_relevant_documents(query)
        reranked_docs = rerank_results(query, retrieved_docs, top_n=5)

        embedding_model = OpenAIEmbeddings(
            model="text-embedding-ada-002",
            openai_api_key=openai_api_key
        )
        query_embedding = embedding_model.embed_query(query)
        query_embedding_np = np.array(query_embedding).reshape(1, -1)

        ranked_chunks = []
        for i, doc in enumerate(reranked_docs):
            content = doc.page_content
            filename = os.path.basename(doc.metadata.get("source", ""))
            snippet = content.strip().replace("\n", " ")[:300]

            doc_embedding = embedding_model.embed_query(content)
            doc_embedding_np = np.array(doc_embedding).reshape(1, -1)
            similarity_score = cosine_similarity(query_embedding_np, doc_embedding_np)[0][0]
            score = round(float(similarity_score), 3)

            ranked_chunks.append({
                "chunk_number": i + 1,
                "file": filename,
                "snippet": snippet,
                "similarity_score": score
            })

        response = qa_chain.invoke({"query": query})
        final_answer = response["result"]
        source_filename = None

        if response.get("source_documents"):
            source_doc = response["source_documents"][0]
            source_filename = os.path.basename(source_doc.metadata.get("source", ""))

        return {
            "query": query,
            "chunks": ranked_chunks,
            "final_answer": final_answer,
            "source_document": source_filename
        }

    # except Exception as e:
    #     return {
    #         "error": str(e),
    #         "query": query
    #     }

def main():
    print("Setting up vectorstore...")
    vectorstore = setup_vector_store(load_only=True)

    print("\n Initializing QA chain...")
    qa_chain, retriever = get_qa_chain(vectorstore)

    query = "what is acupuncture and how does it works?"
    result = run_query(qa_chain, retriever, query)

    print("\n" + "-" * 80)
    print(f"🔍 QUERY: {result.get('query', '')}")
    print("-" * 80)

    if "error" in result:
        print(f"❌ Error: {result['error']}")
        return
    print(f"\n📚 Retrieved {len(result['chunks'])} document chunks:")
    for chunk in result["chunks"]:
        print(f"\n--- Chunk {chunk['chunk_number']} ---")
        print(f"📄 File: {chunk['file']}")
        print(f"🧩 Snippet: {chunk['snippet']}")
        print(f"🔍 Similarity Score: {chunk['similarity_score']}")

    print("\n" + "-" * 80)
    print("🧠 FINAL ANSWER:")
    print("-" * 80)
    print(result["final_answer"])

    if result["source_document"]:
        print("\n📄 Source Document Used:")
        print(f"- {result['source_document']}")
    else:
        print("\n⚠️ No source documents found.")

    print("-" * 80 + "\n")

if __name__ == "__main__":
    main()

