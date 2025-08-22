Authentication vs Authorization 

# Authentication:
Verifies identity (who you are).
Example: IAM authentication for MySQL/Postgres lets users log in to DB using AWS IAM credentials.

SQL Authentication using username/password is less secure than integrated authentication (AD/IAM). The use of shared accounts undermines the principle of least privilege, complicates auditing, and obscures accountability and responsibility—especially during disaster recovery or security incidents

<img width="2807" height="1658" alt="security model" src="https://github.com/user-attachments/assets/11bd20ec-c051-4a9f-8ad9-5630551468b2" />


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






