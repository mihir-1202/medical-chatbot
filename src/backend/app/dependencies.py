from langchain_pinecone import PineconeVectorStore
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
import os
import dotenv

dotenv.load_dotenv()
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')

def get_retrieval_chain():
    """
    Creates the retrieval chain for QA.
    """
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": 'cpu'}
    )
    vector_store = PineconeVectorStore.from_existing_index(index_name = 'medical-chatbot', embedding = embeddings)
    retriever = vector_store.as_retriever()
    
    llm_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    
    system_prompt = (
        "You are a helpful medical assistant. Answer the user's question based on the information "
        "provided in the context. Keep your answers concise and to the point. "
        "This is the context for you to base your answer on: {context}"
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}")
    ])
    
    #creates a chain that takes the documments and stuffs them all into the prompt as context
    document_chain = create_stuff_documents_chain(llm_model, prompt)

    #creates a chain that takes the gets relevant documents from the retriever and passes it to the document chain as context
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    
    return retrieval_chain


