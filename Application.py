from blockNavigator import BlockNavigator
from PyQt6.QtWidgets import QWidget
from PyQt6 import QtWidgets


class Application(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('BlockCypher')
        self.setFixedSize(580, 640)

        self.Navi = BlockNavigator()
        self.app_layout = QtWidgets.QVBoxLayout(self)
        self.control_area()
        self.info_area()
        self.tx_area()
        self.warning_box()
        self.update_boxes()
        # self.show()

    def control_area(self):

        # input box
        self.input = QtWidgets.QLineEdit()
        self.app_layout.addWidget(self.input)

        # 4 buttons
        self.four_buttons = QtWidgets.QHBoxLayout()
        self.search = QtWidgets.QPushButton('Search')
        self.search.clicked.connect(self.search_func)
        self.go_left = QtWidgets.QPushButton('Go Left')
        self.go_left.clicked.connect(self.go_left_func)
        self.go_right = QtWidgets.QPushButton('Go Right')
        self.go_right.clicked.connect(self.go_right_func)
        self.four_buttons.addWidget(self.search)
        self.four_buttons.addWidget(self.go_left)
        self.four_buttons.addWidget(self.go_right)
        self.app_layout.addLayout(self.four_buttons)

    def info_area(self):
        self.info_form = QtWidgets.QFormLayout()
        self.fields = ('hash', 'height', 'size', 'time', 'relayed_by', 'fees', 'n_tx')
        self.info_boxes = {}
        for field in self.fields:
            box = QtWidgets.QLineEdit()
            box.setFixedSize(450, 30)
            box.setReadOnly(True)
            self.info_form.addRow(field, box)
            self.info_boxes[field] = box

        self.app_layout.addLayout(self.info_form)

    def tx_area(self):
        self.tx_form = QtWidgets.QFormLayout()
        txt = str(self.Navi.get_tx_dict())
        self.input_box = QtWidgets.QTextEdit()
        self.output_box = QtWidgets.QTextEdit()
        self.input_box.setReadOnly(True)
        self.input_box.setFixedSize(450, 90)
        self.output_box.setReadOnly(True)
        self.output_box.setFixedSize(450, 90)

        self.tx_form.addRow('Input TX', self.input_box)
        self.tx_form.addRow('Output TX', self.output_box)

        self.app_layout.addLayout(self.tx_form)

    def warning_box(self):
        self.warning_msg = QtWidgets.QLineEdit()
        self.warning_msg.setReadOnly(True)
        self.app_layout.addWidget(self.warning_msg)

    def warning(self, txt):
        self.warning_msg.setText(txt)

    def clear_warning(self):
        self.warning_msg.clear()

    def update_boxes(self):
        self.block_data = self.Navi.get_block_dict()
        for field in self.fields:
            self.info_boxes[field].setText(str(self.block_data[field]))

        self.input_tx, self.output_tx = self.Navi.get_tx_dict()
        in_total, out_total = sum([v[1] for v in self.input_tx]), sum([v[1] for v in self.output_tx])
        in_text, out_text = "Total: " + str(in_total), "Total: " + str(out_total)

        for i in self.input_tx:
            in_text += f"\n->{i[0]} : {i[1]}"
        for i in self.output_tx:
            out_text += f"\n->{i[0]} : {i[1]}"

        self.input_box.setText(in_text)
        self.output_box.setText(out_text)

    def search_func(self):
        self.clear_warning()
        try:
            self.Navi.jump(self.input.text())
            self.update_boxes()
        except ValueError as e:
            self.warning(str(e))

    def go_left_func(self):
        self.clear_warning()
        try:
            self.Navi.go_prev()
            self.update_boxes()
        except ValueError as e:
            self.warning(str(e))

    def go_right_func(self):
        self.clear_warning()
        try:
            self.Navi.go_next()
            self.update_boxes()
        except ValueError as e:
            self.warning(str(e))
