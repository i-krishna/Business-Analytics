Authentication vs Authorization 

# Authentication:
Verifies identity (who you are).
Example: IAM authentication for MySQL/Postgres lets users log in to DB using AWS IAM credentials.

# Authorization:

Determines permissions (what you can do).
Example: IAM policies control who can manage RDS resources (create, modify, delete instances) via AWS Console/API.

SQL Server RBAC:  Create roles (CREATE ROLE), assign permissions (GRANT), add users to roles (ALTER ROLE ADD MEMBER)
```
CREATE ROLE ReportingUser;
GRANT SELECT ON Sales TO ReportingUser;
ALTER ROLE ReportingUser ADD MEMBER [krishna];
```
Power BI RBAC: Define roles in Power BI Desktop (Manage Roles), set DAX filters, publish to Power BI Service, assign users to roles for row-level security.

SQL Server on RDS: IAM is used for management/API (who can create/modify RDS instances), not for direct DB login. 






