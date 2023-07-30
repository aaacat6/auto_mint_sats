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
    # command = f'ord.exe --bitcoin-data-dir "I:/BitcoinNode/blocks" --cookie-file "I:/BitcoinNode/.cookie" --wallet ac_sats wallet inscribe --postage "330 sats" --csv I:/btc/btcNft/batch.csv --fee-rate {median_fee}'
    command_wallet_balance = 'ord.exe --bitcoin-data-dir "I:/BitcoinNode/blocks" --cookie-file "I:/BitcoinNode/.cookie" --wallet ac_sats wallet balance' 

    interval_send = 10  # 设置发送消息的间隔时间（单位：秒）
    interval_sleep = 1  # 设置发送消息后的休眠时间（单位：秒）

    try:
        while True:
            from datetime import datetime
            # 获取当前时间
            now = datetime.now()
            # 转换为你想要的格式
            formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
            median_fee = get_median_fee()
            command = f'ord.exe --bitcoin-data-dir "I:/BitcoinNode/blocks" --cookie-file "I:/BitcoinNode/.cookie" --wallet ac_sats wallet inscribe --postage "330 sats" --csv I:/btc/btcNft/batch.csv --fee-rate {median_fee}'
            print(f"Current medianFee: {median_fee}")   # 打印出当前的medianFee值
            print("Current Time =", formatted_now)
            if median_fee < 6.2:
                send_message_and_execute_command(message, command)
                # time.sleep(120)  # 等待2分钟
                # send_message_and_execute_command(message, command)
            else:
                print("Gas is too high.")
                send_message_and_execute_command(f"WalletBalance", command_wallet_balance)    

            time.sleep(interval_sleep)
            time.sleep(interval_send - interval_sleep)
    except KeyboardInterrupt:
        print("程序已终止。")
