# 姓名：颜君
# 学号：1811511
from sys import exit
from bitcoin.core.script import *

from utils import *
from config import my_private_key, my_public_key, my_address, faucet_address
from ex1 import send_from_P2PKH_transaction


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2
ex3a_txout_scriptPubKey = [OP_OVER,OP_OVER,OP_ADD,181,OP_EQUALVERIFY,OP_SUB,511,OP_EQUAL]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00004999
    txid_to_spend = (
        '415e653b0f84b2145c8d116adf8b7c26035d76d3983aa65eb4ed676b79935af2')
    utxo_index = 4
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        ex3a_txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)
#交易hash: 07c3d1a4b3da9316922412abf6a831c6d7ead3d250cedb6129fc777af7e860ff
# 201 Created
# {
#   "tx": {
#     "block_height": -1,
#     "block_index": -1,
#     "hash": "07c3d1a4b3da9316922412abf6a831c6d7ead3d250cedb6129fc777af7e860ff",
#     "addresses": [
#       "n2WhjF1Jb7CchPN34ZgcU95X8qo7ZyjX2A"
#     ],
#     "total": 4999,
#     "fees": 1000,
#     "size": 178,
#     "preference": "low",
#     "relayed_by": "106.47.150.141",
#     "received": "2020-11-16T17:22:00.13658536Z",
#     "ver": 1,
#     "double_spend": false,
#     "vin_sz": 1,
#     "vout_sz": 1,
#     "confirmations": 0,
#     "inputs": [
#       {
#         "prev_hash": "415e653b0f84b2145c8d116adf8b7c26035d76d3983aa65eb4ed676b79935af2",
#         "output_index": 4,
#         "script": "47304402206d8b3ecb058afe4f2d74949d78c732aa5429ae1533732dbc5bc0c78bf8d3c713022048482288e374fff4fb16e01c7f19278ba2e6b2e8c8a9049f91aa9be4a4ebc3b1012103e05ce22c4f8e1e9cb4c38960548bb41c26d3f3b9dc9a8a5a87ad4163fbb6426c",
#         "output_value": 5999,
#         "sequence": 4294967295,
#         "addresses": [
#           "n2WhjF1Jb7CchPN34ZgcU95X8qo7ZyjX2A"
#         ],
#         "script_type": "pay-to-pubkey-hash",
#         "age": 1862579
#       }
#     ],
#     "outputs": [
#       {
#         "value": 4999,
#         "script": "78789302b500889402ff0187",
#         "addresses": null,
#         "script_type": "unknown"
#       }
#     ]
#   }
# }