# 姓名：颜君
# 学号：1811511
from sys import exit
from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret
from utils import *
from config import my_private_key, my_public_key, my_address, faucet_address
from ex1 import send_from_P2PKH_transaction


cust1_private_key = CBitcoinSecret(
    'cQV2mLZbq3A9ytjP3LPMqtSznpNSQZSGJ3y5NrnJh8gV5ZFqKorJ')
cust1_public_key = cust1_private_key.pub
cust2_private_key = CBitcoinSecret(
    'cRYgjTjLQ4hjnvHrTvv2tdwT8KsMZb2GHiAj7gnvxH6MuCqzCzU8')
cust2_public_key = cust2_private_key.pub
cust3_private_key = CBitcoinSecret(
    'cShqDKXCEoFD3ih23JzPGm872WejiAoWprmTMoGZzAi26dKyEkML')
cust3_public_key = cust3_private_key.pub


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 3

# You can assume the role of the bank for the purposes of this problem
# and use my_public_key and my_private_key in lieu of bank_public_key and
# bank_private_key.
# 检查银行签名，先确认公钥，再检查银行签名
# 任意一个不为真就停止执行脚本，然后再检查多重签名，若最后证实签名为真，则交易有效
ex2a_txout_scriptPubKey = [OP_DUP, OP_HASH160, my_address, OP_EQUALVERIFY, OP_CHECKSIGVERIFY,OP_1, cust1_public_key, cust2_public_key, cust3_public_key, OP_3,OP_CHECKMULTISIG]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00004999
    txid_to_spend = (
        '415e653b0f84b2145c8d116adf8b7c26035d76d3983aa65eb4ed676b79935af2')
    utxo_index = 2
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        ex2a_txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)
# 交易hash：d5bd341b1f8d53d82865d2790718b7942683f17d385775997fe4f009dceab69e

# 201 Created
# {
#   "tx": {
#     "block_height": -1,
#     "block_index": -1,
#     "hash": "d5bd341b1f8d53d82865d2790718b7942683f17d385775997fe4f009dceab69e",
#     "addresses": [
#       "n2WhjF1Jb7CchPN34ZgcU95X8qo7ZyjX2A",
#       "zCeLB3MCPennqmcbcFN1XHLiZpiKy9Usoh"
#     ],
#     "total": 4999,
#     "fees": 1000,
#     "size": 297,
#     "preference": "low",
#     "relayed_by": "2001:250:401:6566:b034:d8bf:450c:32b2",
#     "received": "2020-11-07T12:42:25.743016743Z",
#     "ver": 1,
#     "double_spend": false,
#     "vin_sz": 1,
#     "vout_sz": 1,
#     "confirmations": 0,
#     "inputs": [
#       {
#         "prev_hash": "415e653b0f84b2145c8d116adf8b7c26035d76d3983aa65eb4ed676b79935af2",
#         "output_index": 2,
#         "script": "483045022100b0074c704044f849282d7a00d62b006d3f0bcb7fd24396b0000912c04d4dc9100220528dbd43f52fc876aa38469706b4c6b9c51208284d65f8581f89f0a582647f7b012103e05ce22c4f8e1e9cb4c38960548bb41c26d3f3b9dc9a8a5a87ad4163fbb6426c",
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
#         "script": "76a914e64e7b8c429afaad85ecbef44493824fa97ea00f88ad512102d4b616a2bc9b96e63d25b8e77fd22c111336cf19e71db1d2079e4b0710c4b9de210220d45c7639a7c3c97160add0882c5d1852e34fd07ced8ac50013d256e4388c55210283eb38c7619b848d7a185d8ee7a72845301de82ba614afb0085d277ea83bf4e553ae",
#         "addresses": [
#           "zCeLB3MCPennqmcbcFN1XHLiZpiKy9Usoh"
#         ],
#         "script_type": "pay-to-multi-pubkey-hash"
#       }
#     ]
#   }
# }