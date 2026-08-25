# SIA Reporting API Documentation

> The Secure Internet Access (SIA) Reporting API lets you access and analyze reports for security events, acceptable user policy events, and DNS activity totals. You can also view Indicator of Compromise (IOC) data to further analyze blacklisted entries. The API allows you flexible access to the same reporting features as in Akamai Control Center, using your own tools.

Fetch the complete documentation index at: https://techdocs.akamai.com/etp-reporting/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: API

- [API index](https://techdocs.akamai.com/etp-reporting/reference/api/llms.txt): full category index
- [Secure Internet Access Enterprise Reporting API v3](https://techdocs.akamai.com/etp-reporting/reference/api.md)
- [API summary](https://techdocs.akamai.com/etp-reporting/reference/api-summary.md)
- [Get started](https://techdocs.akamai.com/etp-reporting/reference/get-started.md)
- [API concepts](https://techdocs.akamai.com/etp-reporting/reference/api-concepts.md)
- [Timestamp formats](https://techdocs.akamai.com/etp-reporting/reference/timestamp-formats.md)
- [Report scheduling](https://techdocs.akamai.com/etp-reporting/reference/report-scheduling.md)
- [Rate Limiting](https://techdocs.akamai.com/etp-reporting/reference/rate-limiting.md)
- [Filters object](https://techdocs.akamai.com/etp-reporting/reference/filters.md)
- [Errors](https://techdocs.akamai.com/etp-reporting/reference/errors.md)
- [304](https://techdocs.akamai.com/etp-reporting/reference/304.md)
- [400](https://techdocs.akamai.com/etp-reporting/reference/400.md)
- [403](https://techdocs.akamai.com/etp-reporting/reference/403.md)
- [404](https://techdocs.akamai.com/etp-reporting/reference/404.md)
- [Filter Onramp types](https://techdocs.akamai.com/etp-reporting/reference/onramp-types.md)

## API Reference: Threat event reports

- [Threat event reports index](https://techdocs.akamai.com/etp-reporting/reference/threat-event-reports/llms.txt): full category index
- [Report threat event totals](https://techdocs.akamai.com/etp-reporting/reference/get-threat-events.md): Lists the count of threat events, grouped by the chosen query aggregation.
- [Report threat event details](https://techdocs.akamai.com/etp-reporting/reference/post-threat-event-details.md): Provides all threat events records with detailed information.
- [Report threat event time series](https://techdocs.akamai.com/etp-reporting/reference/get-threat-event-time-series.md): Lists threat event totals, aggregated by hour.

## API Reference: AUP event reports

- [AUP event reports index](https://techdocs.akamai.com/etp-reporting/reference/aup-event-reports/llms.txt): full category index
- [Report AUP event totals](https://techdocs.akamai.com/etp-reporting/reference/get-aup-events.md): Lists total counts for AUP events, aggregated for the given time period.
- [Report AUP event details](https://techdocs.akamai.com/etp-reporting/reference/post-events-details.md): Provides all threat events record details for a given time period.
- [Report AUP event time series](https://techdocs.akamai.com/etp-reporting/reference/get-events-time-series.md): Lists total counts for AUP events, aggregated by hour.

## API Reference: DNS activity reports

- [DNS activity reports index](https://techdocs.akamai.com/etp-reporting/reference/dns-activity-reports/llms.txt): full category index
- [Report DNS activity totals](https://techdocs.akamai.com/etp-reporting/reference/get-dns-activities.md): Lists the count of DNS activities aggregated for the given time period.
- [Report DNS activity event details](https://techdocs.akamai.com/etp-reporting/reference/post-dns-activities-details.md): Lists raw DNS events for a given time period. This operation Lists the first 500 configurable results.
- [Report DNS activity time series](https://techdocs.akamai.com/etp-reporting/reference/get-dns-activities-time-series.md): Lists the count of DNS activities, aggregated by hour.

## API Reference: Security Connector event reports

- [Security Connector event reports index](https://techdocs.akamai.com/etp-reporting/reference/security-connector-event-reports/llms.txt): full category index
- [Report security connector event totals](https://techdocs.akamai.com/etp-reporting/reference/get-sinkhole-events.md): Lists the count of Security Connector events, grouped by the chosen query aggregation.
- [Report security connector event details](https://techdocs.akamai.com/etp-reporting/reference/post-sinkhole-event-details.md): Lists Security Connector events for a given time period.
- [Report security connector event time series](https://techdocs.akamai.com/etp-reporting/reference/get-sinkhole-events-time-series.md): Lists Security Connector event totals, aggregated by hour.

## API Reference: IDP systems reports

- [IDP systems reports index](https://techdocs.akamai.com/etp-reporting/reference/idp-systems-reports/llms.txt): full category index
- [Report IDP access log details](https://techdocs.akamai.com/etp-reporting/reference/post-access-logs-details.md): Lists the IDP access logs for a configuration for a given time period.

## API Reference: Indicators of Compromise (IOC) reports

- [Indicators of Compromise (IOC) reports index](https://techdocs.akamai.com/etp-reporting/reference/indicators-of-compromise-ioc-reports/llms.txt): full category index
- [Get IOC time series report](https://techdocs.akamai.com/etp-reporting/reference/get-time-series.md): Lists the DNS activities of a configuration for a given domain or IP, aggregated by day. Omit `startTimeSec` and `endTimeSec` from the request URL to return all available historical information.
- [Get IOC change report](https://techdocs.akamai.com/etp-reporting/reference/get-ioc-changes.md): Lists historical change information for a given record and record type. Omit `startTimeSec` and `endTimeSec` from the request URL to return all available historical information.
- [Get IOC AVC details report](https://techdocs.akamai.com/etp-reporting/reference/get-ioc-details-avc.md): Lists the AVC details for a given domain or IP.
- [Get IOC CIDR details report](https://techdocs.akamai.com/etp-reporting/reference/get-ioc-details-cidr.md): Lists the CIDR details for a given domain or IP.
- [Get IOC domain tree report](https://techdocs.akamai.com/etp-reporting/reference/get-ioc-domain-tree.md): Lists the blocklisted domains and IPs matching a given record. Returns an empty list if no domains match.
- [Get IOC time series report](https://techdocs.akamai.com/etp-reporting/reference/get-time-series-1.md): Lists the DNS activities of a configuration for a given domain or IP, aggregated by day. Omit `startTimeSec` and `endTimeSec` from the request URL to return all available historical information.
- [Get IOC change report](https://techdocs.akamai.com/etp-reporting/reference/get-ioc-changes-1.md): Lists historical change information for a given record and record type. Omit `startTimeSec` and `endTimeSec` from the request URL to return all available historical information.
- [Get IOC AVC details report](https://techdocs.akamai.com/etp-reporting/reference/get-ioc-details-avc-1.md): Lists the AVC details for a given domain or IP.
- [Get IOC CIDR details report](https://techdocs.akamai.com/etp-reporting/reference/get-ioc-details-cidr-1.md): Lists the CIDR details for a given domain or IP.
- [Get IOC domain tree report](https://techdocs.akamai.com/etp-reporting/reference/get-ioc-domain-tree-1.md): Lists the blocklisted domains and IPs matching a given record. Returns an empty list if no domains match.
- [Get IOC details report](https://techdocs.akamai.com/etp-reporting/reference/get-ioc-details.md): Lists the IOC details for a given domain or IP.
- [Get IOC AUP detail report](https://techdocs.akamai.com/etp-reporting/reference/get-ioc-details-aup.md): Lists the AUP details for a given domain or IP.
- [Get IOC details report](https://techdocs.akamai.com/etp-reporting/reference/get-ioc-details-1.md): Lists the IOC details for a given domain or IP.
- [Get IOC AUP detail report](https://techdocs.akamai.com/etp-reporting/reference/get-ioc-details-aup-1.md): Lists the AUP details for a given domain or IP.

## API Reference: DeepScan event reports

- [DeepScan event reports index](https://techdocs.akamai.com/etp-reporting/reference/deepscan-event-reports/llms.txt): full category index
- [Get deepscan details report](https://techdocs.akamai.com/etp-reporting/reference/get-scan-reports.md): Deepscan results for a configuration's offline network for a given time period. Use the path obtained from `/threat-events`.

## API Reference: Threat metadata report

- [Threat metadata report index](https://techdocs.akamai.com/etp-reporting/reference/threat-metadata-report/llms.txt): full category index
- [Get threat metadata report](https://techdocs.akamai.com/etp-reporting/reference/get-threat-metadata.md): Returns the threat metadata.

## API Reference: Feedback reports

- [Feedback reports index](https://techdocs.akamai.com/etp-reporting/reference/feedback-reports/llms.txt): full category index
- [Report a threat](https://techdocs.akamai.com/etp-reporting/reference/post-feedback-details.md): Reports the threat for a domain.
- [Get feedback event detail report](https://techdocs.akamai.com/etp-reporting/reference/get-feedbacks-details.md): Returns feedback information about a domain based on the feedback type.

## API Reference: Report schedules

- [Report schedules index](https://techdocs.akamai.com/etp-reporting/reference/report-schedules/llms.txt): full category index
- [Create a report schedule](https://techdocs.akamai.com/etp-reporting/reference/post-config-schedule.md): Creates a new report schedule for a given SIA configuration.
- [List report schedules](https://techdocs.akamai.com/etp-reporting/reference/get-config-schedules.md): Lists all configured report schedules for a given SIA configuration.
- [Get a report schedule](https://techdocs.akamai.com/etp-reporting/reference/get-config-schedule.md): Lists the configuration of a specified report schedule.
- [Update a report schedule](https://techdocs.akamai.com/etp-reporting/reference/put-config-schedule.md): Updates the configuration of a specified report schedule.
- [Remove a report schedule](https://techdocs.akamai.com/etp-reporting/reference/delete-config-schedule.md): Removes the configuration of a specified report schedule.
- [Disable a report schedule](https://techdocs.akamai.com/etp-reporting/reference/post-config-schedule-disable.md): Disables the configuration of a specified report schedule.
- [Enable a report schedule](https://techdocs.akamai.com/etp-reporting/reference/post-config-schedule-enable.md): Enables the configuration of a specified report schedule.

## API Reference: Network traffic connections reports

- [Network traffic connections reports index](https://techdocs.akamai.com/etp-reporting/reference/network-traffic-connections-reports/llms.txt): full category index
- [Report network traffic connections totals](https://techdocs.akamai.com/etp-reporting/reference/get-network-traffic-connections.md): Lists the count of network traffic connections totals, grouped by query parameters.
- [Report network traffic connections details](https://techdocs.akamai.com/etp-reporting/reference/post-network-traffic-connections-details.md): Lists network traffic connections for a given time period.
- [Report network traffic connections time series](https://techdocs.akamai.com/etp-reporting/reference/get-connections-time-series.md): Lists network traffic connections totals, aggregated by hour.

## API Reference: Proxy traffic transactions reports

- [Proxy traffic transactions reports index](https://techdocs.akamai.com/etp-reporting/reference/proxy-traffic-transactions-reports/llms.txt): full category index
- [Report proxy traffic transactions totals](https://techdocs.akamai.com/etp-reporting/reference/get-proxy-traffic-transactions.md): Lists the count of proxy traffic transaction totals, grouped by the chosen query aggregation..
- [Report proxy network traffic transaction details](https://techdocs.akamai.com/etp-reporting/reference/post-traffic-transaction-details.md): Lists proxy network traffic connections for a given time period.
- [Report proxy traffic transactions time series](https://techdocs.akamai.com/etp-reporting/reference/get-traffic-transactions-time-series.md): Lists proxy traffic transaction totals, aggregated by hour.

## API Reference: Threat intelligence

- [Threat intelligence index](https://techdocs.akamai.com/etp-reporting/reference/threat-intelligence/llms.txt): full category index
- [Get latest domain threat intelligence](https://techdocs.akamai.com/etp-reporting/reference/get-threat-intel.md): Checks for new threat intelligence dataset. If new data is available, returns a short-lived pre-signed URL.
