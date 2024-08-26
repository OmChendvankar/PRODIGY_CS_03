import sys
import re
import random
import string
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QListWidget, QListWidgetItem, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt
from PySide6.QtGui import QClipboard

class PasswordStrengthChecker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Password Strength Checker')

        # Create widgets
        self.password_input = QLineEdit(self)
        self.feedback_label = QLabel('', self)
        self.show_password_button = QPushButton('Show', self)
        self.suggestions_list = QListWidget(self)

        # Set widget properties
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.show_password_button.setCheckable(True)

        # Connect signals
        self.password_input.textChanged.connect(self.update_feedback)
        self.password_input.textChanged.connect(self.generate_suggestions)
        self.show_password_button.toggled.connect(self.toggle_password_visibility)

        # Set layout
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.password_input)
        input_layout.addWidget(self.show_password_button)

        # Add a spacer item to create a gap
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        layout = QVBoxLayout()
        layout.addWidget(QLabel('Enter your password:'))
        layout.addLayout(input_layout)
        layout.addWidget(self.feedback_label)
        layout.addItem(spacer)  # Add the spacer to create a gap
        layout.addWidget(QLabel('Password Suggestions:'))
        layout.addWidget(self.suggestions_list)
        self.setLayout(layout)

        self.resize(300, 300)

    def update_feedback(self):
        password = self.password_input.text()
        feedback = self.check_password_strength(password)
        self.feedback_label.setText(feedback)

    def check_password_strength(self, password):
        strength = 0
        if len(password) >= 8:
            strength += 1
        if re.search(r'[a-z]', password):
            strength += 1
        if re.search(r'[A-Z]', password):
            strength += 1
        if re.search(r'\d', password):
            strength += 1
        if re.search(r'[\W_]', password):
            strength += 1

        if strength <= 2:
            return 'Weak password'
        elif strength == 3:
            return 'Medium strength password'
        else:
            return 'Strong password'

    def generate_suggestions(self):
        current_password = self.password_input.text()
        self.suggestions_list.clear()

        if current_password:
            suggestions = self.generate_password_suggestions(current_password)
            for suggestion in suggestions:
                self.add_suggestion_item(suggestion)

    def generate_password_suggestions(self, base_password, num_suggestions=3):
        suggestions = []
        for _ in range(num_suggestions):
            suggestion = self.mutate_password(base_password)
            suggestions.append(suggestion)
        return suggestions

    def mutate_password(self, password):
        # Randomly capitalize letters
        password = ''.join(random.choice([c.upper(), c.lower()]) if c.isalpha() else c for c in password)
        
        # Randomly replace some characters with numbers or symbols
        replacements = {
            'a': '@', 's': '$', 'i': '1', 'o': '0', 'e': '3', 'l': '!', 't': '7'
        }
        password = ''.join(replacements.get(c.lower(), c) if random.random() < 0.3 else c for c in password)

        # Add a random number or symbol at the end
        password += random.choice(string.digits + string.punctuation)
        
        return password

    def add_suggestion_item(self, suggestion):
        item_widget = QWidget()
        item_layout = QHBoxLayout()

        # Suggestion label
        suggestion_label = QLabel(suggestion)

        # Copy button
        copy_button = QPushButton('Copy')
        copy_button.setFixedWidth(60)
        copy_button.setVisible(False)
        copy_button.clicked.connect(lambda: self.copy_to_clipboard(suggestion))

        # Add widgets to layout
        item_layout.addWidget(suggestion_label)
        item_layout.addWidget(copy_button)
        item_layout.addStretch()
        item_widget.setLayout(item_layout)

        # Add item to list
        list_item = QListWidgetItem(self.suggestions_list)
        list_item.setSizeHint(item_widget.sizeHint())
        self.suggestions_list.addItem(list_item)
        self.suggestions_list.setItemWidget(list_item, item_widget)

        # Show copy button on hover
        item_widget.enterEvent = lambda event: copy_button.setVisible(True)
        item_widget.leaveEvent = lambda event: copy_button.setVisible(False)

    def copy_to_clipboard(self, text):
        clipboard = QApplication.clipboard()
        clipboard.setText(text)

    def toggle_password_visibility(self, checked):
        if checked:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
            self.show_password_button.setText('Hide')
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
            self.show_password_button.setText('Show')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PasswordStrengthChecker()
    window.show()
    sys.exit(app.exec())