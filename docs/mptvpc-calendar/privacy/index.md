---
icon: lucide/shield-check
---

# MPTVPC Calendar privacy notice

MPTVPC Calendar is a personal calendar integration maintained by Magnús Pétursson. This notice covers its Google Calendar connector and local agenda, not unrelated applications or the rest of this portfolio site.

Contact: [magnus@magnusp.is](mailto:magnus@magnusp.is).

## Information the app accesses

After the owner authorizes an account through Google, the app accesses:

- Calendar identifiers, names, time zones, primary-calendar status and access roles. This information supports account verification and calendar selection.
- For explicitly selected calendars and date ranges: event identifiers, titles, start and end times, useful locations, event status and recurrence-instance metadata. These fields preserve all-day events, changed instances and cancellations.
- Account identity, authorization scopes, token expiry and OAuth credentials needed to make authorized API requests.

The connector does not request event descriptions, attendee lists or attachments. It does not request Gmail, Drive or calendar-write permissions. Calendar titles and locations can themselves contain personal information even when other fields are excluded.

Google's read scopes cover the account's accessible calendars. The app's local calendar allowlist limits actual event fetching; it does not narrow the permission granted by Google.

## How information is used

The app uses this information to verify account identity, read the selected calendars, prepare the owner's agenda, preserve source attribution, identify provable time overlaps and report missing or stale data. It does not automatically resolve conflicts or infer hours actually worked from scheduled appointments.

The connector and agenda do not sell data, display advertising, build advertising profiles or train AI models. They do not publish appointments on this website or write changes back to the original calendars.

## Optional assistant and messaging use

The connector and agenda can run without an AI model. They do not themselves send event data to an AI provider or messaging platform.

If the owner asks an assistant such as Hermes to interpret or send an agenda, the selected calendar text may be processed by the assistant's configured model provider and, when requested, a messaging service such as WhatsApp. Those services have their own privacy and retention terms. The owner must approve the fields and destination and review applicable provider data-use settings before enabling that processing. An API read permission alone is not authorization to share calendar contents elsewhere.

This notice does not promise that data sent to an external assistant or messaging service remains only on the local computer. Organizational calendars also remain subject to the organization's rules.

## Storage and security

OAuth credentials are stored separately for each account, outside the source repository, in owner-restricted local directories and files. Calendar selections and minimal event snapshots are also stored locally. Diagnostic output is designed to avoid credentials and event bodies; source identifiers, counts, timestamps and failure status may appear in operational records.

Local file permissions are not a claim of disk encryption. The computer's security, backups and any separately enabled services affect protection and recovery. No system can guarantee absolute security.

## Retention and removal

The current local tools do not impose an automatic deletion schedule for saved snapshots, credentials or operational records. They remain until the owner removes them. A future scheduled integration needs an explicit retention policy before activation.

The owner can revoke MPTVPC Calendar's Google access at [Google Account connections](https://myaccount.google.com/connections). Revocation stops future authorized access but does not erase snapshots already saved locally or information previously sent to another service.

To remove local data, stop the relevant tool or scheduled process and delete the account's local credentials, selections, snapshots and any applicable copies or backups. Deleting a local copy does not delete an original calendar event. For assistance with access, correction or deletion, contact [magnus@magnusp.is](mailto:magnus@magnusp.is).

## Visiting these pages

These informational pages do not ask visitors to connect a Google account and do not contain calendar data. The website host receives ordinary web requests and may keep technical access logs under its own policies.

## Changes

This notice must be updated before materially changing the app's data access, sharing or retention practices. Additional account permissions or new destinations require separate authorization.

[Back to MPTVPC Calendar](../index.md)
