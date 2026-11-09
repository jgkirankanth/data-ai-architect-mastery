# Microsoft Purview Enterprise Configuration

## Automated Classification Rules
* **Rule 1:** Detect regex pattern for Australian Tax File Numbers (TFN). Apply `Confidential - PII` sensitivity label.
* **Rule 2:** Detect credit card patterns. Apply `Restricted - Financial` label.

## Glossary Mapping
* Term: `Active Customer`. 
* Definition: A customer with a billed transaction in the last 90 days.
* Linked Assets: `Fact_Sales`, `Dim_Customer`.
