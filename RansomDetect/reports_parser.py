# extract the frequence of the API calls

import os
import json
import csv

# where the sample are
submit_folder = os.path.join("dataset_reports","unzipped")
# where to put the results (you need to create the folder)
result_folder = 'results_csv'

# name of the file generated and his logs
report_file_name = "ransomware_grouped_apis.csv"
log_file_name = "ransomware_grouped_apis_logs.txt"

apis = [
    'sha256',
    'family',
    'cuckoo_id',
    'GetFileAttributesA',
    'GetFileAttributesW',
    'GetFileAttributesExA',
    'GetFileAttributesExW',
    'NtOpenKey',
    'RegOpenKey',
    'NtEnumerateKey',
    'RegEnumKey',
    'NtQueryValueKey',
    'RegQueryValue',
    'NtClose',
    'RegCloseKey',
    'GetUserNameA',
    'GetUserNameW',
    'GetComputerNameA',
    'GetComputerNameW',
    'GetSystemMetrics',
    'GetSystemInfo',
    'NtQuerySystemInformation',
    'GlobalMemoryStatus',
    'GlobalMemoryStatusEx',
    'GetDiskFreeSpace',
    'GetDiskFreeSpaceA',
    'GetDiskFreeSpaceW',
    'GetDiskFreeSpaceEx',
    'GetDiskFreeSpaceExA',
    'GetDiskFreeSpaceExW',
    'DeviceIoControl',
    'NtDeviceIoControlFile',
    'NtCreateFile',
    'NtOpenDirectoryObject',
    'IsDebuggerPresent',
    'NtAllocateVirtualMemory',
    'NtProtectVirtualMemory',
    'NtFreeVirtualMemory',
    'LdrGetProcedureAddress',
    'LdrLoadDll',
    'GetAdaptersAddresses',
    'FindWindowA',
    'FindWindowW',
    'FindWindowExA',
    'FindWindowExW'
]

grouped_apis = [
    'sha256',
    'family',
    'cuckoo_id',
    'GetFileAttributes',
    'OpenKey',
    'EnumerateKey',
    'QueryValue',
    'CloseKey',
    'GetUserName',
    'GetSystemMetrics',
    'SystemInformation',
    'GetDiskFreeSpace',
    'GlobalMemoryStatus',
    'GetDiskFreeSpace',
    'DeviceIoControl',
    'NtCreateFile',
    'NtOpenDirectoryObject',
    'IsDebuggerPresent',
    'NtAllocateVirtualMemory',
    'NtProtectVirtualMemory',
    'NtFreeVirtualMemory',
    'LdrGetProcedureAddress',
    'LdrLoadDll',
    'GetAdaptersAddresses',
    'FindWindow'
]

# clear files
with open(os.path.join(result_folder, log_file_name), 'w') as logs:
    logs.write("")

with open(os.path.join(result_folder, report_file_name), 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=grouped_apis)
    csv_writer.writeheader()

# set to small number to test and debug
Number_of_families = 10000
Number_of_reports = 10000

families = os.listdir(submit_folder)

families_index = 0
for family in families:
    if(not(families_index < Number_of_families)):
        break
    families_index = families_index + 1

    reports = os.listdir(os.path.join(submit_folder, family))
    print("\n[INFO] Processing family: {}".format(family))

    reports_index = 0
    for report in reports:
        if(not(reports_index < Number_of_reports)):
            break
        reports_index = reports_index + 1

        print("[INFO] Processing report: {}".format(report))
        file = open(os.path.join(submit_folder, family,
                    report, 'reports', 'report.json'))
        data = json.load(file)

        if 'behavior' not in data:
            with open(os.path.join(result_folder, log_file_name), 'a') as logs:
                logs.write("[NO BEHAVIOR] {} {}\n".format(family, report))
            continue

        stats = {}
        for api in apis:
            stats[api] = 0

        if 'apistats' in data['behavior']:
            api_groups = data['behavior']['apistats']
            for api_group in api_groups:
                for api in apis:
                    if api in api_groups[api_group]:
                        stats[api] = stats[api] + api_groups[api_group][api]

            stats['sha256'] = data['target']['file']['sha256']
            stats['family'] = family
            stats['cuckoo_id'] = report

            grouped_stats = {}
            grouped_stats['sha256'] = data['target']['file']['sha256']
            grouped_stats['family'] = family
            grouped_stats['cuckoo_id'] = report

            grouped_stats['GetFileAttributes'] = stats['GetFileAttributesA'] +stats['GetFileAttributesW'] +stats['GetFileAttributesExA'] +stats['GetFileAttributesExW']
            grouped_stats['OpenKey'] = stats['NtOpenKey'] +stats['RegOpenKey']
            grouped_stats['EnumerateKey'] = stats['NtEnumerateKey'] +stats['RegEnumKey']
            grouped_stats['QueryValue'] = stats['NtQueryValueKey']+stats['RegQueryValue']
            grouped_stats['CloseKey'] = stats['NtClose']+stats['RegCloseKey']
            grouped_stats['GetUserName'] = stats['GetUserNameA']+stats['GetUserNameW']+stats['GetComputerNameA']+stats['GetComputerNameW']
            grouped_stats['GetSystemMetrics'] = stats['GetSystemMetrics']
            grouped_stats['SystemInformation'] = stats['GetSystemInfo']+stats['NtQuerySystemInformation']
            grouped_stats['GetDiskFreeSpace'] = stats['GetDiskFreeSpace']+stats['GetDiskFreeSpaceA']+stats['GetDiskFreeSpaceW']+stats['GetDiskFreeSpaceEx']+stats['GetDiskFreeSpaceExA']+stats['GetDiskFreeSpaceExW']
            grouped_stats['GlobalMemoryStatus'] = stats['GlobalMemoryStatus']+stats['GlobalMemoryStatusEx']
            grouped_stats['GetDiskFreeSpace'] = stats['GetDiskFreeSpace'] + stats['GetDiskFreeSpaceA'] + stats['GetDiskFreeSpaceW'] + stats['GetDiskFreeSpaceEx'] + stats['GetDiskFreeSpaceExA'] + stats['GetDiskFreeSpaceExW']
            grouped_stats['DeviceIoControl'] = stats['DeviceIoControl']	+ stats['NtDeviceIoControlFile']
            grouped_stats['NtCreateFile'] = stats['NtCreateFile']
            grouped_stats['NtOpenDirectoryObject'] = stats['NtOpenDirectoryObject']
            grouped_stats['IsDebuggerPresent'] = stats['IsDebuggerPresent']
            grouped_stats['NtAllocateVirtualMemory'] = stats['NtAllocateVirtualMemory']
            grouped_stats['NtProtectVirtualMemory'] = stats['NtProtectVirtualMemory']
            grouped_stats['NtFreeVirtualMemory'] = stats['NtFreeVirtualMemory']
            grouped_stats['LdrGetProcedureAddress'] = stats['LdrGetProcedureAddress']
            grouped_stats['LdrLoadDll'] = stats['LdrLoadDll']
            grouped_stats['GetAdaptersAddresses'] = stats['GetAdaptersAddresses']
            grouped_stats['FindWindow'] = stats['FindWindowA'] + stats['FindWindowW'] + stats['FindWindowExA'] + stats['FindWindowExW']
            
            with open(os.path.join(result_folder, report_file_name), 'a') as csv_file:
                csv_writer = csv.DictWriter(csv_file, fieldnames=grouped_apis)
                csv_writer.writerow(grouped_stats)
                print("[INFO] Writing in the {}".format(report_file_name))
        else:
            print('[WARINING] No API stats.')
            with open(os.path.join(result_folder, log_file_name), 'a') as logs:
                logs.write("[NO APISTATS] {} {}\n".format(family, report))

        file.close()
