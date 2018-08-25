import requests
PATH = 'project_path'

def get_one_kernel_path(path):
  with open(path) as f:
    l = f.readlines()
    KernelList = l[2].split()
    return KernelList[0]

def line(Me):
    line_notify_token = 'YOUR_TOKEN'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    message = '\n' + Me 
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    line_notify = requests.post(line_notify_api, data=payload, headers=headers)

result_kernel_path = get_one_kernel_path(PATH + "result")
pastResult_kernel_path = get_one_kernel_path(PATH + "pastResult")

if (result_kernel_path != pastResult_kernel_path):
  line('There is a new post on Kernel!')
  line('https://www.kaggle.com/' + result_kernel_path)
