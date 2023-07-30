import time
import os
import requests
import json
import subprocess
from datetime import datetime# 获取当前时间

def get_median_fee():#获取当前中位数gas费
  while True:
     try:
       response = requests.get("https://mempool.space/api/v1/fees/mempool-blocks")
       data = json.loads(response.text)
       median_fee = data[0]['medianFee'] # 获取最新的块（列表的第一个元素）的 'medianFee' 值
       return median_fee
     except requests.exceptions.ConnectionError:
       print("Connection error, retrying...")
       time.sleep(5) 

def send_message_and_execute_command(message, command_name, command):#发送命令主函数
    cmd_command = f'echo "{message}" & {command}'

    process = subprocess.Popen(cmd_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)#获取函数是否执行成功
    stdout, stderr = process.communicate()
    returncode = process.returncode
    if returncode == 0:
        print(f"Command '{command_name}' executed successfully! Output: {stdout.decode('utf-8')}")
    else:
        print(f"Command '{command_name}' execution failed! Return code: {returncode}, Error message: {stderr.decode('utf-8')}")
    return returncode

if __name__ == "__main__":
    interval_send = 30  # 设置发送消息的间隔时间（单位：秒）
    interval_sleep = 1  # 设置发送消息后的休眠时间（单位：秒）

    command_mint_sats_success_count = 0 #函数执行成功的次数

    try:
        while True:
            interval_send = 30
            now = datetime.now()
            formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")# 转换为你想要的格式
            median_fee = get_median_fee()

            command_mint_sats = f'ord.exe --bitcoin-data-dir "I:/BitcoinNode/blocks" --cookie-file "I:/BitcoinNode/.cookie" --wallet ac_sats wallet inscribe --postage "330 sats" --csv I:/btc/btcNft/batch.csv --fee-rate {median_fee}'
            command_transfer_sats = f'ord.exe --bitcoin-data-dir "I:/BitcoinNode/blocks" --cookie-file "I:/BitcoinNode/.cookie" --wallet ac_sats wallet inscribe --postage "330 sats" --destination bc1pgc7tz23sh6h75zqase2dq82zdwtp9eq00vpwafrvptul3ukmlg5q9pqp38 I:/btc/btcNft/brc20_transfer.txt --fee-rate {median_fee}'  
            command_wallet_balance = 'ord.exe --bitcoin-data-dir "I:/BitcoinNode/blocks" --cookie-file "I:/BitcoinNode/.cookie" --wallet ac_sats wallet balance' 

            print("Current Time =", formatted_now)
            print(f"Current medianFee: {median_fee}")   # 打印出当前的medianFee值
            send_message_and_execute_command(f"WalletBalance", "command_wallet_balanc",command_wallet_balance) 

            if median_fee <= 6.2:
                interval_send = 5
                if send_message_and_execute_command(f"MintSats","command_mint_sats", command_mint_sats) == 0:
                    command_mint_sats_success_count += 1  # increment successful command_mint_sats counter
                if command_mint_sats_success_count == 43:  # check if command has been executed 43 times
                    send_message_and_execute_command("Transferring Sats","command_transfer_sats", command_transfer_sats)
                    command_mint_sats_success_count = 0  # reset command counter
            else:
                print("Gas is too high.")
   
            time.sleep(interval_sleep)
            time.sleep(interval_send - interval_sleep)
    except KeyboardInterrupt:
        print("程序已终止。")
