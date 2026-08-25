# Alerts Documentation

> Akamai's Alerts application is a monitoring tool that both analyzes historical audience metrics and projects the expected traffic. Using intelligent algorithms, this service compares projected traffic with actual traffic in real time, and includes static alerts based on thresholds you set. It can trigger adaptive web alerts when current audience metrics goes above or below projected traffic. It does this by taking into consideration accurate traffic patterns modeled on historical data rather than on static thresholds.

Fetch the complete documentation index at: https://techdocs.akamai.com/alerts-app/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Sparklines
- [List sparklines](https://techdocs.akamai.com/alerts-app/reference/get-sparklines.md): Lists _sparklines_, reports that plot anomalies that trigger firings over a time series. Each sparkline this operation lists corresponds to an alert definition. Specify more than one alert identifier to gather related data from different alerts for potential use in overlays, for example one sparkline to identify too much traffic, and another for too little traffic. Note that sparklines based on adaptive alerts provide observed data for both `anomalies` and the full range of `points`. Sparklines based on static alerts only provide observed data for `anomalies`, and the `points` simply define the range of the time series without any observed non-anomalous data.
