# Enterprise Security Architecture

## Network Security
* Utilize **Azure Private Endpoints** for ADLS Gen2, Azure SQL, and Azure Key Vault to disable public internet access.
* Deploy **On-Premises Data Gateway** for secure ingestion from legacy on-prem databases.

## Privacy-by-Design
* Implement **Dynamic Data Masking (DDM)** in Azure SQL to obfuscate PII (e.g., `XXX-XXX-1234`).
* Apply **Row-Level Security (RLS)** in Power BI and Fabric to restrict data access based on Entra ID regional group membership.
