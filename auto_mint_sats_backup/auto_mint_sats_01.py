# import time
# import subprocess

# def send_message_to_cmd(message):
#     cmd_command = f'echo {message}'
#     subprocess.Popen(cmd_command, shell=True)

# if __name__ == "__main__":
#     message = 'ord.exe --bitcoin-data-dir "E:\BitcoinNode\blocks" --cookie-file "E:\BitcoinNode\.cookie" --wallet ac_sats wallet balance'
#     interval_send = 10    # 设置发送消息的间隔时间（单位：秒）
#     interval_sleep = 5  # 设置发送消息后的休眠时间（单位：秒）

#     try:
#         while True:
#             send_message_to_cmd(message)
#             time.sleep(interval_sleep)
#             time.sleep(interval_send - interval_sleep)
#     except KeyboardInterrupt:
#         print("程序已终止。")


# import time
# import os

# def send_message_and_execute_command(message, command):
#     cmd_command = f'echo "{message}" & {command}'
#     os.system(cmd_command)

# if __name__ == "__main__":
#     message = 'Mint Sats.'
#     command = 'ord.exe --bitcoin-data-dir "E:\BitcoinNode\blocks" --cookie-file "E:\BitcoinNode\.cookie" --wallet ac_sats wallet balance'  # 在这里替换成你想要执行的命令

#     interval_send = 10    # 设置发送消息的间隔时间（单位：秒）
#     interval_sleep = 0.1  # 设置发送消息后的休眠时间（单位：秒）

#     try:
#         while True:
#             send_message_and_execute_command(message, command)
#             time.sleep(interval_sleep)
#             time.sleep(interval_send - interval_sleep)
#     except KeyboardInterrupt:
#         print("程序已终止。")

import time
import os
import requests
import json

def get_median_fee_avg():
    response = requests.get("https://mempool.space/api/v1/blocks")
    data = json.loads(response.text)
    total_median_fee = sum(block['medianFee'] for block in data)
    return total_median_fee / len(data)

def send_message_and_execute_command(message, command):
    cmd_command = f'echo "{message}" & {command}'
    os.system(cmd_command)

if __name__ == "__main__":
    message = 'Mint Sats.'
    command = 'ord.exe --bitcoin-data-dir "E:\\BitcoinNode\\blocks" --cookie-file "E:\\BitcoinNode\\.cookie" --wallet ac_sats wallet balance'
    interval_send = 10
    interval_sleep = 0.1

    try:
        while True:
            median_fee_avg = get_median_fee_avg()
            if median_fee_avg < 9:
                send_message_and_execute_command(message, command)
            time.sleep(interval_send)
    except KeyboardInterrupt:
        print("程序已终止。")
