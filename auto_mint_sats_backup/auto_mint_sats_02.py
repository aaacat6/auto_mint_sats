# import os
# import time
# import requests
# import json

# def get_median_fee_avg():
#     response = requests.get("https://mempool.space/api/v1/blocks")
#     data = json.loads(response.text)
#     total_median_fee = sum(block['extras']['medianFee'] for block in data)
#     return total_median_fee / len(data)

# def send_message(message):
#     print(message)

# def execute_command(command):
#     os.system(command)

# if __name__ == "__main__":
#     command = 'curl --version'
#     interval_send = 20
#     interval_sleep = 0.1

#     try:
#         while True:
#             median_fee_avg = get_median_fee_avg()
#             if median_fee_avg < 6:
#                 send_message('Mint Sats.')
#                 execute_command(command)
#             else:
#                 send_message('Gas is too high.')
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
    # 只获取最上方的三个 'medianFee'
    median_fees = [block['extras']['medianFee'] for block in data[:3]]
    median_fee_avg = sum(median_fees) / len(median_fees)
    return median_fee_avg

def send_message_and_execute_command(message, command):
    cmd_command = f'echo "{message}" & {command}'
    os.system(cmd_command)

if __name__ == "__main__":
    message = 'Mint Sats.'
    command = 'ord.exe --bitcoin-data-dir "E:\BitcoinNode\blocks" --cookie-file "E:\BitcoinNode\.cookie" --wallet ac_sats wallet balance'

    interval_send = 10    # 设置发送消息的间隔时间（单位：秒）
    interval_sleep = 0.1  # 设置发送消息后的休眠时间（单位：秒）

    try:
        while True:
            median_fee_avg = get_median_fee_avg()
            if median_fee_avg < 10:
                send_message_and_execute_command(message, command)
            else:
                print("Gas is too high.")
            time.sleep(interval_sleep)
            time.sleep(interval_send - interval_sleep)
    except KeyboardInterrupt:
        print("程序已终止。")
