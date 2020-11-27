# 姓名：颜君
# 学号：1811511
from sys import exit
from bitcoin.core.script import *

from utils import *
from config import my_private_key, my_public_key, my_address, faucet_address
from ex1 import P2PKH_scriptPubKey
from ex2a import (ex2a_txout_scriptPubKey, cust1_private_key, cust2_private_key,
                  cust3_private_key,cust1_public_key,cust2_public_key,cust3_public_key)


def multisig_scriptSig(txin, txout, txin_scriptPubKey):
    bank_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             my_private_key)
    cust1_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             cust1_private_key)
    cust2_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             cust2_private_key)
    cust3_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             cust3_private_key)
    ######################################################################
    # TODO: Complete this script to unlock the BTC that was locked in the
    # multisig transaction created in Exercise 2a.
    #把用户1签名、银行签名和公钥依次入栈
    return [OP_0,cust1_sig,bank_sig, my_public_key]
    ######################################################################


def send_from_multisig_transaction(amount_to_send, txid_to_spend, utxo_index,
                                   txin_scriptPubKey, txout_scriptPubKey):
    txout = create_txout(amount_to_send, txout_scriptPubKey)

    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = multisig_scriptSig(txin, txout, txin_scriptPubKey)

    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig)

    return broadcast_transaction(new_tx)

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00003999
    txid_to_spend = 'd5bd341b1f8d53d82865d2790718b7942683f17d385775997fe4f009dceab69e'
    utxo_index = 0
    ######################################################################

    txin_scriptPubKey = ex2a_txout_scriptPubKey
    txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)

    response = send_from_multisig_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        txin_scriptPubKey, txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)
# 交易hash:4c986313f3d0d41d2db014a8357541ac7ecda15f33ea74d534581f7cace942a5

# 201 Created
# {
#   "tx": {
#     "block_height": -1,
#     "block_index": -1,
#     "hash": "4c986313f3d0d41d2db014a8357541ac7ecda15f33ea74d534581f7cace942a5",
#     "addresses": [
#       "mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB",
#       "zCeLB3MCPennqmcbcFN1XHLiZpiKy9Usoh"
#     ],
#     "total": 3999,
#     "fees": 1000,
#     "size": 264,
#     "preference": "low",
#     "relayed_by": "2001:250:401:6566:b034:d8bf:450c:32b2",
#     "received": "2020-11-07T12:46:43.037448415Z",
#     "ver": 1,
#     "double_spend": false,
#     "vin_sz": 1,
#     "vout_sz": 1,
#     "confirmations": 0,
#     "inputs": [
#       {
#         "prev_hash": "d5bd341b1f8d53d82865d2790718b7942683f17d385775997fe4f009dceab69e",
#         "output_index": 0,
#         "script": "004730440220494666182d4a5e4506509920951b1a5d253943eb1319c2d9702186a146df1698022000d2332572c9a4733153c20ff7bdbdd04c4e42660e6fd4e0dc8c2daeb00dd42a0147304402207849588150a92d8a7ab6481b1a16bf1bb82c85eae9e1dda207bcd9f8ecf4624302207d949b67d86fe8cfa6ae5450fef72db373838dbb3af01420eef5d9ce3b9d5b35012103e05ce22c4f8e1e9cb4c38960548bb41c26d3f3b9dc9a8a5a87ad4163fbb6426c",
#         "output_value": 4999,
#         "sequence": 4294967295,
#         "addresses": [
#           "zCeLB3MCPennqmcbcFN1XHLiZpiKy9Usoh"
#         ],
#         "script_type": "pay-to-multi-pubkey-hash",
#         "age": 1889366
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