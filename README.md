# REP_Bot
Research Experience Program Bot

Purpose: 
This bot automatically reserves a REP study/survey for a class given the strict time constraints once a week. 
This eliminates having to manually reserve the study at the small time window since space is limited.

Implementation:
Selenium script executes automation on a headless Chrome browser inside a Linux EC2 instance.
A Lambda script on AWS is fired to spin up and down the EC2 instance given the time parameters specified on CloudWatch (for cost effective measures).
Email notifications are sent if claim was successful or if no studies were found (through smtp).
Selenium script initiates and terminates through a cronjob.

Cron parameters: 10 09 * * 1 python /path/repbot_prod.py
