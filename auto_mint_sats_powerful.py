import time
import os
import json
import subprocess
from datetime import datetime# 获取当前时间
import random

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
    interval_send = 5  # 设置发送消息的间隔时间（单位：秒）
    interval_sleep = 1  # 设置发送消息后的休眠时间（单位：秒）
    
    random_number = random.uniform(6, 6.2)
    rounded_number = round(random_number, 2)

    command_mint_sats_success_count = 0 #函数执行成功的次数

    try:
        while True:
            now = datetime.now()
            formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")# 转换为你想要的格式
            random_number = random.uniform(5.9 6.2)
            rounded_number = round(random_number, 2)

            command_mint_sats = f'ord.exe --bitcoin-data-dir "I:/BitcoinNode/blocks" --cookie-file "I:/BitcoinNode/.cookie" --wallet ac_sats wallet inscribe --postage "330 sats" --csv I:/btc/btcNft/batch.csv --fee-rate {random_number}'
            command_transfer_sats = f'ord.exe --bitcoin-data-dir "I:/BitcoinNode/blocks" --cookie-file "I:/BitcoinNode/.cookie" --wallet ac_sats wallet inscribe --postage "330 sats" --destination bc1pgc7tz23sh6h75zqase2dq82zdwtp9eq00vpwafrvptul3ukmlg5q9pqp38 I:/btc/btcNft/brc20_transfer.txt --fee-rate {random_number}'  
            command_wallet_balance = 'ord.exe --bitcoin-data-dir "I:/BitcoinNode/blocks" --cookie-file "I:/BitcoinNode/.cookie" --wallet ac_sats wallet balance' 

            print("Current Time =", formatted_now)
            # print(f"Current medianFee: {median_fee}")   # 打印出当前的medianFee值
            send_message_and_execute_command(f"WalletBalance", "command_wallet_balanc",command_wallet_balance) 

            if send_message_and_execute_command(f"MintSats","command_mint_sats", command_mint_sats) == 0:
                command_mint_sats_success_count += 1  # increment successful command_mint_sats counter
            if command_mint_sats_success_count == 43:  # check if command has been executed 43 times
                send_message_and_execute_command("Transferring Sats","command_transfer_sats", command_transfer_sats)
                command_mint_sats_success_count = 0  # reset command counter

            time.sleep(interval_sleep)
            time.sleep(interval_send - interval_sleep)
    except KeyboardInterrupt:
        print("程序已终止。")
