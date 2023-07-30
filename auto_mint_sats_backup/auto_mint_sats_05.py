import time
import os
import requests
import json


def get_median_fee():
    response = requests.get("https://mempool.space/api/v1/fees/mempool-blocks")
    data = json.loads(response.text)

    # 获取最新的块（列表的第一个元素）的 'medianFee' 值
    median_fee = data[0]['medianFee']  
    return median_fee

def send_message_and_execute_command(message, command):
    cmd_command = f'echo "{message}" & {command}'
    os.system(cmd_command)

if __name__ == "__main__":
    message = 'Mint Sats.'
    command_wallet_balance = 'ord.exe --bitcoin-data-dir "I:/BitcoinNode/blocks" --cookie-file "I:/BitcoinNode/.cookie" --wallet ac_sats wallet balance' 

    interval_send = 60  # 设置发送消息的间隔时间（单位：秒）
    interval_sleep = 1  # 设置发送消息后的休眠时间（单位：秒）

    command_count = 0  # initialize command counter

    try:
        while True:
            from datetime import datetime
            # 获取当前时间
            now = datetime.now()
            # 转换为你想要的格式
            formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
            median_fee = get_median_fee()
            command = f'ord.exe --bitcoin-data-dir "I:/BitcoinNode/blocks" --cookie-file "I:/BitcoinNode/.cookie" --wallet ac_sats wallet inscribe --postage "330 sats" --csv I:/btc/btcNft/batch.csv --fee-rate {median_fee}'
            command_transfer_sats = f'ord.exe --bitcoin-data-dir "I:/BitcoinNode/blocks" --cookie-file "I:/BitcoinNode/.cookie" --wallet ac_sats wallet inscribe --postage "330 sats" --destination bc1pgc7tz23sh6h75zqase2dq82zdwtp9eq00vpwafrvptul3ukmlg5q9pqp38 I:/btc/btcNft/brc20_transfer.txt --fee-rate {median_fee}'  
            print(f"Current medianFee: {median_fee}")   # 打印出当前的medianFee值
            print("Current Time =", formatted_now)

            # if median_fee > 15:
            #     interval_send = 60
            # if 6.2 < median_fee < 10:
            #     interval_send = 30  
            if median_fee <= 6.2:
                interval_send = 10
                send_message_and_execute_command(f"WalletBalance", command_wallet_balance)
                send_message_and_execute_command(message, command)
                command_count += 1  # increment command counter
                if command_count == 43:  # check if command has been executed 43 times
                    send_message_and_execute_command("Transferring Sats", command_transfer_sats)
                    command_count = 0  # reset command counter
            else:
                # interval_send = 60
                interval_send = 30  
                print("Gas is too high.")
                send_message_and_execute_command(f"WalletBalance", command_wallet_balance)    

            time.sleep(interval_sleep)
            time.sleep(interval_send - interval_sleep)
    except KeyboardInterrupt:
        print("程序已终止。")
