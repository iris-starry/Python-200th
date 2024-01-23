KB = 1024
total_service = 0

with open('access_lot', 'r') as f:
    logs = f.readlines()
    for log in logs:
        log = log.split()
        sevicebyte = log[9]
        if sevicebyte.isdigit():
            total_service += int(sevicebyte)

total_service /= KB
print('총 서비스 용량: %dKB' %total_service)