CREATE TABLE incidents (
    incident_id INTEGER PRIMARY KEY,
    employee_name TEXT NOT NULL,
    incident_date DATE,
    incident_type TEXT,
    location TEXT,
    description TEXT,
    corrective_action TEXT,
    status TEXT
);

CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    employee_name TEXT NOT NULL,
    department TEXT,
    position TEXT
);
