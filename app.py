from process import stock_analyze

if __name__ == "__main__":

    input_file = "/Users/tramln/working/apple_interview/app/stock_analyzer/data_source/finance-charts-apple.csv"
    output_dir = "/Users/tramln/working/apple_interview/app/stock_analyzer/data_output"

    stock_analyze(input_file, output_dir)
