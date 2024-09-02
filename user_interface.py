import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from analysis_engine import perform_summary_analysis, perform_correlation_analysis, perform_regression_analysis

class DataAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Analyzer")

        self.file_path = None

        # File selection button
        self.file_button = tk.Button(root, text="Select Data File", command=self.load_file)
        self.file_button.pack(pady=10)

        # Analysis type entry
        self.analysis_label = tk.Label(root, text="Analysis Type (summary/correlation/regression):")
        self.analysis_label.pack()
        self.analysis_entry = tk.Entry(root)
        self.analysis_entry.pack(pady=5)

        # Target entry (optional, for regression analysis)
        self.target_label = tk.Label(root, text="Target (for regression analysis):")
        self.target_label.pack()
        self.target_entry = tk.Entry(root)
        self.target_entry.pack(pady=5)

        # Run analysis button
        self.run_button = tk.Button(root, text="Run Analysis", command=self.run_analysis)
        self.run_button.pack(pady=20)

    def load_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])
        if self.file_path:
            messagebox.showinfo("File Selected", f"Selected file: {self.file_path}")
        else:
            messagebox.showwarning("No File Selected", "Please select a file.")

    def run_analysis(self):
        if not self.file_path:
            messagebox.showerror("Error", "No file selected. Please select a file.")
            return
        
        analysis_type = self.analysis_entry.get().strip().lower()
        target = self.target_entry.get().strip()
        
        try:
            if self.file_path.endswith('.xlsx'):
                data = pd.read_excel(self.file_path)
            else:
                data = pd.read_csv(self.file_path)
            
            if analysis_type == 'summary':
                results = perform_summary_analysis(data)
            elif analysis_type == 'correlation':
                results = perform_correlation_analysis(data)
            elif analysis_type == 'regression':
                if not target:
                    raise ValueError("Target must be specified for regression analysis.")
                results = perform_regression_analysis(data, target)
            else:
                raise ValueError(f"Unsupported analysis type '{analysis_type}'")
            
            # Display results
            results_str = str(results) if not isinstance(results, pd.DataFrame) else results.to_string()
            messagebox.showinfo("Analysis Results", results_str)
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = DataAnalyzerApp(root)
    root.mainloop()

