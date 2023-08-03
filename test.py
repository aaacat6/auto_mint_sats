import time
import requests
import json
import subprocess
from datetime import datetime# 获取当前时间
import command

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

# def send_message_and_execute_command(message, command_name, command):#发送命令主函数
#     cmd_command = f'echo "{message}" & {command}' #当你在 cmd 中输入 echo Hello, World!，它将会打印出 "Hello, World!"。

#     process = subprocess.Popen(cmd_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)#获取函数是否执行成功
#     stdout, stderr = process.communicate()
#     returncode = process.returncode
#     if returncode == 0:
#         print(f"Command '{command_name}' executed successfully! Output: {stdout.decode('utf-8')}")
#     else:
#         print(f"Command '{command_name}' execution failed! Return code: {returncode}, Error message: {stderr.decode('utf-8')}")
#     return returncode

if __name__ == "__main__":
    interval_send = 10  # 设置发送消息的间隔时间（单位：秒）
    interval_sleep = 1  # 设置发送消息后的休眠时间（单位：秒）

    # command_send_btc_success_count = 0 #函数执行成功的次数

    try:
        while True:
            now = datetime.now()
            formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")# 转换为你想要的格式
            median_fee = get_median_fee()

            # get_command_wallet_balance = command.fun_command_wallet_balance()
            # print(get_command_wallet_balance)
            
            print(command.command_wallet_balance)
            
            # command_send_btc = command.command_send_btc
            print("Current Time =", formatted_now)
            print(f"Current medianFee: {median_fee}")   # 打印出当前的medianFee值
            # send_message_and_execute_command(f"WalletBalance", "get_command_wallet_balance",get_command_wallet_balance) 

            # if command_send_btc_success_count <= 8 :   
            #     if send_message_and_execute_command(f"send btc","command_send_btc", command_send_btc) == 0:
            #         command_send_btc_success_count += 1  # increment successful command_mint_sats counter
            # else :
            #     print("done")
            #     break        
            time.sleep(interval_send)

    except KeyboardInterrupt:
        print("程序已终止。")
