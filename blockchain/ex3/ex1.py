from bitcoin.core.script import *

from utils import *
from config import (my_private_key, my_public_key, my_address,
                    faucet_address)


def P2PKH_scriptPubKey(address):#输出脚本
    ######################################################################
    # TODO: Complete the standard scriptPubKey implementation for a
    # PayToPublicKeyHash transaction
    return [OP_DUP,OP_HASH160,address,OP_EQUALVERIFY,OP_CHECKSIG]
    ######################################################################


def P2PKH_scriptSig(txin, txout, txin_scriptPubKey):#输入脚本
    signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             my_private_key)
    ######################################################################
    # TODO: Complete this script to unlock the BTC that was sent to you
    # in the PayToPublicKeyHash transaction. You may need to use variables
    # that are globally defined.
    return [signature,my_public_key]
    ######################################################################


def send_from_P2PKH_transaction(amount_to_send, txid_to_spend, utxo_index,
                                txout_scriptPubKey):
    txout = create_txout(amount_to_send, txout_scriptPubKey)

    txin_scriptPubKey = P2PKH_scriptPubKey(my_address)
    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = P2PKH_scriptSig(txin, txout, txin_scriptPubKey)

    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig)

    return broadcast_transaction(new_tx)


if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00004999
    txid_to_spend = (
        '415e653b0f84b2145c8d116adf8b7c26035d76d3983aa65eb4ed676b79935af2')
    utxo_index = 1
    ######################################################################


    txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)
    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index, txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)
