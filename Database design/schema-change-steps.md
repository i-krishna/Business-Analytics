# Schema updates for new reporting features in RDS and EC2

Gather requirements: Meet with stakeholders to define new reporting needs.
Design changes: Create/update ER diagrams, define new tables/columns/indexes.
Dev/test: Write change scripts (SQL ALTER, CREATE, etc.), test in dev/staging.
Review: Peer review scripts, validate against sample data.
Deploy: Schedule downtime if needed, apply scripts to RDS (via SSMS/AWS Console) and EC2 (via SSMS/command line).
Validate: Run post-deployment checks, confirm reporting works.
Document: Update schema docs, version control scripts, notify teams.

```
+---------------------+
| 1. Gather           |
| Requirements        |
+---------------------+
          |
          v
+---------------------+
| 2. Design Changes   |
| (ER diagrams,       |
| tables/columns)     |
+---------------------+
          |
          v
+---------------------+
| 3. Dev/Test         |
| (Write & test SQL   |
| scripts in dev)     |
+---------------------+
          |
          v
+---------------------+
| 4. Review           |
| (Peer review,       |
| validate sample)    |
+---------------------+
          |
          v
+---------------------+
| 5. Deploy           |
| (Apply scripts to   |
| RDS/EC2, schedule   |
| downtime if needed) |
+---------------------+
          |
          v
+---------------------+
| 6. Validate         |
| (Post-deployment    |
| checks, confirm     |
| reporting)          |
+---------------------+
          |
          v
+---------------------+
| 7. Document         |
| (Update docs,       |
| version control,    |
| notify teams)       |
+---------------------+
```
