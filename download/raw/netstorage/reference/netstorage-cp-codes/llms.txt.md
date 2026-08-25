# NetStorage Documentation

> NetStorage is a holistic solution for maintaining large collections of on-demand digital content-including electronic images, streaming media files, software, documents, and other digital objects-while also offering performance compatible with today’s online delivery needs and customers’ expectations of instant access.

Fetch the complete documentation index at: https://techdocs.akamai.com/netstorage/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: NetStorage CP codes
- [Create a CP code](https://techdocs.akamai.com/netstorage/reference/post-cpcodes.md): This operation creates a CP code for use with NetStorage.
- [List unused CP Codes](https://techdocs.akamai.com/netstorage/reference/get-cpcodes-unused.md): Get a list of CP codes that aren't assigned to a storage group.
- [List CP codes in use](https://techdocs.akamai.com/netstorage/reference/get-cpcodes-used.md): Get a list of all CP codes that are assigned to a storage group.
- [Delete an automatic purge routine](https://techdocs.akamai.com/netstorage/reference/delete-cpcode-age-deletions.md): Delete the automatic purge routine for a specific CP code.
- [View the automatic purge routine](https://techdocs.akamai.com/netstorage/reference/get-cpcode-age-deletions.md): View the automatic purge routines for a `cpcodeId`. You can optionally include a URL-encoded `ageDeletionDirectoryPrefix` to filter an individual purge routine.
- [Modify a purge routine](https://techdocs.akamai.com/netstorage/reference/put-cpcode-age-deletions.md): Make changes to an automatic purge routine for a specific CP code.
