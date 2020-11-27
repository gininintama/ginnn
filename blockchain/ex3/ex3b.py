# 姓名：颜君
# 学号：1811511
from sys import exit
from bitcoin.core.script import *

from utils import *
from config import my_private_key, my_public_key, my_address, faucet_address
from ex1 import P2PKH_scriptPubKey
from ex3a import ex3a_txout_scriptPubKey


######################################################################
# TODO: set these parameters correctly
amount_to_send = 0.00003999
txid_to_spend = '07c3d1a4b3da9316922412abf6a831c6d7ead3d250cedb6129fc777af7e860ff'
utxo_index = 0
######################################################################

txin_scriptPubKey = ex3a_txout_scriptPubKey
######################################################################
# TODO: implement the scriptSig for redeeming the transaction created
# in  Exercise 3a.
txin_scriptSig = [346,-165]
######################################################################
txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)

response = send_from_custom_transaction(
    amount_to_send, txid_to_spend, utxo_index,
    txin_scriptPubKey, txin_scriptSig, txout_scriptPubKey)
print(response.status_code, response.reason)
print(response.text)
#交易hash: 840ffa94fd215c559cc3692db3cff419bdb4963ff5f9dc9638b6090ecf29adfe
# 201 Created
# {
#   "tx": {
#     "block_height": -1,
#     "block_index": -1,
#     "hash": "840ffa94fd215c559cc3692db3cff419bdb4963ff5f9dc9638b6090ecf29adfe",
#     "addresses": [
#       "mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB"
#     ],
#     "total": 3999,
#     "fees": 1000,
#     "size": 91,
#     "preference": "low",
#     "relayed_by": "106.47.150.141",
#     "received": "2020-11-16T17:23:23.968018923Z",
#     "ver": 1,
#     "double_spend": false,
#     "vin_sz": 1,
#     "vout_sz": 1,
#     "confirmations": 0,
#     "inputs": [
#       {
#         "prev_hash": "07c3d1a4b3da9316922412abf6a831c6d7ead3d250cedb6129fc777af7e860ff",
#         "output_index": 0,
#         "script": "025a0102a580",
#         "output_value": 4999,
#         "sequence": 4294967295,
#         "script_type": "unknown",
#         "age": 0
#       }
#     ],
#     "outputs": [
#       {
#         "value": 3999,
#         "script": "76a9149f9a7abd600c0caa03983a77c8c3df8e062cb2fa88ac",
#         "addresses": [
#           "mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB"
#         ],
#         "script_type": "pay-to-pubkey-hash"
#       }
#     ]
#   }
# }