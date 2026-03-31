chad@Mac Sentinel-Log-AI % python3 src/main.py
Initializing bert-base-uncased...
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
The following layers were not sharded: bert.encoder.layer.*.attention.self.value.bias, bert.encoder.layer.*.output.LayerNorm.bias, bert.encoder.layer.*.attention.self.value.weight, bert.embeddings.token_type_embeddings.weight, bert.encoder.layer.*.attention.output.dense.bias, bert.encoder.layer.*.output.dense.bias, classifier.weight, bert.embeddings.LayerNorm.weight, bert.encoder.layer.*.attention.self.query.weight, bert.encoder.layer.*.attention.self.key.weight, bert.encoder.layer.*.attention.self.key.bias, bert.encoder.layer.*.intermediate.dense.weight, bert.pooler.dense.weight, bert.encoder.layer.*.attention.self.query.bias, classifier.bias, bert.encoder.layer.*.attention.output.LayerNorm.weight, bert.encoder.layer.*.intermediate.dense.bias, bert.encoder.layer.*.output.LayerNorm.weight, bert.encoder.layer.*.attention.output.dense.weight, bert.pooler.dense.bias, bert.encoder.layer.*.attention.output.LayerNorm.bias, bert.embeddings.word_embeddings.weight, bert.encoder.layer.*.output.dense.weight, bert.embeddings.LayerNorm.bias, bert.embeddings.position_embeddings.weight
Loading weights: 100%|█████████████████████| 199/199 [00:00<00:00, 23561.51it/s]
Initial Training Step Complete. Loss: 0.6869

--- Starting Analysis of 10 Log Entries ---

✅ [NORMAL] (Conf: 57.28%)
    Log: Jan 21 12:00:01 hms-prod-01 systemd: Started Session 123 of user root.

✅ [NORMAL] (Conf: 53.24%)
    Log: Jan 21 12:01:15 hms-prod-02 kernel: x86/fpu: Supporting XSAVE feature 0x002.

✅ [NORMAL] (Conf: 52.71%)
    Log: Jan 21 12:02:30 hms-prod-03 ntpd[1402]: Receive time set: +0.000004s.

✅ [NORMAL] (Conf: 54.19%)
    Log: Jan 21 12:05:42 hms-prod-452 sshd: WARNING: repeated login attempts from unauthorized IP 192.168.1.50 - Potential Brute Force.

✅ [NORMAL] (Conf: 54.82%)
    Log: Jan 21 12:08:12 hms-prod-05 CRON[2041]: (root) CMD (run-parts /etc/cron.hourly)

✅ [NORMAL] (Conf: 52.33%)
    Log: Jan 21 12:10:10 hms-prod-01 kernel: CRITICAL: CPU temperature above 95C - hardware throttling initiated.

✅ [NORMAL] (Conf: 53.91%)
    Log: Jan 21 12:12:45 hms-prod-07 postfix/cleanup[3201]: A12B3C4D5E: message-id=<202601211212@hms.edu>

✅ [NORMAL] (Conf: 53.79%)
    Log: Jan 21 12:15:22 hms-prod-452 kernel: ALERT: Out of memory (OOM-Kill process 5902 'python3').

✅ [NORMAL] (Conf: 54.11%)
    Log: Jan 21 12:18:05 hms-prod-12 systemd: Stopping User Manager for UID 1001.

✅ [NORMAL] (Conf: 55.16%)
    Log: Jan 21 12:20:33 hms-prod-22 sshd: Accepted publickey for admin from 10.0.5.15 port 54322 ssh2.
