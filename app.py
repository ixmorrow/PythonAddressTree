from web3 import Web3
import requests
import json
from flask import Flask, render_template, request
from etherscan import Etherscan

infuraURL = 'https://mainnet.infura.io/v3/1e38cb5d71f34c468c879476819fb7dd'
etherscanURL = 'https://api.etherscan.io'
token = 'D8T2XEDQGMKMADTZVBM4UCY12NMQ34XX5V'
w3 = Web3(Web3.HTTPProvider(infuraURL))
eth = Etherscan(token)

app = Flask(__name__)


@app.route('/', methods = ['POST', 'GET'])
def hello():
    if request.method == 'POST':
        addr = request.form['ethAddress']
        print(eth.get_eth_balance(addr))
        txs = getTxs(addr)
        print(txs)
        nodes=getNodes(txs)
        print(nodes)
        return render_template('tree.html', data=txs, nodes=nodes)
    else:
        return render_template('index.html')

def getTxs(addr):
    print("Current block number: " + str(w3.eth.block_number))
    txs = (eth.get_normal_txs_by_address(addr, 0, 99999999, 'asc'))
    text = []
    for tx in txs:
        x = {}
        x['from'] = tx['from']
        x['to'] = tx['to']
        x['value'] = tx['value']
        text.append(x)
    return text

def getNodes(transactions):
    nodes = []
    for i in transactions:
        if (i['from'] not in nodes):
            nodes.append(i['from'])
        if (i['to'] not in nodes):
            nodes.append(i['to'])
    return nodes

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)



if __name__ == '__main__':
   app.run(debug = True)

   connected = w3.isConnected()
   print(connected)
   if (connected):
       print(getTxs())
