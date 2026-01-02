# Architecture & Core Logic

## 1. The "Grey Box" Integration
-   **Google Sheets**: API (Read/Write).
-   **MIS**: Selenium Automation (No API).
-   **Blaze**: "Token Sniffing" via background Selenium performance logs.

## 2. Multi-Day Deal Logic (MD5 Hashing)
-   **Key**: `md5(brand|discount|vendor|locs|notes)`
-   **Anchor**: First instance (Monday).
-   **Reference**: Subsequent days (Yellow rows).
