from block import Block


class BlockNavigator:
    def __init__(self, height=None, hash=None):
        self.height = height
        self.update()

    def update(self):
        self.block = Block(self.height)
        self.height = self.block.get_height()

    def check_error(self):
        if 'error' in self.block.get_block().keys():
            raise ValueError(self.block.get_block()['error'])

    def go_next(self):
        self.height += 1
        self.update()
        self.check_error()
        return self.get_block_dict()

    def go_prev(self):
        self.height -= 1
        self.update()
        self.check_error()
        return self.get_block_dict()

    def jump(self, height_hash):
        try:
            self.block = Block(height_hash)
            self.height = self.block.get_height()
            return self.get_block_dict()
        except:
            raise ValueError('Invalid Hash or height')

    def get_block_dict(self):
        return self.block.get_block_info()

    def get_tx_dict(self):
        return self.block.get_tx_info()
