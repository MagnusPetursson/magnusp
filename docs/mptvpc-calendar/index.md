---
icon: lucide/calendar-days
---

# MPTVPC Calendar

MPTVPC Calendar is a private, read-only calendar tool maintained by Magnús Pétursson for personal use. It reads selected calendars from separately authorized accounts and prepares a local agenda. It is not a public calendar service and does not offer public account registration.

## What it does

The Google Calendar connector reads calendar metadata and selected event details within an explicit date range. The local agenda keeps each event's source, preserves overlapping appointments, and warns when a source is missing or stale. It does not create, edit, delete or synchronize calendar events between accounts.

The Google connector and local agenda are working components. Additional calendar-provider delivery and unattended scheduling are separate setup steps; this page does not claim they are already running.

## Google permissions

The app requests only these Google Calendar permissions:

- `calendar.calendarlist.readonly`: discover calendar names, identifiers, time zones and access roles, and verify the intended account.
- `calendar.events.readonly`: read selected calendar events for the requested date range.

Google grants these permissions across calendars accessible to the authorized account. A local allowlist determines which calendars the tool actually reads; this filter is not a separate Google permission boundary. Each account must be authorized individually.

The app does not request Gmail, Drive or calendar-write access. It does not need your Google password. Authorization takes place on Google's own website.

## Privacy and contact

These public pages describe the app. They do not display appointments, OAuth credentials or private account lists.

Read the [privacy notice](privacy/index.md) for data use, storage, optional assistant processing and removal instructions.

For support or privacy questions, contact [magnus@magnusp.is](mailto:magnus@magnusp.is).
