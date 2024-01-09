import os

from stock_analyzer.process import stock_analyze

if __name__ == "__main__":
    project_dir = "/Users/tramln/working/apple_stock"
    input_file = os.path.join(project_dir, "/data_source/finance-charts-apple.csv")
    output_dir = "/Users/tramln/working/test"
    stock_analyze(input_file, output_dir)
