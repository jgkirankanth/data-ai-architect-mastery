# Architecture Patterns: Data Vault vs Dimensional

## Data Vault 2.0 (Enterprise Scalability)
Best for: Highly volatile source systems, massive scale integration.
* **Hubs:** Business keys (e.g., `Hub_Customer`).
* **Links:** Relationships between Hubs (e.g., `Link_Customer_Account`).
* **Satellites:** Context and descriptive attributes (e.g., `Sat_Customer_Demographics`).

## Dimensional / Star Schema (Serving Layer)
Best for: Direct querying by Power BI, fast aggregation.
* **Fact Tables:** Quantitative metrics (e.g., `Fact_Sales`).
* **Dimension Tables:** Descriptive attributes (e.g., `Dim_Date`, `Dim_Product`).

*Decision:* Use Data Vault in the Raw/Silver layer for auditability, and Dimensional modelling in the Gold layer for reporting.
