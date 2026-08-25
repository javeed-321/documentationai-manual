# MSL5 Powered by Harmonic Documentation

> Documentation for MSL5 Powered by Harmonic

Fetch the complete documentation index at: https://techdocs.akamai.com/msl5-harmonic/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: API

- [API index](https://techdocs.akamai.com/msl5-harmonic/reference/api/llms.txt): full category index
- [MSL5 API](https://techdocs.akamai.com/msl5-harmonic/reference/api.md)
- [API summary](https://techdocs.akamai.com/msl5-harmonic/reference/api-summary.md)
- [Get started with MSL5 API](https://techdocs.akamai.com/msl5-harmonic/reference/get-started.md)
- [API concepts](https://techdocs.akamai.com/msl5-harmonic/reference/api-concepts.md)
- [API workflow](https://techdocs.akamai.com/msl5-harmonic/reference/api-workflow.md)
- [Content Purge API workflow](https://techdocs.akamai.com/msl5-harmonic/reference/content-purge-api-workflow.md)
- [API performance](https://techdocs.akamai.com/msl5-harmonic/reference/api-performance.md)
- [Errors](https://techdocs.akamai.com/msl5-harmonic/reference/errors.md)
- [HTTP status codes](https://techdocs.akamai.com/msl5-harmonic/reference/http-status-codes.md)
- [200](https://techdocs.akamai.com/msl5-harmonic/reference/204-copy.md): Operation was successful
- [201](https://techdocs.akamai.com/msl5-harmonic/reference/201.md): Resource created
- [202](https://techdocs.akamai.com/msl5-harmonic/reference/202.md): The resource was successfully accepted
- [204](https://techdocs.akamai.com/msl5-harmonic/reference/204.md): Successful deletion
- [400](https://techdocs.akamai.com/msl5-harmonic/reference/400.md): Bad Request
- [401](https://techdocs.akamai.com/msl5-harmonic/reference/401.md): Unauthorized request
- [403](https://techdocs.akamai.com/msl5-harmonic/reference/403.md): Access is forbidden
- [404](https://techdocs.akamai.com/msl5-harmonic/reference/404.md): Resource not found
- [409](https://techdocs.akamai.com/msl5-harmonic/reference/409.md): There is a conflict in the resource (for instance in an attempt to delete an entity that is still active).
- [412](https://techdocs.akamai.com/msl5-harmonic/reference/412.md): Precondition failed.
- [500](https://techdocs.akamai.com/msl5-harmonic/reference/500.md): Internal server error.

## API Reference: Media Services Live API

- [Media Services Live API index](https://techdocs.akamai.com/msl5-harmonic/reference/media-services-live-api/llms.txt): full category index
- [List alert configurations](https://techdocs.akamai.com/msl5-harmonic/reference/get-v1-alert-configurations.md): List alert configurations.
- [Get alert configuration by ID](https://techdocs.akamai.com/msl5-harmonic/reference/get-v1-alert-configuration-id.md): Get a specific alert configuration by ID.
- [Update alert configuration](https://techdocs.akamai.com/msl5-harmonic/reference/put-v1-alert-configuration-id.md): Update an existing alert configuration.  **Immutable fields** — the following fields cannot be changed after creation. If the request body contains a different value, the API returns 400: - `alert_type_id`  **Editable fields** — all other fields can be updated, including `name`. If the new name conflicts with an existing alert owned by the same user, the API returns 409.  For Phase 2 (dynamic/non-preset) alert types, changes are synced to SignOz before the database is updated. If SignOz rejects the change, the database remains untouched.
- [Delete alert configuration](https://techdocs.akamai.com/msl5-harmonic/reference/delete-v1-alert-configuration-id.md): Delete an alert configuration.
- [Create alert configuration](https://techdocs.akamai.com/msl5-harmonic/reference/post-v1-alert-configuration.md): Create a new alert configuration.
- [Subscribe to alert configuration](https://techdocs.akamai.com/msl5-harmonic/reference/post-v1-alert-configuration-id-subscribe.md): Subscribe to an alert configuration. Start receiving the alert email notification.
- [Unsubscribe from alert configuration](https://techdocs.akamai.com/msl5-harmonic/reference/post-v1-alert-configuration-id-unsubscribe.md): Unsubscribe from an alert configuration. Stop receiving the alert email notification.
- [Activate alert configuration](https://techdocs.akamai.com/msl5-harmonic/reference/post-v1-alert-configuration-id-activate.md): Activate an alert configuration. Start sending the alert notification email.
- [Deactivate alert configuration](https://techdocs.akamai.com/msl5-harmonic/reference/post-v1-alert-configuration-id-deactivate.md): Deactivate an alert configuration. Stop sending the alert notification email.
- [List triggered alerts](https://techdocs.akamai.com/msl5-harmonic/reference/get-v1-alert-triggers.md): List alert given alert configuration_id (optional), start_time (optional), end_time (optional), status (optional).
- [List alert types](https://techdocs.akamai.com/msl5-harmonic/reference/get-v1-alert-types.md): List alert types.
- [Get alert type by ID](https://techdocs.akamai.com/msl5-harmonic/reference/get-v1-alert-type-id.md): Get specific alert type by ID.
- [Retrieve usage data](https://techdocs.akamai.com/msl5-harmonic/reference/get-v1-usage-startdate-startdate-enddate-enddate.md): Retrieve usage data for specified date range and filters. Returns ingest, storage, and processing metrics aggregated by date, contract, and CP tag.
- [List CP Tags](https://techdocs.akamai.com/msl5-harmonic/reference/list_cptags.md): Lists all accessible CP Tags.
- [Create CP Tag](https://techdocs.akamai.com/msl5-harmonic/reference/create_cptag.md): Creates a new CP Tag.
- [Create origin server](https://techdocs.akamai.com/msl5-harmonic/reference/create_origin.md): Creates a new origin server. Hostname must be unique and zones must be different. Any optional field that is omitted will use its default value as documented on each field.
- [List origins](https://techdocs.akamai.com/msl5-harmonic/reference/list_origins.md): Lists all accessible origin servers. Admins see all origins in the system.
- [Get origin details](https://techdocs.akamai.com/msl5-harmonic/reference/get_origin.md): Retrieves origin server configuration and status.
- [Delete origin](https://techdocs.akamai.com/msl5-harmonic/reference/delete_origin.md): Permanently removes an origin server. Fails if origin has active streams.
- [Update origins](https://techdocs.akamai.com/msl5-harmonic/reference/put_origins.md): Update an existing origin's configuration.
- [List publishing locations](https://techdocs.akamai.com/msl5-harmonic/reference/list_publishing_locations.md): List all accessible publishing locations.
- [List S3 storage connections](https://techdocs.akamai.com/msl5-harmonic/reference/list_s3_storage_connections.md): Lists S3 storage connections for the authenticated account.
- [Create S3 storage connection](https://techdocs.akamai.com/msl5-harmonic/reference/create_s3_storage_connection.md): Creates a new S3-compatible storage connection with inline connectivity validation.
- [Get S3 storage connection](https://techdocs.akamai.com/msl5-harmonic/reference/get_s3_storage_connection.md): Retrieves an S3 storage connection by ID.
- [Update S3 storage connection](https://techdocs.akamai.com/msl5-harmonic/reference/update_s3_storage_connection.md): Updates an S3 storage connection with inline connectivity re-validation.
- [Delete S3 storage connection](https://techdocs.akamai.com/msl5-harmonic/reference/delete_s3_storage_connection.md): Soft-deletes an S3 storage connection.
- [Create stream](https://techdocs.akamai.com/msl5-harmonic/reference/create_stream.md): Create a new stream with the specified configuration. Any optional field that is omitted will use its default value as documented on each field.
- [List streams](https://techdocs.akamai.com/msl5-harmonic/reference/list_streams.md): List all accessible streams.
- [Get stream details](https://techdocs.akamai.com/msl5-harmonic/reference/get_stream.md): Get detailed information about a specific stream, including origin hostname details for both primary and backup locations.
- [Import a v4 stream](https://techdocs.akamai.com/msl5-harmonic/reference/import_stream.md): Imports an existing stream configuration from v4 format.
- [Update stream](https://techdocs.akamai.com/msl5-harmonic/reference/update_stream.md): Update an existing stream's configuration. This is a full update; omitted optional fields will be reset to their default values, not preserved. See each field description for details.
- [Delete stream](https://techdocs.akamai.com/msl5-harmonic/reference/delete_stream.md): Delete a stream and its associated resources.
- [Create event](https://techdocs.akamai.com/msl5-harmonic/reference/create_event.md): Create a new event. Past-event artifacts are always produced by the async worker pipeline; `?async` only controls whether the request waits for the worker to finish (sync response) or returns immediately (async response). A successful sync response omits the `clipping` field; async responses include it.
- [List events](https://techdocs.akamai.com/msl5-harmonic/reference/list_events.md): List all events for a stream.
- [Get event details](https://techdocs.akamai.com/msl5-harmonic/reference/get_event.md): Get detailed information about an event.
- [Delete event](https://techdocs.akamai.com/msl5-harmonic/reference/delete_event.md): Delete an event.
- [Delete event retention buffer](https://techdocs.akamai.com/msl5-harmonic/reference/delete_event_retention_buffer.md): Delete an event's retention buffer. This will mark recorded content as unavailable within a given time range
- [List event's deleted retention buffer](https://techdocs.akamai.com/msl5-harmonic/reference/list_event_deleted_retention_buffer.md): Lists all time ranges of segments marked as unavailable for the specified event.
- [List event exports](https://techdocs.akamai.com/msl5-harmonic/reference/list_event_exports.md): List all export tasks for an event.
- [Create event export](https://techdocs.akamai.com/msl5-harmonic/reference/create_event_export.md): Create a new event export task to export an event to S3 storage.
- [Get event export](https://techdocs.akamai.com/msl5-harmonic/reference/get_event_export.md): Get details of a specific export task.
- [Cancel event export](https://techdocs.akamai.com/msl5-harmonic/reference/cancel_event_export.md): Cancel a queued or running export task.
- [Create ingest credential](https://techdocs.akamai.com/msl5-harmonic/reference/create_ingest_credential.md): Create new ingest credentials.
- [List ingest credentials](https://techdocs.akamai.com/msl5-harmonic/reference/list_ingest_credentials.md): List all ingest credentials for a stream.
- [Update ingest credential](https://techdocs.akamai.com/msl5-harmonic/reference/update_ingest_credential.md): Update ingest credential metadata.
- [Delete ingest credential](https://techdocs.akamai.com/msl5-harmonic/reference/delete_ingest_credential.md): Remove ingest credentials.
- [List log destinations](https://techdocs.akamai.com/msl5-harmonic/reference/list_log_destinations.md): List all log destinations for a stream.
- [Create log destination](https://techdocs.akamai.com/msl5-harmonic/reference/create_log_destination.md): Create a new log destination for a stream.
- [Get log destination details](https://techdocs.akamai.com/msl5-harmonic/reference/get_log_destination.md): Get detailed information about a log destination.
- [Update log destination](https://techdocs.akamai.com/msl5-harmonic/reference/update_log_destination.md): Update an existing log destination.
- [Delete log destination](https://techdocs.akamai.com/msl5-harmonic/reference/delete_log_destination.md): Delete a log destination.
- [Activate log destination](https://techdocs.akamai.com/msl5-harmonic/reference/activate_log_destination.md): Activate a log destination to start exporting logs.
- [Deactivate log destination](https://techdocs.akamai.com/msl5-harmonic/reference/deactivate_log_destination.md): Deactivate a log destination to stop exporting logs.
