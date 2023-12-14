import sys
from PyQt5.Qt import QApplication, QMainWindow
from ieee import Ui_IEEE
from model import IEEEModel


class IEEE(QMainWindow, Ui_IEEE):
    def __init__(self):
        super().__init__()

        self.model_one = IEEEModel()
        self.model_two = IEEEModel()
        self.dirty_data_part_one = '0'
        self.dirty_data_part_two = '0'
        self.symbol = '+'
        self.second_part = False
        self.null_second = True

        self.setupUi(self)
        self.init_handlers()
        self.render_data()

    def init_handlers(self):
        for btn in self.btn_group_digits.buttons():
            btn.clicked.connect(self.key_pressed_digits)

        self.btn_reset.clicked.connect(self.key_pressed_reset)
        self.btn_symbol.clicked.connect(self.key_pressed_symbol)
        self.btn_dot.clicked.connect(self.key_pressed_dot)
        self.btn_run.clicked.connect(self.key_pressed_run)
        self.btn_load.clicked.connect(self.key_pressed_load)

    def key_pressed_dot(self):
        self.second_part = True

    def key_pressed_run(self):
        self.model_two = IEEEModel(self.model_one)
        self.model_two.calc()

        self.render_data()

    def key_pressed_load(self):
        self.model_one.load_number(self.dirty_data_part_one, self.dirty_data_part_two, self.symbol)
        self.dirty_data_part_one = '0'
        self.dirty_data_part_two = '0'
        self.symbol = '+'
        self.second_part = False
        self.null_second = True

        self.render_data()

    def key_pressed_symbol(self):
        self.symbol = '-' if self.symbol == '+' else '+'

        self.render_data()

    def key_pressed_reset(self):
        self.dirty_data_part_one = '0'
        self.dirty_data_part_two = '0'
        self.symbol = '+'
        self.second_part = False
        self.null_second = True
        self.model_one.clear()
        self.model_two.clear()

        self.render_data()

    def key_pressed_digits(self):
        digit = self.sender().text()

        if self.second_part:
            if self.null_second:
                self.null_second = False
                self.dirty_data_part_two = digit
            elif len(self.dirty_data_part_one) + len(self.dirty_data_part_two) < 20:
                self.dirty_data_part_two += digit
        else:
            if self.dirty_data_part_one == '0':
                self.dirty_data_part_one = digit
            elif len(self.dirty_data_part_one) + len(self.dirty_data_part_two) < 20:
                self.dirty_data_part_one += digit

        self.render_data()

    def render_data(self):
        data = f'{self.symbol}{self.dirty_data_part_one}.{self.dirty_data_part_two}'
        self.label_input.setText(data)

        check = self.dirty_data_part_one == '0' and self.dirty_data_part_two == '0'
        check = check and self.symbol == '+' and self.model_one.is_empty()
        check = check and self.model_two.is_empty()
        self.btn_reset.setDisabled(check)

        symbol_1, order_1, exp_1 = self.model_one.get_data()
        symbol_2, order_2, exp_2 = self.model_two.get_data()

        self.label_output_symbol.setText(symbol_1)
        self.label_output_symbol_res.setText(symbol_2)
        self.label_output_order.setText(order_1)
        self.label_output_order_res.setText(order_2)
        self.label_output_exp.setText(exp_1)
        self.label_output_exp_res.setText(exp_2)


def main():
    app = QApplication(sys.argv)
    window = IEEE()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
