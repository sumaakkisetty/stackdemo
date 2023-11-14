import tkinter as tk

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")

        # Create an entry widget for custom input
        self.input_entry = tk.Entry(root)
        self.input_entry.pack(fill="x")

        # Create buttons for custom input, undo, and redo
        self.custom_input_button = tk.Button(root, text="Custom Input", command=self.custom_input)
        self.undo_button = tk.Button(root, text="Undo", command=self.undo)
        self.redo_button = tk.Button(root, text="Redo", command=self.redo)

        self.custom_input_button.pack()
        self.undo_button.pack()
        self.redo_button.pack()

        # Create a text widget to display and edit text
        self.text_widget = tk.Text(root)
        self.text_widget.pack(fill="both", expand=True)

        # Create stacks for undo and redo
        self.undo_stack = []
        self.redo_stack = []

        # Create an initial state
        self.push_state()

    def push_state(self):
        # Save the current text content in the undo stack
        self.undo_stack.append(self.text_widget.get("1.0", "end"))
        # Clear the redo stack since we're creating a new state
        self.redo_stack = []

    def custom_input(self):
        # Get the text from the input field and insert it into the text widget
        custom_text = self.input_entry.get()
        self.text_widget.insert("end", custom_text)
        self.push_state()  # Save the state after the custom input

    def undo(self):
        if self.undo_stack:
            # Pop the previous state from the undo stack
            previous_state = self.undo_stack.pop()
            # Save the current state in the redo stack
            self.redo_stack.append(self.text_widget.get("1.0", "end"))
            # Update the text content
            self.text_widget.delete("1.0", "end")
            self.text_widget.insert("1.0", previous_state)

    def redo(self):
        if self.redo_stack:
            # Pop the next state from the redo stack
            next_state = self.redo_stack.pop()
            # Save the current state in the undo stack
            self.undo_stack.append(self.text_widget.get("1.0", "end"))
            # Update the text content
            self.text_widget.delete("1.0", "end")
            self.text_widget.insert("1.0", next_state)

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()