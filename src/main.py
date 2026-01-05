# Changelog

## [v12.5] - 2026-01-05 (Current)
### Fixed
-   **Breakdown View Bug**: Monthly and Sale sections now preserved when switching to Breakdown view
    -   Previously, rebuild deleted non-weekly rows
    -   Now saves monthly/sale rows before rebuild and re-appends after

### Added
-   **Blaze Discount Title Integration**: Link Blaze promotions to Google Sheet rows
    -   Blue "Blaze" button in ID Matcher Actions column
    -   Selection modal with suggested matches, full library, and drag-drop queue
    -   Writes to "Blaze Discount Title" column in Google Sheet
    -   Auto-fetches Blaze data if not already synced
-   **Suggestion Filter Dropdown**: NONE/BOGO/B2G1/BULK filter for suggestions
    -   BULK matches patterns like "2 for $40", "Mix & Match", etc.
-   **Alternate Brand Names Input**: Add alternate spellings for better matching
    -   Tags display with remove buttons
-   **Status Filter for Full Library**: All/Active/Inactive filter
-   **Three Apply Buttons**: Separate control for MIS IDs and Blaze Titles
    -   "Apply MIS IDs" - Only writes MIS ID column
    -   "Apply Blaze Titles" - Only writes Blaze Discount Title column
    -   "Apply All" - Writes both columns
-   **New Endpoint**: `/api/mis/apply-blaze-titles` for writing Blaze titles

### Changed
-   **Removed 10 Suggestion Limit**: Now shows ALL matching suggestions
-   **Approve/Deny Buttons**: Made more compact to fit Blaze button
-   **approvedMatches Structure**: Now includes `blaze_titles` array field

## [v12.4] - 2026-01-02
### Added
-   **Multi-Day Reference System**: Yellow rows now appear for subsequent weekdays to indicate the deal is part of a group.
-   **Visuals**: Weekday headers now use Bright Cyan (#00ffff) for contrast.
-   **Header Notes**: Format `[Rows] Brand - D: X%` added to headers.

## [v12.2] - Previous
-   **Cleanup Audit Tab**: Added "Zombie Deal" detection.
-   **Weekly Breakdown List**: New UI component for planning.
