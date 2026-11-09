# Practical Walkthrough: Azure AI & RAG Backend

This guide walks you through deploying an enterprise-grade Retrieval-Augmented Generation (RAG) backend using FastAPI and Azure AI.

## Stage 1: Infrastructure Deployment
1. Open terminal and log into Azure: `az login`.
2. Navigate to `02-azure-data-platform/infrastructure` and run:
   `az deployment group create --resource-group YOUR_RG --template-file main.bicep`
3. Open the Azure Portal. Verify that **Azure OpenAI** and **Azure AI Search** have been provisioned.

## Stage 2: Model Configuration
1. Open **Azure AI Studio** (`aistudio.azure.com`).
2. Navigate to your deployed OpenAI resource. Click **Deployments** > **Create new deployment**.
3. Deploy `text-embedding-ada-002` (Name it exactly this).
4. Deploy `gpt-4o` (Name it `gpt-4o`).
* **Verification:** Test the deployment in the AI Studio Chat Playground.

## Stage 3: Running the FastAPI Service
1. Open this repository in VS Code.
2. Open terminal and create a virtual environment: `python -m venv .venv`
3. Activate it: `.\.venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (Mac/Linux).
4. Install dependencies: `pip install fastapi uvicorn openai azure-search-documents`
5. Create a `.env` file in `05-azure-ai-and-rag/src/rag` containing your Azure endpoints and keys.
6. Run the server: `uvicorn main:app --reload`
* **Verification:** Open your browser to `http://localhost:8000/docs`. You will see the Swagger UI. Use the `/ask` endpoint to submit a query and receive a grounded response.
