# Incident Tracking System
# Author: Zaira Contreras

print("=" * 40)
print("      INCIDENT TRACKING SYSTEM")
print("=" * 40)

incident = {
    "Incident ID": 1001,
    "Employee Name": "John Smith",
    "Incident Date": "2026-06-01",
    "Incident Type": "Near Miss",
    "Location": "Plant A",
    "Description": "Unsecured ladder observed near active work area.",
    "Corrective Action": "Ladder removed and area inspected.",
    "Status": "Closed"
}

for key, value in incident.items():
    print(f"{key}: {value}")

print("\nIncident successfully recorded.")
