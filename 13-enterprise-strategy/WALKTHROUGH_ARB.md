# Practical Walkthrough: The Architecture Review Board (ARB)

For the Enterprise Data Architect role, you must know how to defend your designs. Practice this mock ARB scenario with a peer or by recording yourself.

## The Scenario
You are proposing migrating the company's core operational reporting from an on-premises SQL Server to Microsoft Fabric. You have submitted the `ADR_Template.md` choosing Fabric over a pure Databricks approach.

## The Challenge (Mock Questions to defend against)
1. **The Infrastructure Lead asks:** "Fabric is SaaS. How do we ensure our data doesn't traverse the public internet? We require Private Endpoints."
   * *Your Defense:* Explain how Fabric supports Managed Private Endpoints and Private Links for secure VNet integration.
2. **The Data Engineering Lead asks:** "We have complex, thousands-of-lines Python transformations. Why Fabric Notebooks over Databricks?"
   * *Your Defense:* Acknowledge Databricks is superior for massive-scale complex engineering, but justify Fabric based on unified governance (OneSecurity), native Power BI integration (Direct Lake), and reduced integration overhead for this specific workload.
3. **The Security Officer asks:** "How are you handling Data Masking for PII?"
   * *Your Defense:* Detail the use of Purview auto-classification and Fabric OLS/RLS.

* **Verification:** You can answer these without hesitation using the STAR method, focusing on business value and risk mitigation.
