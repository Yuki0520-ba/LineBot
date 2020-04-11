import sys
import requests
import json


#引数のワードでapi叩く
#返ってきたjsonをパース
#返ってきた中のbestResponseをreturnする
def api_reply(message,user_name):
    chaplusUrl = "https://www.chaplus.jp/v1/chat?apikey=5e9123b1ed5d2"

    detail= {
        'utterance': message,
        'username' : user_name,
        'agentState' : {
            'agentName' : 'oreore',
            'age' : '18歳',
            'tone' : 'kansai'
        }
    }

    response=requests.post(chaplusUrl,json.dumps(detail))
    lists = json.loads(response.text)

    return lists["bestResponse"]["utterance"]



#コマンドライン入力で実行　第二引数を引数としてreplyを実行
#replyから返ってきたものを標準出力
def main():
    res=api_reply(sys.argv[1],'太郎')
    print(res)
    

if __name__ == '__main__':
    main()