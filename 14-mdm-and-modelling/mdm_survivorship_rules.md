# Master Data Management: Golden Record Design

## Match & Merge Rules (Citizen Domain)
1. **Exact Match:** National ID Number (TFN/SSN).
2. **Fuzzy Match:** First Name, Last Name, and Date of Birth (Levenshtein distance < 2).
3. **Survivorship:** 
   * Address data survives from the Billing System (highest trust).
   * Email data survives from the CRM System (most frequently updated).
