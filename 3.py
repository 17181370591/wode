#https://www.cnblogs.com/ouyangping/p/8453920.html

import itchat as wx, time
from itchat.content import *


wx.auto_login(True)
wx.login()
wx.logout()

#发送信息，这里toUserName参数是朋友的UserName，
#类似于'@a62007da23b483439c6262894fdfd337e5858c3c68d8eea591608b6cd62a13e5'
wx.send('123',toUserName='filehelper')
wx.send('123',toUserName=wx.get_friends()[3]['UserName'])
#还有一种方法是
friend=wx.search_friends(name='柴小起')[0]
friend.send('hello')


#单纯发送信息
wx.send_msg('456','filehelper')

#发图片
wx.send('@img@1.jpg','filehelper')

#发文件
x.send('@fil@1.txt','filehelper')

#返回完整的好友列表
fs=wx.get_friends()

fs[0]['UserName']

wx.search_friends(userName='@e1369b61913fa443d45697cc37668cb2ce22d8dc551c3dcf28ae273c41864386')

#nickname
wx.search_friends(name='柴小起')

wx.search_friends(wechatAccount='littlecodersh')


wx.get_mps()        #将返回完整的工作号列表


get_chatrooms        #返回完整的群聊列表.

search_chatrooms        #群聊搜索.

memberList = itchat.get_frients()[1:]
# 创建群聊, topic 键值为群聊名称.
chatroomUserName = itchat.create_chatroom(memberList, "test chatroom")
# 删除群聊内的用户
itchat.delete_member_from_chatroom(chatroomUserName, memberList[0])
# 增加用户进入群聊.
itchat.add_member_into_chatroom(chatroomUserName, memberList[0], useInvitation=False)

