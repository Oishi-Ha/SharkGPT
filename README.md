# SharkGPT

如何在 AWS Lightsail 上搭建 ChatGPT API 网站，以及我走了哪些弯路
营销号标题：使用 ChatGPT 搭建属于自己的 ChatGPT

**背景描绘**

ChatGPT的使用途径主要包含了两种互动模式——浏览器(Browser) 和应用程序接口(API)。其中，浏览器模式可以让我们通过虚拟专用网络(VPN)的形式登陆并体验 ChatGPT。然而，一旦我们需要进行二次开发——无论是构建自己的 ChatGPT 网站，还是将 ChatGPT 整合到自身的软件项目中，亦或是对 ChatGPT 本身进行深度定制，或者进行提示(prompt)训练，此时我们就需要借助 ChatGPT 的 API。然而，由于中国大陆的网络限制，我们无法直接链接到 ChatGPT API。为此，我使用的解决方案是：在亚马逊云服务（AWS）中购买位于美国的服务器，并在这台服务器上构建完备的运行环境。

**思维导图**
![image](https://github.com/Oishi-Ha/SharkGPT/assets/52454458/045f86f5-f4ff-4f31-baf4-e624657a81cb)

**技术选型**

AWS Lightsail（Ubuntu 20.04） + XShell + ChatGPT API

**需要什么**

1. ChatGPT 账号（获取 API Key）
2. AWS 全球区账号（搭建 Lightsail）
3. 基础 python 知识和 Linux 知识。

**说明步骤**

1. 准备 OpenAI API Key
    
    登陆OpenAI 官网查看 API 文档 https://platform.openai.com/docs/quickstart ，在 ****Add your API key 那里申请自己的 API key****
    
2. 在 AWS Lightsail 上开启实例
    
    使用 AWS Lightsail (价格比 EC2 低，更适合小项目，当然用 EC2 也可以) 开启实例，并设置安全组。
    
    1. 注意点一：AWS 的 SSH key 默认是密钥文件，需要妥善保管。使用 XShell 可以轻松登录，不过注意宝塔好像不好登录（拓展点一：远程 SSH 工具介绍）
    2. 注意点二：系统版本选择，我选择的是 Ubuntu 20.04，这里不太建议选择 Amazon Linux，因为这个系统的中文资料较少，缺乏了解（拓展点二：服务器 Linux 系统介绍）。我一开始使用了  Amazon Linux 和 CentOS 9，至少宝塔不好做兼容。
3. 通过 XShell 连接 Lightsail 并初始化 Linux 系统，执行以下命令：
    1. sudo passwd
    2. su root
    3. sudo apt update
    4. sudo apt install lrzsz -y
    5. sudo apt install unrar -y
    6. sudo apt install python3
    7. apt-get install python3-venv
    8. python3 --version
    9. rz
    10. unrar x OpenAI_a.rar
    11. cd OpenAI_a
    12. sudo python3 -m venv venv
    13. . venv/bin/activate
    14. pip install -r requirements.txt
    15. flask run --host=0.0.0.0 --port=5000   # 注意这里跟官网有不同（注意点三）
4. 通过 http://public ip:5000/ 访问 Demo
    
    

关键词热点：ChatGPT，搭建自己的 ChatGPT，薅 AWS 羊毛，网站搭建
