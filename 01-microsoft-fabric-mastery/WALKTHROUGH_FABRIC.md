# Practical Walkthrough: End-to-End Fabric Lakehouse

This guide provides the exact steps to build a Medallion architecture in Microsoft Fabric, simulating a real-world enterprise delivery.

## Stage 1: Provisioning the Foundation
1. Log into `app.fabric.microsoft.com`.
2. Click **Workspaces** > **New Workspace**. Name it `Fabric-Portfolio-Dev`.
3. In the workspace, click **New** > **Lakehouse**. Name it `LH_Financial_Market`.
4. Open the Lakehouse. In the Explorer pane, click the `...` next to **Files** and select **Upload Files**. Upload a sample CSV containing historical stock data.

## Stage 2: Bronze to Silver (Data Engineering)
1. Click **New** > **Notebook**.
2. Copy the code from `src/bronze_to_silver.py` in this repository.
3. Replace the `<workspace_id>` and `<lakehouse_id>` placeholders in the code with your actual IDs (found in your browser's URL).
4. Run the notebook. 
* **Verification:** Navigate back to your Lakehouse. Expand the **Tables** section. You should see a new Delta table named `silver_market_ticks` with a strict schema and no null prices.

## Stage 3: Silver to Gold (Data Modelling)
1. Switch to the **SQL analytics endpoint** view in your Lakehouse (top right dropdown).
2. Click **New SQL query**.
3. Write an aggregation query (e.g., Daily Average Price by Ticker) and use `CREATE VIEW vw_gold_daily_metrics AS...` to save it.
* **Verification:** The view appears under the **Views** folder and executes in under 2 seconds.

## Stage 4: Power BI Direct Lake & Security
1. In the Lakehouse, click **New semantic model**.
2. Select your `vw_gold_daily_metrics` view.
3. Click **Manage roles** in the Power BI ribbon to configure Row-Level Security (RLS). Create a role named `TechSectorOnly` and add a DAX filter: `[Sector] = "Technology"`.
* **Verification:** Click **View as**, select the `TechSectorOnly` role, and confirm the data filters correctly.
