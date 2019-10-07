# REP_Bot
Research Experience Program Bot

Purpose: 
This bot automatically reserves a REP study/survey for a class given the strict time constraints once a week. 
This eliminates having to manually reserve the study at the small time window since space is limited.

Implementation:
Script executes automation on a headless Chrome browser inside a Linux EC2 CL instance (prod server). 
CloudWatch spins up and spins down the EC2 instance given the time parameters specified on AWS Lambda (for cost effective measures).
Email notifications are sent if claim was successful or if no studies were found (through smtp).
This script initiates and terminates through a cron job.

Cron parameters: 10 09 * * 1 python /path/repbot_prod.py

FRAMEWORK:
Selenium WebDriver

LICENSE:
Selenium is an open source software, released under the Apache 2.0 license
