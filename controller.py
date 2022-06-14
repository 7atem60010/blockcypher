import blockcypher
from dotenv import load_dotenv

load_dotenv()


class Info:
    def __init__(self, block):
        self.token = "$TOKEN"
        self.current = block

    def get_height(self):
        return self.block['height']

    def get_block_size(self):
        return self.block['size']

    def get_time(self):
        return self.block['time']
