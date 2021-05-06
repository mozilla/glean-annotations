This field is stored as a string in the "raw" tables (e.g., `baseline`, `metrics`) and a familiar `DATE` in derived tables (e.g., `baseline_clients_daily`). 

An example of calculating DAU by profile age from the `baseline` table is given in [STMO#79741](https://sql.telemetry.mozilla.org/queries/79741/source), which
utilizes the UDF `parse_iso8601_date` to create a `DATE` from the string column.

An example of calculating new profile DAU from the `baseline_clients_daily` table is given in [STMO#77855](https://sql.telemetry.mozilla.org/queries/77855/source).
