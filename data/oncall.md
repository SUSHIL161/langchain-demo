# On-call Guide (Team Falcon)

## Rotation
- Each on-call shift lasts 7 days, starting Monday at 10:00 IST.
- Two people are on call at a time: a primary and a secondary.
- The schedule is managed in PagerDuty under the service name `falcon-platform`.

## Response times
- Sev1 (service down): acknowledge within 5 minutes, start working on it within 15 minutes.
- Sev2 (major feature broken): acknowledge within 30 minutes.
- Sev3 (minor issue): handle during working hours, within 2 working days.

## Escalation
1. Primary on-call gets paged first.
2. If the primary does not acknowledge in 10 minutes, the secondary is paged.
3. If neither acknowledges in 20 minutes, the Engineering Manager, Priya Nair, is paged.
4. For Sev1 incidents lasting more than 1 hour, open an incident channel named `#inc-YYYYMMDD-<short-name>`.

## Communication
- Post status updates in #falcon-oncall every 30 minutes during a Sev1.
- Write a postmortem for every Sev1 within 3 working days.

## Handover
- Handover meeting is every Monday at 09:30 IST.
- The outgoing primary writes a handover note listing open incidents and known risks.
