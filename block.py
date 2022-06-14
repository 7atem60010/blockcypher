from dotenv import load_dotenv
import blockcypher

load_dotenv()
TX_LIM = 1


class Block:
    def __init__(self, height_hash):
        self.token = "$TOKEN"
        self.height_hash = height_hash
        if not self.height_hash:
            self.height_hash = blockcypher.get_blockchain_overview()['height']
            print(str(self.height_hash))
        self.block = blockcypher.get_block_overview(str(self.height_hash), api_key=None)

    def _retrieve_block(self, height):
        if not height:
            height = blockcypher.get_blockchain_overview()['height']
        block = blockcypher.get_block_overview(str(height), txn_limit=TX_LIM, txn_offset=2)
        return block

    def get_block(self):
        return self.block

    def get_height(self):
        try:
            return int(self.block['height'])
        except:
            raise ValueError("Block with this height/hash not found!")

    def get_block_info(self):
        keys = ('hash', 'height', 'size', 'time', 'relayed_by', 'fees', 'n_tx')
        return {k: self.block[k] for k in keys}

    def get_tx_info(self):
        txid = self.block['txids'][1]
        tx = blockcypher.get_transaction_details(txid)
        # print(tx['inputs'])
        input_tx = [[d['addresses'][0], int(d['output_value'])] for d in tx['inputs']]
        output_tx = [[d['addresses'][0], int(d['value'])] for d in tx['outputs']]
        return input_tx, output_tx
