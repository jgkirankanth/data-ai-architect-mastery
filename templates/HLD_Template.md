# High-Level Design: [Project Name]

## 1. Executive Summary
**Business Problem:** [Brief description]
**Target State Outcome:** [Brief description]

## 2. Architecture Diagram
[Insert Mermaid.js or Draw.io architectural flow]

## 3. Component Selection
*   **Ingestion:** [e.g., Fabric Pipelines - Justification]
*   **Storage:** [e.g., OneLake / ADLS Gen2 - Justification]
*   **Compute/Transformation:** [e.g., Fabric Spark / Databricks - Justification]
*   **Serving:** [e.g., Direct Lake Power BI / Synapse Serverless - Justification]

## 4. Security & Governance Design
*   **Authentication:** Entra ID integration.
*   **Data Protection:** Encryption at rest (CMK/PMK) and in transit.
*   **Role-Based Access Control (RBAC):** Define key roles (Data Engineer, Analyst).
