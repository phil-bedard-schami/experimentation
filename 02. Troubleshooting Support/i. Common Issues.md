# Common Issues

### CDC failure

Please note, this is the current state: this will changed in a fully fledged process with monitoring etc.

In the future we will have a monitoring solution that notifiesus of any failures in the DMS/CDC process for any database migration tasks that failed. If ever a task has failed it will automatically stop the task therefore a user will need to go back in to resume the task manually.

1) Go to DMS in AWS
2) Database migration tasks
3) Status -> You will see a failure
4) Go in the task -> actions -> Stop (this has to be done, a failure will not stop the process automatically)

    Better to do this afterhours as it will retrigger the full load which can take time and put stress on the system. After that it will start replication the ongoing changes.

5) Task -> actions -> Resume/Restart

Restart: Going from the beginning, will delete everything on the target database and retrigger a full load then CDC will kick in for ongoing replication.

Resume: Will resume the CDC based on the checkpoint and replicate whatever changes were missed as it was stopped/offline.

6) 
7) 

Extra check: If you resume the task and you don't see any activity in the table statistics then you can assume that the task hasn't resumed. You can also check the CloudWatch metrics. In the CloudWatch metricsyou can filter by Full Load, CDC, etc. You will most likely see a lot of acitvity in the incoming changes when filtered to CDC but not with full load since a full load is only done on restart.

Recovery checkpoint will allow you to track when it ran last. No action needed but it's for us to understand that the system knows when the last time the replication worked and to know what data to recapture.

Lambda function created to retrigger the database migration task if ever 