# Alerts Documentation

> Akamai's Alerts application is a monitoring tool that both analyzes historical audience metrics and projects the expected traffic. Using intelligent algorithms, this service compares projected traffic with actual traffic in real time, and includes static alerts based on thresholds you set. It can trigger adaptive web alerts when current audience metrics goes above or below projected traffic. It does this by taking into consideration accurate traffic patterns modeled on historical data rather than on static thresholds.

Fetch the complete documentation index at: https://techdocs.akamai.com/alerts-app/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Templates
- [List templates](https://techdocs.akamai.com/alerts-app/reference/get-templates.md): Lists templates for all supported alerts. Objects listed in the response provide only high-level information about each alert template, such as its `name` and whether its `origin` is `STATIC` or `ADAPTIVE`.  For a full definition that specifies all required `fields`, get a [specific template instance](ref:get-template).
- [Get a template](https://techdocs.akamai.com/alerts-app/reference/get-template.md): Fetches a specific template. The response features a full set of `fields` on which to base a [new alert definition](ref:post-definition).
